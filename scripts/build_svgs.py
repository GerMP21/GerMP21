#!/usr/bin/env python3
"""Generate the profile's SVG assets into ../assets.

Every SVG adapts to GitHub's light and dark themes with a
prefers-color-scheme media query, uses the system monospace font, and
respects prefers-reduced-motion. The profile text lives in
content/profile.md; this script turns it into SVG cards and writes
README.md. Edit the text there (or the header/stack/setup data below)
and re-run:

    python3 scripts/build_svgs.py
"""
import html
import re
import urllib.parse
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

STYLE = """
<style>
  :root { --ink:#1b1b1b; --muted:#6b6b6b; --dim:#9a9a9a; --rule:#cfcfcf; --accent:#b5561a; --link:#3d59a1; }
  @media (prefers-color-scheme: dark) {
    :root { --ink:#e6e6e6; --muted:#9a9a9a; --dim:#6f6f6f; --rule:#3a3a3a; --accent:#ff9e64; --link:#7aa2f7; }
  }
  .mono { font-family: ui-monospace, "SFMono-Regular", "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }
  .ink { fill: var(--ink); } .muted { fill: var(--muted); } .dim { fill: var(--dim); } .accent { fill: var(--accent); } .link { fill: var(--link); }
  .rule { stroke: var(--rule); stroke-width: 1; }
  .draw { stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: draw 1.4s cubic-bezier(.6,0,.2,1) forwards; }
  .rise { opacity: 0; animation: rise .9s cubic-bezier(.2,.7,.2,1) forwards; }
  .fade { opacity: 0; animation: fade .7s ease forwards; }
  .blink { animation: blink 1.1s steps(1) infinite; }
  .d1 { animation-delay: .2s; } .d2 { animation-delay: .5s; } .d3 { animation-delay: .9s; }
  .d4 { animation-delay: 1.2s; } .d5 { animation-delay: 1.5s; } .d6 { animation-delay: 1.8s; }
  @keyframes draw { to { stroke-dashoffset: 0; } }
  @keyframes rise { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: none; } }
  @keyframes fade { to { opacity: 1; } }
  @keyframes blink { 50% { opacity: 0; } }
  @media (prefers-reduced-motion: reduce) {
    .draw { animation: none; stroke-dashoffset: 0; }
    .rise, .fade { animation: none; opacity: 1; }
    .blink { animation: none; }
  }
</style>
"""


def svg(width, height, title, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'role="img" aria-labelledby="t">\n<title id="t">{escape(title)}</title>\n'
        f"{STYLE}{body}</svg>\n"
    )


def text(x, y, s, size, cls="ink", extra="", anchor=None, spacing=None):
    a = f' text-anchor="{anchor}"' if anchor else ""
    ls = f' letter-spacing="{spacing}"' if spacing is not None else ""
    return f'<text x="{x}" y="{y}" font-size="{size}"{a}{ls} class="mono {cls} {extra}">{s}</text>\n'


def header():
    b = ""
    b += text(48, 44, "PROFILE — INDEX Nº 021", 11, "muted", "fade d1", spacing=3.5)
    b += text(952, 44, "URUGUAY — SOFTWARE DEVELOPER", 11, "muted", "fade d1", anchor="end", spacing=3.5)
    b += '<line x1="48" y1="58" x2="952" y2="58" class="rule draw"/>\n'
    b += text(46, 176, "German", 72, "ink", "rise d2", spacing=-2)
    b += '<g class="fade d3">'
    b += text(48, 214, "Builds LLM systems, audio plugins and developer tools.", 19, "muted").rstrip()
    b += "</g>\n"
    b += text(48, 274, "focus ▸", 12.5, "dim", "fade d4")
    b += text(128, 274, escape("LLM integration · AI automation · Rust audio DSP · spec-driven development"), 12.5, "accent", "fade d4")
    b += text(48, 300, "open to projects · freelance · collaboration", 12.5, "muted", "fade d5")
    b += '<line x1="48" y1="342" x2="952" y2="342" class="rule draw"/>\n'
    b += '<g class="fade d6">'
    b += text(48, 374, "RUST &amp; AUDIO", 11.5, "muted", spacing=3).rstrip()
    b += text(186, 374, "·", 11.5, "accent").rstrip()
    b += text(210, 374, "LLM &amp; AUTOMATION", 11.5, "muted", spacing=3).rstrip()
    b += text(388, 374, "·", 11.5, "accent").rstrip()
    b += text(412, 374, "SPEC-DRIVEN DEV", 11.5, "muted", spacing=3).rstrip()
    b += text(952, 374, "@GerMP21", 11.5, "muted", anchor="end", spacing=3).rstrip()
    b += "</g>\n"
    return svg(1000, 400, "German — software developer in Uruguay: LLM systems, audio plugins and developer tools", b)


