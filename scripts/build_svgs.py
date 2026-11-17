#!/usr/bin/env python3
"""Generate the profile's SVG assets into ../assets.

Every SVG adapts to GitHub's light and dark themes with a
prefers-color-scheme media query, uses the system monospace font, and
respects prefers-reduced-motion. Edit the text below and re-run:

    python3 scripts/build_svgs.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"

STYLE = """
<style>
  :root { --ink:#1b1b1b; --muted:#6b6b6b; --dim:#9a9a9a; --rule:#cfcfcf; --accent:#3d59a1; }
  @media (prefers-color-scheme: dark) {
    :root { --ink:#e6e6e6; --muted:#9a9a9a; --dim:#6f6f6f; --rule:#3a3a3a; --accent:#7aa2f7; }
  }
  .mono { font-family: ui-monospace, "SFMono-Regular", "SF Mono", Menlo, Consolas, "Liberation Mono", monospace; }
  .ink { fill: var(--ink); } .muted { fill: var(--muted); } .dim { fill: var(--dim); } .accent { fill: var(--accent); }
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


def main():
    OUT.mkdir(exist_ok=True)
    files = {"header.svg": header(), "stack.svg": stack(), "setup.svg": setup(), "footer.svg": footer()}
    for num, name in SECTIONS:
        files[f"s{num}.svg"] = section(num, name)
    for name, content in files.items():
        (OUT / name).write_text(content, encoding="utf-8")
        print("wrote", OUT / name)


if __name__ == "__main__":
    main()
