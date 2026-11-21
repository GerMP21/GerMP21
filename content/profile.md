<!--
Text of the profile README. Edit here, then run:  python3 scripts/build_svgs.py
That redraws every card in assets/ and rewrites README.md.

Format: "## NN name" starts a numbered section. Inside a section:
"### Title" starts a new card, "- " is a bullet, blank lines separate
paragraphs, and **bold**, [links](https://...) and `code` work as usual.
Markers on their own line: {{stack}}, {{setup}}, {{telemetry}}, {{contact-links}}.
In "projects", every bullet becomes its own card linking to the bullet's first link.
-->

## 01 whoami
**Hi, I'm German 👋**

I'm a software developer based in Uruguay. I like finding creative solutions to problems, and I'm always learning in a field that never stops changing.

These days I build LLM-integrated solutions and AI automation, audio plugins for music production, open source developer tools, and SaaS products for my own business. Still, part of me misses building models the old-fashioned way, by hand with TensorFlow or scikit-learn, and I'm always looking for an excuse to get back to it. Feel free to explore my repositories, open an issue or reach out if you'd like to build something together.

## 02 projects
- **[Corrosion](https://github.com/GerMP21/Corrosion-VST)** (Rust, VST3 + CLAP): an industrial physical-modeling instrument. Bowed, struck, scraped and blown pipes, plates, chains and cables, followed by drive, body, space and a diode clipper.
- **[Omnisnap](https://github.com/GerMP21/Omnisnap)** (Go, AGPL v3): shows which elements render differently in every browser engine your users run, with one command and the browsers already installed. It compares element geometry instead of pixels, reports each difference at the element where it starts, and writes a self-contained report; it also runs as a GitHub Action and from npm or PyPI. Release candidate v0.1.0-rc.5.
- **[mysql-split-import](https://github.com/GerMP21/mysql-split-import)** (Python): imports multi-gigabyte mysqldump files in resumable, per-table transactions, so a dropped connection costs one part instead of the whole night. Standard library only.
- **[DGI RUC proxy](https://github.com/GerMP21/DGI-WS_PersonaGetActEmpresarial-Proxy-Client)** (Node.js, Express): a JSON REST API for Uruguay's DGI taxpayer (RUC) web service. It handles the SOAP envelopes, WS-Security signing and XML-in-CDATA parsing behind bearer-token authentication.
- **[dotfiles](https://github.com/GerMP21/dotfiles)** (Shell): my CachyOS + niri desktop, with scripts that install, link, set up and verify the whole system.

## 03 how i work
Docs come first. Before I write any code I write down what I'm building and why, along with what "done" looks like, and the code has to answer to that document. The specs live in the repository next to the code, are versioned with it and get reviewed like code.

I switch between two spec-driven development tools depending on the job:

- **[OpenSpec](https://github.com/Fission-AI/OpenSpec)** when I'm changing an existing system. Every change starts as a proposal with its tasks and the spec changes it implies. Once it ships, it gets archived and merged into the main specs, so they always describe how the software behaves today.
- **[agent-skills](https://github.com/addyosmani/agent-skills)** when I want the whole path from idea to release: refining the spec, breaking it into tasks, building in small verifiable steps, testing, reviewing and shipping.

Working this way is also what makes AI coding agents useful to me. I use [Claude Code](https://claude.com/claude-code) and [OpenCode](https://opencode.ai). An agent working from a written spec has a contract to follow, and I can review what it produces against that spec rather than against a chat history.

It's the same habit behind my audio plugins, where every design document starts with a single sentence. If you'd like to contribute to one of my projects, the specs are the best place to start.

## 04 coming soon
### HyperFlow
An [OpenCode](https://opencode.ai/) plugin that runs development from product spec to release as a state machine with quality gates. The LLM orchestrates while deterministic TypeScript tools do the work: planning waits until every open question is resolved, implementation is test-first, and shipping requires lint, tests, coverage, security scanning and fuzzing. It won't install, delete, commit or deploy anything without your approval.

**Status:** v0.1.0 MVP: 11 agents, 21 commands, 16 skills and 37 tools, with 113 tests passing. **License:** MIT.

## 05 stack
{{stack}}

### Programming languages

- **Python** is the language I know best. I've used it professionally, and it's the home of my favorite area: machine learning.
- **Rust** is the one that excites me most right now. It's as fast as C, and its borrow checker makes code safer, which opens the door to systems programming and games.
- **JavaScript and TypeScript** came with two years of focused web development after my bachelor's degree. I pick up new frameworks and libraries quickly.
- **PHP** is the newest addition: I'm exploring it at the moment.

### Frontend

htmx is my first choice. I love low-JS development: the server renders HTML, and htmx adds just the interactivity a page needs, with no build step and no client-side state to keep in sync. When a project really calls for a JavaScript framework, I reach for SvelteKit for its developer experience, or React for single-page apps. Tailwind CSS keeps the styling quick either way.

### Mobile

I build cross-platform mobile apps with React Native and Expo.

### Backend

I build REST and GraphQL APIs, including authentication and authorization, with Zitadel as my identity provider. Building GraphQL APIs with NestJS is the part I enjoy most.

### Databases

I studied SQL and relational database design in depth during my degree, which is why PostgreSQL is my default. I've used MongoDB at work, and graph databases like Neo4j interest me for data science and social applications.

### Scraping

Scraping was my first job, and I still love it. I use Scrapy for large crawls, Playwright and Selenium when a site needs a real browser, Patchright when it actively fights automation, and Browser Use when an AI agent has to find its own way through a site.

### AI and machine learning

I build LLM-powered applications with Claude, Gemini and OpenAI models, using LangChain and LangGraph to orchestrate agents and workflows. Deep learning is still what I enjoy most: stacking layers and watching the loss drop epoch after epoch never gets old.

### Audio plugins

I write audio plugins for music production in Rust, using nih-plug for the DSP and plugin plumbing and egui for the interface, and ship them as CLAP and VST3.

Each plugin begins as one sentence about what it does. That sentence stays at the top of the design document, and I build out from it, adding features as I see fit. When a feature doesn't fit the sentence, it goes to a different plugin.

I like controls that mean something physical. [Corrosion](https://corrosion-vst.org/) asks how big the pipe is and how rusted. Once you know what a knob does to the object, you can stop reading the manual.

There are no mode menus. Each plugin is one continuum, with the familiar sound as the default and the strange stuff a few turns away.

Before anything is released, it passes automated tests, real-time safety checks (the audio thread never allocates memory) and the standard plugin validators. That doesn't make it bug-free, but it does catch the obvious crashes before you do. And Rust, of course, catches plenty more.

Everything is free software under GPLv3. If you [buy a build on Ko-fi](https://ko-fi.com/Z1P42ATY5F), you're funding the next plugin and getting builds you can install straight away.

#### In development
These are at the concept stage: each has a PRD and a DSP spec, and each has to pass an offline Python prototype before any Rust gets written.

- **Orrery**: a reverb made of sound sources orbiting the listener, or a rotary speaker with forty rotors. Radius sets how far each source travels, in meters (0.30 m is a Leslie horn). Coherence sets how the orbits line up: locked pairs are a rotary speaker, evenly spread is a string ensemble, scattered is a granular cloud. Drift spreads their speeds across just intervals, from unison to a chord. Because the reverb tail is made of the same orbiting copies, the space itself rotates.
- **Sideband**: a ring modulator whose carrier follows the note you play. Ratio sets the carrier relative to that note: at simple ratios the sidebands land on just intervals, so a single note becomes a power chord or a triad; at 1 it's an octave fuzz; off the grid it's a bell. Density morphs the carrier from a sine to an impulse train, ending in a sample-rate crusher that tracks the note. Purity moves it between harmonizer and clangorous ring mod. Out of the box it's an octave fuzz.
- **Undertow**: an envelope-driven phaser and resonant filter on one modulation bus, with bipolar depth, so the filter can sweep up while the phaser sweeps down from the same note. Its flagship routing, Vortex, puts the phaser inside the filter's resonance loop, giving one filter several moving resonant peaks.

## 06 setup
{{setup}}

**CachyOS** on a **ThinkPad T480**, fully encrypted (LUKS), running the scrollable-tiling Wayland compositor **[niri](https://github.com/niri-wm/niri)** with the [Noctalia](https://docs.noctalia.dev) shell, keyboard-driven with vim-style keys. Configs and setup scripts are in my [dotfiles](https://github.com/GerMP21/dotfiles).

Linux is my main development environment, and I'm at home on the command line with tools like `tar`, `rsync`, `grep`, `sed`, `gawk`, `xargs`, `parallel` and `screen`. I use Neovim for its speed and extensibility, and Docker to run services and keep environments reproducible.

## 07 telemetry
{{telemetry}}

## 08 contact
Have a project that needs another developer? Feel free to reach out.

{{contact-links}}