SECTIONS = [
    ("01", "whoami"),
    ("02", "projects"),
    ("03", "how i work"),
    ("04", "coming soon"),
    ("05", "stack"),
    ("06", "setup"),
    ("07", "telemetry"),
    ("08", "contact"),
]


def section(num, name):
    b = text(48, 40, num, 13, "accent", "fade d1", spacing=2)
    b += text(80, 40, f"— {escape(name.upper())}", 13, "ink", "fade d1", spacing=4)
    b += '<line x1="48" y1="56" x2="952" y2="56" class="rule draw"/>\n'
    return svg(1000, 72, f"Section {num}: {name}", b)


STACK = [
    ("LANGUAGES", "Python · Rust · TypeScript · JavaScript · PHP · HTML · CSS"),
    ("FRONTEND", "SvelteKit · React · htmx · Tailwind CSS"),
    ("MOBILE", "React Native · Expo"),
    ("BACKEND", "FastAPI · NestJS · Express · GraphQL · REST"),
    ("DATA", "PostgreSQL · MySQL · MariaDB · MongoDB · Neo4j"),
    ("AI / ML", "Claude · Gemini · OpenAI · LangChain · LangGraph"),
    ("", "NumPy · pandas · scikit-learn · TensorFlow"),
    ("AUDIO", "Rust · nih-plug · egui · CLAP · VST3"),
    ("WORKFLOW", "OpenSpec · agent-skills · Claude Code · OpenCode"),
    ("TOOLS", "Linux · GNU · Docker · Neovim"),
]


def stack():
    top, row = 40, 34
    h = top + row * len(STACK) + 24
    b = ""
    for i, (cat, items) in enumerate(STACK):
        y = top + row * i
        delay = f"animation-delay:{0.15 + i * 0.08:.2f}s"
        b += f'<g class="fade" style="{delay}">'
        b += text(48, y, escape(cat), 11.5, "accent", spacing=3).rstrip()
        b += text(230, y, escape(items), 14, "ink").rstrip()
        b += f'<line x1="48" y1="{y + 13}" x2="952" y2="{y + 13}" class="rule"/>'
        b += "</g>\n"
    return svg(1000, h, "Technical stack", b)


SETUP = [
    ("SYSTEM", "CachyOS on a ThinkPad T480 · LUKS full-disk encryption"),
    ("DESKTOP", "niri (scrollable-tiling Wayland) + Noctalia shell · vim-style keys"),
    ("TERMINAL", "Alacritty + zsh (vi mode, starship)"),
    ("EDITORS", "Neovim (native LSP, Treesitter, Telescope) · Doom Emacs · VSCodium"),
    ("DEV", "Docker · Postman · MySQL Workbench"),
    ("MUSIC", "Ardour · VCV Rack · yabridge"),
    ("APPS", "Obsidian · LibreOffice · GIMP"),
    ("BACKUPS", "Syncthing to a second PC"),
]


def setup():
    top, row = 40, 34
    h = top + row * len(SETUP) + 24
    b = ""
    for i, (cat, items) in enumerate(SETUP):
        y = top + row * i
        delay = f"animation-delay:{0.15 + i * 0.08:.2f}s"
        b += f'<g class="fade" style="{delay}">'
        b += text(48, y, escape(cat), 11.5, "accent", spacing=3).rstrip()
        b += text(230, y, escape(items), 14, "ink").rstrip()
        b += f'<line x1="48" y1="{y + 13}" x2="952" y2="{y + 13}" class="rule"/>'
        b += "</g>\n"
    return svg(1000, h, "Setup: CachyOS, niri, Neovim and tools", b)


