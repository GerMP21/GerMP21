#!/usr/bin/env python3
"""Fetch GitHub stats and draw ../assets/stats.svg in the profile's style.

Runs daily in .github/workflows/stats.yml. Uses only the standard library.

    GH_TOKEN=... python3 scripts/build_stats.py            # real data
    python3 scripts/build_stats.py --sample out.svg        # fake data, for previewing the design
    python3 scripts/build_stats.py --placeholder           # "first run pending" card

Contribution counts cover the last year. With the workflow's built-in token
they include public contributions only; with a personal access token in the
STATS_TOKEN secret they also count private contributions (as a total, with no
repository names). Repos, stars and languages always come from public,
non-fork repositories, so nothing about private repositories is shown.
"""
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_svgs import OUT, svg, text  # noqa: E402  (shared style)

LOGIN = "GerMP21"
TOP_LANGUAGES = 6

QUERY = """
query($login: String!, $cursor: String) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar { totalContributions }
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      totalPullRequestReviewContributions
      restrictedContributionsCount
    }
    repositories(first: 100, after: $cursor, ownerAffiliations: OWNER,
                 isFork: false, privacy: PUBLIC) {
      totalCount
      pageInfo { hasNextPage endCursor }
      nodes {
        stargazerCount
        languages(first: 20, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name } }
        }
      }
    }
  }
}
"""


def graphql(token, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {token}", "User-Agent": "profile-stats"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.load(r)
    if body.get("errors"):
        raise SystemExit(f"GitHub API error: {body['errors']}")
    return body["data"]["user"]


def fetch(token):
    cursor, stars, langs, first = None, 0, {}, None
    while True:
        user = graphql(token, {"login": LOGIN, "cursor": cursor})
        first = first or user
        repos = user["repositories"]
        for repo in repos["nodes"]:
            stars += repo["stargazerCount"]
            for edge in repo["languages"]["edges"]:
                name = edge["node"]["name"]
                langs[name] = langs.get(name, 0) + edge["size"]
        if not repos["pageInfo"]["hasNextPage"]:
            break
        cursor = repos["pageInfo"]["endCursor"]
    c = first["contributionsCollection"]
    return {
        "contributions": c["contributionCalendar"]["totalContributions"],
        "commits": c["totalCommitContributions"],
        "prs": c["totalPullRequestContributions"],
        "issues": c["totalIssueContributions"],
        "reviews": c["totalPullRequestReviewContributions"],
        "private": c["restrictedContributionsCount"],
        "repos": first["repositories"]["totalCount"],
        "stars": stars,
        "languages": langs,
    }


SAMPLE = {
    "contributions": 1234, "commits": 987, "prs": 56, "issues": 12, "reviews": 34,
    "private": 400, "repos": 18, "stars": 21,
    "languages": {"Python": 500, "Rust": 300, "TypeScript": 150, "JavaScript": 120,
                  "Shell": 60, "CSS": 20, "PHP": 5},
}


def render(s, updated):
    rows = [
        ("CONTRIBUTIONS", f"{s['contributions']:,}", "last 12 months"),
        ("COMMITS", f"{s['commits']:,}", ""),
        ("PULL REQUESTS", f"{s['prs']:,}", ""),
        ("ISSUES", f"{s['issues']:,}", ""),
        ("REVIEWS", f"{s['reviews']:,}", ""),
        ("PUBLIC REPOS", f"{s['repos']:,}", "excluding forks"),
        ("STARS", f"{s['stars']:,}", "on public repos"),
    ]
    if s.get("private"):
        rows.insert(1, ("PRIVATE", f"{s['private']:,}", "contributions"))

    total = sum(s["languages"].values()) or 1
    langs = sorted(s["languages"].items(), key=lambda kv: kv[1], reverse=True)[:TOP_LANGUAGES]

    top, row = 40, 34
    height = top + row * max(len(rows), len(langs) + 1) + 28
    b = ""
    # left column: numbers
    for i, (label, value, note) in enumerate(rows):
        y = top + row * i
        delay = f"animation-delay:{0.15 + i * 0.08:.2f}s"
        b += f'<g class="fade" style="{delay}">'
        b += text(48, y, escape(label), 11.5, "accent", spacing=3).rstrip()
        b += text(300, y, escape(value), 15, "ink", anchor="end").rstrip()
        if note:
            b += text(316, y, escape(note), 11.5, "dim").rstrip()
        b += f'<line x1="48" y1="{y + 13}" x2="470" y2="{y + 13}" class="rule"/>'
        b += "</g>\n"
    # right column: languages
    b += text(530, top, "TOP LANGUAGES", 11.5, "accent", "fade d1", spacing=3)
    b += text(952, top, "public repos, by code size", 11.5, "dim", "fade d1", anchor="end")
    for i, (name, size) in enumerate(langs, start=1):
        y = top + row * i
        pct = size / total * 100
        width = max(2, 190 * size / langs[0][1])
        delay = f"animation-delay:{0.2 + i * 0.1:.2f}s"
        b += f'<g class="fade" style="{delay}">'
        b += text(530, y, escape(name), 14, "ink").rstrip()
        b += f'<rect x="695" y="{y - 9}" width="{width:.1f}" height="8" class="bar"/>'
        b += text(952, y, f"{pct:.1f}%", 12.5, "muted", anchor="end").rstrip()
        b += f'<line x1="530" y1="{y + 13}" x2="952" y2="{y + 13}" class="rule"/>'
        b += "</g>\n"
    b += text(952, height - 14, f"UPDATED {updated}", 10.5, "dim", "fade d6", anchor="end", spacing=3)
    title = (f"GitHub stats: {s['contributions']} contributions in the last year, "
             f"{s['repos']} public repos, {s['stars']} stars; top languages "
             + ", ".join(n for n, _ in langs))
    return svg(1000, height, title, b).replace(
        "</style>", "  .bar { fill: var(--accent); opacity: .85; }\n</style>", 1)


def placeholder():
    b = text(48, 40, "STATS", 11.5, "accent", spacing=3)
    b += text(160, 40, "generated daily by a GitHub Action · first run pending", 13, "muted")
    b += '<line x1="48" y1="56" x2="952" y2="56" class="rule"/>\n'
    return svg(1000, 72, "GitHub stats: first run pending", b)


def main():
    OUT.mkdir(exist_ok=True)
    args = sys.argv[1:]
    if args[:1] == ["--placeholder"]:
        (OUT / "stats.svg").write_text(placeholder(), encoding="utf-8")
        return
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if args[:1] == ["--sample"]:
        out = Path(args[1]) if len(args) > 1 else OUT / "stats-sample.svg"
        out.write_text(render(SAMPLE, today), encoding="utf-8")
        print("wrote", out)
        return
    token = os.environ.get("GH_TOKEN")
    if not token:
        raise SystemExit("Set GH_TOKEN (the workflow passes STATS_TOKEN or GITHUB_TOKEN).")
    path = OUT / "stats.svg"
    new = render(fetch(token), today)
    # Don't rewrite (and commit) the file when only the date would change
    strip = lambda s: re.sub(r"UPDATED \d{4}-\d{2}-\d{2}", "", s)
    if path.exists() and strip(path.read_text(encoding="utf-8")) == strip(new):
        print("stats unchanged; keeping", path)
        return
    path.write_text(new, encoding="utf-8")
    print("wrote", path)


if __name__ == "__main__":
    main()
