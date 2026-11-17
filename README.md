# Hi, I'm German 👋
I'm a software developer based in Uruguay. I like finding creative solutions to problems, and I'm always learning in a field that never stops changing.

These days I build LLM-integrated solutions and AI automation, audio plugins for music production, open source developer tools, and SaaS products for my own business. Still, part of me misses building models the old-fashioned way, by hand with TensorFlow or scikit-learn, and I'm always looking for an excuse to get back to it. Feel free to explore my repositories, open an issue or reach out if you'd like to build something together.

## :memo: How I work
[![OpenSpec](https://img.shields.io/badge/OpenSpec-2B2B2B?style=for-the-badge)](https://github.com/Fission-AI/OpenSpec)
[![agent-skills](https://img.shields.io/badge/agent--skills-2B2B2B?style=for-the-badge)](https://github.com/addyosmani/agent-skills)
[![Claude Code](https://img.shields.io/badge/Claude_Code-D97757?style=for-the-badge&logo=claudecode&logoColor=white)](https://claude.com/claude-code)
[![OpenCode](https://img.shields.io/badge/OpenCode-000000?style=for-the-badge&logo=opencode&logoColor=white)](https://opencode.ai)

Docs come first. Before I write any code I write down what I'm building and why, along with what "done" looks like, and the code has to answer to that document. The specs live in the repository next to the code, are versioned with it and get reviewed like code.

I switch between two spec-driven development tools depending on the job:

- **[OpenSpec](https://github.com/Fission-AI/OpenSpec)** when I'm changing an existing system. Every change starts as a proposal with its tasks and the spec changes it implies. Once it ships, it gets archived and merged into the main specs, so they always describe how the software behaves today.
- **[agent-skills](https://github.com/addyosmani/agent-skills)** when I want the whole path from idea to release: refining the spec, breaking it into tasks, building in small verifiable steps, testing, reviewing and shipping.

Working this way is also what makes AI coding agents useful to me. I use Claude Code and OpenCode, and an agent working from a written spec has a contract to follow, and I can review what it produces against that spec rather than against a chat history.

It's the same habit behind my audio plugins, where every design document starts with a single sentence. If you'd like to contribute to one of my projects, the specs are the best place to start.

## :construction: Coming soon

### Omnisnap
Shows exactly which elements render differently in every browser engine your users run, with one command and the browsers already installed. Instead of pixel diffs, it compares element geometry (sizes, positions, line wraps, overflow, truncation) and reports each difference at the element where it starts, not at every element it pushes down the page.

It discovers Chrome, Edge, Brave, Opera, Vivaldi, Chromium, Firefox, Safari and WebKitGTK and drives them over CDP, WebDriver BiDi or WebDriver Classic, running branded browsers as shipped. Every finding comes with a cause: it neutralizes the suspects and measures the page again, and a third engine settles which one is wrong. Results go to a self-contained local report, or to one pull request comment from a report-only GitHub Action on Ubuntu, Windows and macOS.

The prototype found 24/24 planted bugs at the right element, with no false reports on bug-free pages across five engines.

**Status:** design and prototype; v1 is specified in 17 module specs. **License:** Apache 2.0.

### HyperFlow
An [OpenCode](https://opencode.ai/) plugin that runs the development lifecycle, from product spec to release, as a state machine with quality gates. The LLM orchestrates and deterministic TypeScript tools do the work: a PRD is atomized into specs, questions and decisions with traceable IDs, planning waits until every question is resolved, and a phase kernel refuses illegal transitions.

Implementation is test-first, repairs stop after three attempts, and shipping requires lint, typecheck, tests, coverage, security scanning, fuzzing and ablation checks that prove the tests catch regressions.

The full version (v1.0), already specified, adds regression-first bugfix and behavior-preserving refactor workflows, versioned re-planning, test tool selection across 14 language ecosystems, drift detection, and generated CI and release checklists. Parallel tasks, browser automation and multi-repo support are planned for v1.0. It won't install, delete, migrate, commit or deploy anything without your approval.

**Status:** v0.1.0 MVP: 11 agents, 21 commands, 16 skills and 37 tools, all implemented, with 113 tests passing. **License:** MIT.

### Context-to-Decision
An open source system that turns messy operational data into a decision loop. It ingests and normalizes data, defines metrics and the drivers behind them, generates briefings, tracks decisions and compares them with outcomes over time. The idea: every objective needs a metric, every metric needs drivers, every driver needs data, and every decision should leave a trace. Built with Python, FastAPI, PostgreSQL and Docker Compose.

## :toolbox: Tools I use

### Programming languages
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-663399?style=for-the-badge&logo=css&logoColor=white)

- **Python** is the language I know best. I've used it professionally, and it's the home of my favorite area: machine learning.
- **Rust** is the one that excites me most right now. The borrow checker makes code safer and opens the door to systems programming and faster games.
- **JavaScript and TypeScript** came with two years of focused web development after my bachelor's degree. I pick up new frameworks and libraries quickly.

### Frontend
![SvelteKit](https://img.shields.io/badge/SvelteKit-FF3E00?style=for-the-badge&logo=svelte&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![htmx](https://img.shields.io/badge/htmx-3366CC?style=for-the-badge&logo=htmx&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)

SvelteKit is my first choice for server-rendered apps because of its developer experience. I build single-page apps with React, use htmx for server-driven interactivity, and style everything quickly with Tailwind CSS.

### Mobile
![React Native](https://img.shields.io/badge/React_Native-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Expo](https://img.shields.io/badge/Expo-1C2024?style=for-the-badge&logo=expo&logoColor=white)

I build cross-platform mobile apps with React Native and Expo.

### Backend
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white)
![NestJS](https://img.shields.io/badge/NestJS-E0234E?style=for-the-badge&logo=nestjs&logoColor=white)
![GraphQL](https://img.shields.io/badge/GraphQL-E10098?style=for-the-badge&logo=graphql&logoColor=white)

I build REST and GraphQL APIs, including authentication and authorization. Building GraphQL APIs with NestJS is the part I enjoy most.

### Databases
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=mariadb&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=for-the-badge&logo=neo4j&logoColor=white)

I studied SQL and relational database design in depth during my degree, which is why PostgreSQL is my default. I've used MongoDB at work, and graph databases like Neo4j interest me for data science and social applications.

### AI and machine learning
![Claude](https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=claude&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlegemini&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langgraph&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)

I build LLM-powered applications with Claude and Gemini, using LangChain and LangGraph to orchestrate agents and workflows. Deep learning is still what I enjoy most: stacking layers and watching the loss drop epoch after epoch never gets old.

### Audio plugins
![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
![nih-plug](https://img.shields.io/badge/nih--plug-2B2B2B?style=for-the-badge)
![egui](https://img.shields.io/badge/egui-2B2B2B?style=for-the-badge)
![CLAP](https://img.shields.io/badge/CLAP-2B2B2B?style=for-the-badge)
![VST3](https://img.shields.io/badge/VST3-2B2B2B?style=for-the-badge)

I write audio plugins for music production in Rust, using nih-plug for the DSP and plugin plumbing and egui for the interface, and ship them as CLAP and VST3.

Each plugin begins as one sentence about what it does. That sentence stays at the top of the design document, and I build out from it, adding features as I see fit. When a feature doesn't fit the sentence, it goes to a different plugin.

I like controls that mean something physical. [Corrosion](https://github.com/GerMP21/Corrosion-VST) asks how big the pipe is and how rusted. Once you know what a knob does to the object, you can stop reading the manual.

There are no mode menus. Each plugin is one continuum, with the familiar sound as the default and the strange stuff a few turns away.

Before anything is released, it passes automated tests, real-time safety checks (the audio thread never allocates memory) and the standard plugin validators. That doesn't make it bug-free, but it does catch the obvious crashes before you do. And Rust, of course, catches plenty more.

Everything is free software under GPLv3. If you [buy a build on Ko-fi](https://ko-fi.com/Z1P42ATY5F), you're funding the next plugin and getting builds you can install straight away.

### Development tools
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![GNU](https://img.shields.io/badge/GNU-A42E2B?style=for-the-badge&logo=gnu&logoColor=white)
![Neovim](https://img.shields.io/badge/Neovim-57A143?style=for-the-badge&logo=neovim&logoColor=white)

Linux is my main development environment. I'm at home on the command line with tools like `tar`, `rsync`, `grep`, `sed`, `gawk`, `xargs`, `parallel` and `screen`. My editor is Neovim, for its speed and extensibility.

### Other tools
![Obsidian](https://img.shields.io/badge/Obsidian-7C3AED?style=for-the-badge&logo=obsidian&logoColor=white)
![LibreOffice](https://img.shields.io/badge/LibreOffice-18A303?style=for-the-badge&logo=libreoffice&logoColor=white)
![GIMP](https://img.shields.io/badge/GIMP-5C5543?style=for-the-badge&logo=gimp&logoColor=white)
![Ardour](https://img.shields.io/badge/Ardour-C61C3E?style=for-the-badge&logo=ardour&logoColor=white)

## :mailbox_with_mail: Get in touch
[![Synaptech Solutions](https://img.shields.io/badge/Synaptech_Solutions-A84D08?style=for-the-badge)](https://synaptech-solutions.com/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge)](https://www.linkedin.com/in/germanmartinez21/)
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/Z1P42ATY5F)

Have a project that needs another developer? Feel free to reach out.