def footer():
    b = '<line x1="48" y1="20" x2="952" y2="20" class="rule draw"/>\n'
    b += text(48, 52, "NOW ▸", 11.5, "accent", "fade d1", spacing=3)
    b += text(130, 52, "building Omnisnap and HyperFlow · writing plugin specs · exploring PHP", 13, "ink", "fade d2")
    b += ('<text x="952" y="84" font-size="11" text-anchor="end" letter-spacing="3.5" class="mono dim fade d3">'
          'END OF FILE <tspan class="accent blink">▮</tspan></text>\n')
    return svg(1000, 100, "Now: building Omnisnap and HyperFlow, writing plugin specs, exploring PHP", b)


# ---------------------------------------------------------------- text cards
ROOT = OUT.parent
CONTENT = ROOT / "content" / "profile.md"
README = ROOT / "README.md"

BODY = 14.5          # body font size
CHAR_W = 0.602       # monospace advance width, in em (Menlo, Liberation Mono, DejaVu)
X0, X1 = 48, 952
WRAP = int((X1 - X0) / (BODY * CHAR_W)) - 3   # characters per line, with a margin
LINE = 23            # line height
INLINE = re.compile(r"\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)|`([^`]+)`")


def segments(s):
    """Split inline markup into (text, style) pieces; style is '', 'b', 'a' (link) or 'c' (code)."""
    out, pos = [], 0
    for m in INLINE.finditer(s):
        if m.start() > pos:
            out.append((s[pos:m.start()], ""))
        if m.group(1) is not None:          # **bold**, possibly containing a link
            inner = m.group(1)
            lm = re.fullmatch(r"\[([^\]]+)\]\(([^)]+)\)", inner)
            out.append((lm.group(1) if lm else inner, "ba" if lm else "b"))
        elif m.group(2) is not None:
            out.append((m.group(2), "a"))
        else:
            out.append((m.group(4), "c"))
        pos = m.end()
    if pos < len(s):
        out.append((s[pos:], ""))
    return out


def links(s):
    return re.findall(r"\[([^\]]+)\]\((https?://[^)]+)\)", s)


def plain(s):
    return "".join(t for t, _ in segments(s))


def wrap(segs, width, indent=0):
    """Word-wrap styled segments into lines of at most `width` characters."""
    words = []
    for t, st in segs:
        for w in re.split(r"(\s+)", t):
            if w:
                words.append((w, st))
    lines, cur, n = [], [], indent
    for w, st in words:
        if w.isspace():
            if cur:
                cur.append((" ", st)); n += 1
            continue
        if n + len(w) > width and cur:
            while cur and cur[-1][0] == " ":
                cur.pop()
            lines.append(cur); cur, n = [], indent
        cur.append((w, st)); n += len(w)
    while cur and cur[-1][0] == " ":
        cur.pop()
    if cur:
        lines.append(cur)
    return lines


def tspans(line):
    out = ""
    for t, st in line:
        t = escape(t)
        if st == "b":
            out += f'<tspan font-weight="700">{t}</tspan>'
        elif st == "a":                     # links: blue, bold
            out += f'<tspan class="link" font-weight="700">{t}</tspan>'
        elif st == "c":                     # code: orange highlight
            out += f'<tspan class="accent">{t}</tspan>'
        elif st == "ba":
            out += f'<tspan class="link" font-weight="700">{t}</tspan>'
        else:
            out += t
    return out


def card(blocks, title):
    """Draw a text card. blocks: list of (kind, text) with kind h3, h4, p or li."""
    y, b = 22, ""
    first = True
    for kind, t in blocks:
        if kind == "h3":
            y += 0 if first else 18
            b += text(X0, y, escape(t.upper()), 12, "accent", spacing=4)
            b += f'<line x1="{X0}" y1="{y + 12}" x2="{X1}" y2="{y + 12}" class="rule"/>\n'
            y += 38
        elif kind == "h4":
            y += 0 if first else 8
            b += text(X0, y, escape(t.upper()), 11, "dim", spacing=3.5)
            y += 26
        else:
            indent = 3 if kind == "li" else 0
            for j, line in enumerate(wrap(segments(t), WRAP, indent)):
                if kind == "li" and j == 0:
                    b += text(X0, y, "▸", BODY, "accent")
                x = X0 + indent * BODY * CHAR_W
                b += (f'<text x="{x:.1f}" y="{y}" font-size="{BODY}" class="mono ink">'
                      f"{tspans(line)}</text>\n")
                y += LINE
            y += 6 if kind == "li" else 12
        first = False
    height = y - 4
    return svg(1000, height, title, f'<g class="fade d1">\n{b}</g>\n')


def parse(md):
    """Parse content/profile.md into [(num, name, [item, ...])]."""
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    sections = []
    for part in re.split(r"(?m)^## ", md)[1:]:
        head, _, body = part.partition("\n")
        num, name = head.split(" ", 1)
        items, blocks, para = [], [], []

        def flush_para():
            if para:
                blocks.append(("p", " ".join(para))); para.clear()

        def flush_card():
            flush_para()
            if blocks:
                items.append(("card", list(blocks))); blocks.clear()

        for line in body.splitlines():
            s = line.strip()
            if not s:
                flush_para(); continue
            if re.fullmatch(r"\{\{[a-z-]+\}\}", s):
                flush_card(); items.append(("marker", s[2:-2])); continue
            if s.startswith("### "):
                flush_card(); blocks.append(("h3", s[4:])); continue
            if s.startswith("#### "):
                flush_para(); blocks.append(("h4", s[5:])); continue
            if s.startswith("- "):
                flush_para(); blocks.append(("li", s[2:])); continue
            para.append(s)
        flush_card()
        sections.append((num, name.strip(), items))
    return sections


def badge(label, url, style="flat-square", logo=None):
    q = urllib.parse.quote(label.replace("-", "--").replace("_", "__").replace(" ", "_"))
    lg = f"&amp;logo={logo}&amp;logoColor=white" if logo else ""
    return (f'<a href="{html.escape(url)}"><img src="https://img.shields.io/badge/{q}-2B2B2B?style={style}{lg}" '
            f'alt="{html.escape(label)}"></a>')


def link_row(pairs):
    seen, out = set(), []
    for label, url in pairs:
        if url not in seen:
            seen.add(url); out.append(badge(label, url))
    return '<p align="center">\n  ' + "\n  ".join(out) + "\n</p>\n" if out else ""


def img(src, alt, link=None):
    tag = f'<img src="{src}" alt="{html.escape(alt)}" width="100%">'
    return f'<a href="{html.escape(link)}">{tag}</a>' if link else tag


GRAPH = ("https://github-readme-activity-graph.vercel.app/graph?username=GerMP21&bg_color=00000000"
         "&color={c}&title_color={c}&line={l}&point={l}&area=true&area_color={l}&hide_border=true"
         "&custom_title=CONTRIBUTION%20TELEMETRY")

MARKERS = {
    "stack": img("assets/stack.svg", "Stack — " + "; ".join(f"{c or 'more'}: {v}" for c, v in STACK)),
    "setup": img("assets/setup.svg", "Setup — " + "; ".join(f"{c}: {v}" for c, v in SETUP)),
    "telemetry": (
        img("assets/stats.svg", "GitHub stats: contributions, commits, pull requests, issues, reviews, "
            "public repos, stars and top languages, updated daily") + "\n\n"
        '<p align="center">\n<picture>\n'
        f'  <source media="(prefers-color-scheme: dark)" srcset="{html.escape(GRAPH.format(c="e6e6e6", l="ff9e64"))}">\n'
        f'  <img src="{html.escape(GRAPH.format(c="1b1b1b", l="b5561a"))}" alt="Contribution activity graph for GerMP21" width="100%">\n'
        "</picture>\n</p>"),
    "contact-links": (
        '<p align="center">\n  '
        + "\n  ".join(badge(l, u, "for-the-badge") for l, u in [
            ("Synaptech Solutions", "https://synaptech-solutions.com/"),
            ("LinkedIn", "https://www.linkedin.com/in/germanmp/"),
            ("Ko-fi", "https://ko-fi.com/Z1P42ATY5F"),
            ("GitHub", "https://github.com/GerMP21")])
        + "\n</p>"),
}

HEADER_LINKS = [
    ("Synaptech Solutions", "https://synaptech-solutions.com/", None),
    ("LinkedIn", "https://www.linkedin.com/in/germanmp/", None),
    ("Ko-fi", "https://ko-fi.com/Z1P42ATY5F", "kofi"),
    ("GitHub", "https://github.com/GerMP21", "github"),
]


def as_markdown(blocks):
    """The card's text as normal Markdown, so it can be selected and its links clicked."""
    out = []
    for kind, t in blocks:
        if kind in ("h3", "h4"):
            out.append(f"**{t}**")
        elif kind == "li":
            out.append(f"- {t}")
        else:
            out.append(t)
    # keep consecutive bullets in one list
    md = ""
    for i, line in enumerate(out):
        sep = "\n" if i and line.startswith("- ") and out[i - 1].startswith("- ") else "\n\n"
        md += (sep if i else "") + line
    return md


def text_toggle(markdown):
    """A collapsed <details> holding selectable text under a card."""
    return f"<details>\n<summary><sub>show as text</sub></summary>\n\n{markdown}\n\n</details>"


MARKER_TEXT = {
    "stack": "\n".join(f"- **{c or 'More'}:** {v}" for c, v in STACK),
    "setup": "\n".join(f"- **{c.title()}:** {v}" for c, v in SETUP),
}


def build():
    files = {"header.svg": header(), "stack.svg": stack(), "setup.svg": setup(), "footer.svg": footer()}
    sections = parse(CONTENT.read_text(encoding="utf-8"))
    md = ["<!-- Generated by scripts/build_svgs.py from content/profile.md: edit that file, then re-run the script. -->",
          '<p align="center">\n  ' + img("assets/header.svg", "German — software developer in Uruguay: "
                                           "LLM systems, audio plugins and developer tools") + "\n</p>",
          '<p align="center">\n  ' + "\n  ".join(badge(l, u, logo=g) for l, u, g in HEADER_LINKS) + "\n</p>"]
    for num, name, items in sections:
        files[f"s{num}.svg"] = section(num, name)
        md.append(img(f"assets/s{num}.svg", f"{num} — {name}"))
        n = 0
        for kind, val in items:
            if kind == "marker":
                md.append(MARKERS[val])
                if val in MARKER_TEXT:
                    md.append(text_toggle(MARKER_TEXT[val]))
                continue
            groups = [[blk] for blk in val] if name == "projects" else [val]
            for blocks in groups:
                n += 1
                fname = f"card-{num}-{n:02d}.svg"
                alt = " ".join(plain(t) for _, t in blocks)
                files[fname] = card(blocks, alt)
                pairs = [l for _, t in blocks for l in links(t)]
                if name == "projects" and pairs:
                    md.append(img(f"assets/{fname}", alt, pairs[0][1]))
                else:
                    md.append(img(f"assets/{fname}", alt))
                    if pairs:
                        md.append(link_row(pairs).rstrip())
                    md.append(text_toggle(as_markdown(blocks)))
            if name == "projects":       # one toggle for all project cards
                md.append(text_toggle(as_markdown(val)))
    md.append('<p align="center">\n  ' + img("assets/footer.svg", "Now: building Omnisnap and HyperFlow, "
                                             "writing plugin specs, exploring PHP") + "\n</p>")
    return files, "\n\n".join(md) + "\n"


def main():
    OUT.mkdir(exist_ok=True)
    files, readme = build()
    for old in OUT.glob("card-*.svg"):      # drop cards that no longer exist
        if old.name not in files:
            old.unlink()
    for name, content in files.items():
        (OUT / name).write_text(content, encoding="utf-8")
    README.write_text(readme, encoding="utf-8")
    print(f"wrote {len(files)} SVGs to {OUT} and {README}")


if __name__ == "__main__":
    main()
