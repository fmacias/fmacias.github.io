# AGENTS.md
## Role
You could act as a senior software architect and technical writer, as a front-end engineer or as a UX specialist.

You are maintaining documentation that must work correctly in:
- Obsidian (editing + knowledge navigation)
- MkDocs (static site generation)

If is it required a task to create, refactor, and validate Markdown files following strict best practices.

## Context

You are working in the `fmacias.github.io` repository, which hosts the public website and documentation hub for Fernando Macías.

This repository is intended to power a **static, content-first, mobile-first website** generated with **MkDocs**, preferably using **Material for MkDocs**, and deployed to **GitHub Pages**.

The website has these primary purposes:

1. Present Fernando Macías as a senior freelance software developer.
2. Offer a concise and credible professional public profile.
3. Showcase selected repositories under the `fmacias` GitHub account, especially `TplQueue`.
4. Publish curated technical documentation in Markdown.
5. Provide a clear contact path for clients, collaborators, and employers.

This repository is **not** intended to become a heavy frontend application, a JavaScript-dependent SPA, or a visually overloaded marketing site.

The website must remain:

- static-first
- Markdown-first
- mobile-first
- accessible by default
- lightweight
- maintainable
- professional
- technically credible


---

## Core priorities

When making design, implementation, structure, or content decisions, apply these priorities in this order:

1. Accessibility
2. Clarity and usability
3. Performance
4. Mobile-first responsiveness
5. Broad browser/device support
6. Maintainability
7. Content quality
8. Visual polish

If there is tension between aesthetics and usability, usability wins.

If there is tension between novelty and robustness, robustness wins.

If there is tension between customization and maintainability, maintainability wins.

---

## Product philosophy

This website must behave like a **professional technical presence**, not like a trend-driven landing page.

The desired result is:

- easy to scan
- fast to load
- easy to navigate
- readable on phones first
- friendly to assistive technologies
- conservative in dependencies
- simple to evolve over time
- trustworthy in tone and structure

Do not optimize for visual novelty.
Optimize for trust, clarity, resilience, and low friction.

---

## Mandatory design principles

### 1. Mobile-first

All layouts and page flows must be designed for narrow screens first.

Assume the default user context may include:

- small screen
- touch input
- low or unstable bandwidth
- limited CPU and memory
- interrupted attention
- one-handed use

Desktop is an enhancement layer, not the baseline design assumption.

Rules:

- prioritize narrow-width readability first
- keep above-the-fold mobile content meaningful
- ensure primary actions remain visible and easy to reach
- avoid large hero sections that bury useful content
- avoid layouts that depend on hover
- avoid desktop-only assumptions

### 2. Accessibility by default

Accessibility is mandatory, not optional polish.

All changes must aim to satisfy **WCAG 2.2 AA in practice**.

Minimum accessibility expectations:

- semantic HTML structure
- logical heading hierarchy
- one `h1` per page
- keyboard-accessible interactive elements
- visible focus states
- sufficient color contrast
- descriptive links
- accessible forms with explicit labels
- meaningful alt text for informative images
- empty alt text for decorative images
- no information conveyed by color alone
- no keyboard traps
- no inaccessible custom widgets where native HTML is sufficient
- content remains usable at zoom
- touch targets are comfortably tappable
- motion is restrained and never required to understand content

Prefer native, semantic HTML over custom behavior.

Examples:
- prefer `button` over clickable `div`
- prefer `nav`, `main`, `header`, `footer`, `section`, `article` over anonymous wrappers
- prefer explicit labels over placeholder-only inputs
- prefer simple lists and headings over visually clever but semantically poor structures

If a custom design choice weakens accessibility, reject it.

### 3. Ergonomics and cognitive load

The website must be easy to understand quickly.

Every page should help users answer:

- Where am I?
- What is this page about?
- What can I do next?
- Where do I go from here?

Rules:

- use short paragraphs
- use strong headings and subheadings
- use concise labels
- reduce visual clutter
- reduce navigation complexity
- present only the most useful options
- keep call-to-action patterns clear and restrained
- maintain consistent spacing and hierarchy
- prefer scanning over reading walls of text

Avoid:

- decorative complexity
- oversized intros
- vague labels like “More”, “Other”, “Stuff”, “Various”
- long dense paragraphs on landing pages
- mixed visual metaphors
- unpredictable navigation behavior

### 4. Performance as a UX requirement

Performance is part of usability and must be treated as a first-class requirement.

All implementations must favor good practical behavior regarding:

- fast initial rendering
- low JavaScript cost
- low layout shift
- low asset weight
- low memory usage
- reduced dependency overhead

Rules:

- keep JavaScript minimal
- introduce JavaScript only when it adds clear value
- avoid large third-party libraries
- avoid unnecessary CSS overrides
- optimize images before adding them
- avoid background video
- avoid auto-playing media
- avoid heavy animation
- avoid unnecessary web fonts
- prefer system fonts or restrained font loading
- avoid DOM-heavy structures for simple content
- avoid features that significantly degrade low-end devices

Treat every added dependency as a cost.

### 5. Progressive enhancement and universality

The baseline experience must remain usable without relying on advanced or fragile browser behavior.

Rules:

- core navigation must work without JavaScript
- important content must not depend on animation
- essential actions must not depend on hover
- the site must degrade gracefully
- prefer widely supported platform features
- prefer stable web standards over trendy techniques
- test mentally for slower devices and modest browsers

Do not build the site in a way that assumes:
- perfect hardware
- perfect bandwidth
- perfect vision
- mouse precision
- large viewport
- latest high-end browser features for essential behavior

---

## Mandatory implementation philosophy

### Static-first

This repository must remain a static website repository.

Do not introduce server-side assumptions.

Do not architect features as if this were a full-stack application unless explicitly requested.

### Markdown-first

If a page can be implemented clearly in Markdown, use Markdown.

Prefer Markdown content over custom HTML when the theme already supports the required structure well.

Introduce custom HTML only when there is a clear, justified UX need.

### Theme-first, customization-second

Assume **Material for MkDocs** is the default presentation layer.

Prefer using theme capabilities before introducing overrides.

Prefer:
- standard navigation
- standard search
- standard admonitions
- standard tabs
- standard content components

Avoid replacing working theme behavior with custom widgets unless there is a demonstrated usability benefit.

### Simplicity-first

Use the simplest implementation that fully satisfies the requirement.

Do not add engineering complexity to solve a design problem that can be solved with content structure, spacing, hierarchy, or standard theme features.

---

## Repository and structure rules

Single-language reference structure:

```text
.
├─ mkdocs.yml
├─ docs/
│  ├─ index.md
│  ├─ services.md
│  ├─ tplqueue.md
│  ├─ profile.md
│  ├─ contact.md
│  ├─ assets/
│  │  ├─ images/
│  │  ├─ files/
│  │  ├─ stylesheets/
│  │  └─ javascripts/
│  └─ technical/
│     ├─ overview.md
│     ├─ architecture.md
│     └─ getting-started.md
└─ .github/ 
```

Rules:

- keep top-level structure small and predictable
- group documentation logically
- avoid deep nesting unless documentation volume requires it
- keep public-facing pages distinct from deep technical documentation
- avoid orphan pages
- avoid duplicate content across pages
- in the multilingual site, prefer language-specific landing pages at `docs/en/index.md` and `docs/de/index.md` over legacy `home.md` duplicates

Multilingual structure supplement:

```text
.
|-- mkdocs.yml
|-- docs/
|   |-- en/
|   |   |-- index.md
|   |   |-- services.md
|   |   |-- tplqueue.md
|   |   |-- profile.md
|   |   |-- contact.md
|   |   `-- technical/
|   |       |-- overview.md
|   |       |-- architecture.md
|   |       `-- getting-started.md
|   |-- de/
|   |   |-- index.md
|   |   |-- services.md
|   |   |-- tplqueue.md
|   |   |-- profile.md
|   |   |-- contact.md
|   |   `-- technical/
|   |       |-- overview.md
|   |       |-- architecture.md
|   |       `-- getting-started.md
|   |-- es/
|   |   |-- index.md
|   |   |-- services.md
|   |   |-- tplqueue.md
|   |   |-- profile.md
|   |   |-- contact.md
|   |   `-- technical/
|   |       |-- overview.md
|   |       |-- architecture.md
|   |       `-- getting-started.md
|   `-- assets/
|       |-- images/
|       |-- files/
|       |-- stylesheets/
|       `-- javascripts/
|-- overrides/
|-- scripts/
`-- .github/
```

The current public site follows the multilingual structure below, with language-specific landing pages in `docs/en/index.md` and `docs/de/index.md`.

Additional structure rules:

- keep the same relative page paths across language trees whenever possible
- treat `docs/en/`, `docs/de/`, and later `docs/es/` as parallel content trees, not unrelated page sets
- do not publish multilingual content by mixing English and German inside one Markdown document
- keep language-independent assets under shared `docs/assets/` unless a language-specific asset is truly required
- prefer one multilingual MkDocs build over separate disconnected builds when localized navigation must work in one served site


---

## Information architecture rules

The website should generally remain small and focused.

Preferred top-level navigation:

- Services
- TplQueue
- Documentation
- Profile / About
- Contact

A localized landing page may exist at `/` and `/de/` without a visible `Home` navigation item.

Changes to navigation must improve discoverability or user flow.

Do not add navigation items casually.

Do not create deep menu trees without a real information architecture need.

Do not bury important pages under vague parent sections.

---

## Language and localization rules

The site must support English and German as first-class published languages.

Spanish may be added later using the same structure.

Rules:

- English is the default fallback language
- English content lives in `docs/en/`
- German content lives in `docs/de/`
- Spanish content, when added, must live in `docs/es/`
- do not mix multiple languages in the same Markdown page
- do not maintain one page that contains English and German sections hidden with JavaScript or CSS
- keep equivalent pages aligned by relative path, for example `/services/` and `/de/services/`
- keep the main navigation structure aligned across languages unless a real content difference justifies divergence
- language switching must remain explicit and visible to users
- direct links to a specific language page must remain on that language page

Preferred behavior:

- English is the default built language at `/`
- German is built at `/de/`
- Spanish, when added, should be built at `/es/`
- the root path `/` may use a very small JavaScript redirect, but the landing content should live in `docs/<lang>/index.md`
- if a saved language preference exists, use it first when that language is available
- otherwise, if the browser language starts with `de`, route to `/de/`
- otherwise stay on the English root `/`
- do not auto-redirect users between languages after they are already inside a language-specific page

Accessibility and maintainability rules:

- the baseline site must remain usable without JavaScript
- JavaScript may assist with the root redirect and language preference persistence only
- core navigation and content access must not depend on JavaScript
- every language page must remain readable as standalone Markdown

---

## Homepage rules

The homepage must be a concise synthesis, not a full CV.

It must quickly communicate:

- who Fernando Macías is
- what he offers
- what technical domains he focuses on
- what type of freelance work he is open to
- where visitors can learn more
- how to contact him

Homepage content should be optimized for quick scanning on mobile.

Above the fold on mobile, the user should understand the professional positioning without needing to scroll through decorative material.

Do not overload the homepage with excessive biography, full technical history, or repository-level details.

---

## Content rules

<b>Tone</b>

The tone must be:

- professional
- concise
- credible
- calm
- technically precise
- business-friendly

Avoid:

- hype
- exaggerated marketing claims
- vague buzzwords
- empty superlatives
- filler text
- overlong self-description

---

## Positioning

The site should present Fernando Macías as:

- a senior software developer
!- strongly focused on .NET / C# and also profesionally skilled with Java/JavaSpring, Javascript, Bash and Powshell scripting and skilled to get fast involved profesinollay to work within embeded systems 
- capable on frontend as well
- experienced in industrial and integration-heavy contexts
- especially relevant for MES / MOS / manufacturing / equipment integration / data acquisition domains
- open to adjacent freelance technical opportunities

## Public documentation curation

Documentation on the public website must be curated.

Do not copy large volumes of raw internal repo material into the site without filtering.

Only publish documentation that is useful to public readers, such as:

- project overview
- architecture summaries
- selected design explanations
- getting started guidance
- selected implementation rationale
- links to source repositories

Public docs must be understandable without requiring private context.

---

## Readability

All pages must be readable both:

- as rendered pages
- and as raw Markdown

Use:

- clear headings
- short sections
- bullet lists when useful
- code fences where relevant
- direct linking
- restrained cross-linking

Avoid over-embedding content or turning one page into an unstructured dump.

---

## Accessibility rules for contributors

All contributions must satisfy these rules:

- Exactly one h1 per page.
- Logical heading progression.
- Landmarks must be clear.
- Links must be descriptive out of context.
- Interactive controls must be keyboard usable.
- Focus must remain visible.
- Forms must have labels.
- Validation states must be explicit and understandable.
- Color must not be the only differentiator.
- Informative images need useful alt text.
- Decorative images must use empty alt text.
- Tables must only be used for real tabular data.
- Content must remain usable at increased zoom.
- Motion must never be required to understand the interface.
- Touch targets must be reasonably sized for mobile.

Never introduce inaccessible custom controls when native controls solve the problem.

## Responsive design rules

- Design from the smallest viewport upward.
- Prefer fluid layouts before adding breakpoints.
- Add breakpoints only when content actually needs them.
- Prefer reflow over hiding important content.
- Avoid horizontal scrolling except where truly unavoidable.
- Ensure code blocks are usable on narrow screens.
- Ensure tables degrade acceptably on mobile.
- Keep spacing proportional and restrained on mobile.
- Keep important text visible without requiring excessive scroll.
- Avoid giant empty spaces on large screens.

---

## Visual design rules

The visual language should communicate:

- technical maturity
- professionalism
- clarity
- restraint
- reliability

Prefer:

- clean typography
- moderate whitespace
- stable hierarchy
- restrained accent colors
- predictable component usage
- clean section divisions
- simple iconography only when it adds clarity

Avoid:

- neon-heavy palettes
- decorative clutter
- large shadow-heavy compositions
- unnecessary gradients
- trend-driven animation
- overly playful patterns
- fake complexity
- oversized cards for simple text

Visual polish must support comprehension, not compete with it.

---

## JavaScript rules

JavaScript is allowed, but only when justified.

Default assumption: no custom JavaScript unless clearly needed.

Allowed use cases may include:

- small progressive enhancements
- light interaction improvements
- analytics only if explicitly approved
- carefully implemented contact form behavior if introduced

Rules:

- JavaScript must not be required for basic navigation
- JavaScript must not block access to content
- avoid framework-level client-side architecture
- avoid large script dependencies
- avoid duplicate behavior already provided by the theme
- avoid client-side complexity for static content
- do not use JavaScript to hide one language and reveal another inside the same Markdown page
- if language detection is implemented, keep it limited to the root landing behavior and preference persistence
- do not redirect a user away from a deep-linked language page just because the browser prefers another language

If a feature can be implemented well without JavaScript, do not add JavaScript.

---

## CSS customization rules

Custom CSS must remain minimal, purposeful, and maintainable.

Prefer:

- theme configuration first
- small overrides second
- scoped changes
- readability improvements
- spacing and hierarchy adjustments
- restrained branding adjustments

Avoid:

- large custom CSS layers
- fighting the theme
- brittle selector chains
- unnecessary visual divergence from the theme
- pixel-perfect hacks
- custom layouts that become fragile on small screens

If a CSS customization increases long-term maintenance cost without clear UX value, reject it.

---

## Images, media, and assets rules

Rules:

- every asset must justify its presence
- optimize images before committing
- prefer SVG for simple diagrams/icons when appropriate
- avoid oversized screenshots
- avoid decorative media that slows page load
- avoid autoplay media
- provide alt text where needed
- keep downloadable files organized and clearly named

Do not add media just to make the page look fuller.

---

## Forms and contact rules

If a contact form is introduced:

- Keep fields minimal.
- Every field must have a clear purpose.
- Labels must always be visible.
- Validation must be explicit and accessible.
- Error states must be understandable.
- Mobile ergonomics must be preserved.
- Anti-spam must not destroy usability.
- Third-party integrations must be justified and reviewed for reliability and privacy impact.

Prefer no contact form over a poor contact form.

A plain email/contact page is acceptable if it creates less friction and lower maintenance burden.

---

## SEO and metadata rules

Apply basic SEO hygiene without harming clarity.

Ensure:

- meaningful page titles
- useful meta descriptions when configured
- descriptive headings
- human-readable navigation labels
- meaningful internal linking
- clean page naming

Do not introduce keyword stuffing or SEO gimmicks.

---

# Security and repository hygiene rules

If automation or deployment files are added:

- do not commit secrets
- do not place API keys in repository files
- use GitHub secrets only when necessary
- keep workflows minimal
- prefer official or trusted actions
- do not add unnecessary deployment complexity

Public configuration is acceptable.
Public secrets are never acceptable.

---

## MkDocs-specific rules

Assume the site is maintained with MkDocs.

Rules:

- keep mkdocs.yml clear and readable
- prefer one MkDocs configuration for the multilingual site when the chosen plugin cleanly supports it
- prefer simple navigation structure
- keep Markdown files organized under docs/
- keep language content under `docs/<lang>/`
- use theme features before adding custom behavior
- do not overcomplicate the build model
- keep deployment compatible with GitHub Pages
- avoid plugin sprawl
- prefer Material for MkDocs language and alternate-link capabilities over custom multilingual workarounds
- a multilingual plugin is acceptable when it is the simplest way to build and serve the whole localized site coherently
- if a root redirect page is added, keep it outside the core content model and keep its behavior minimal and predictable

Before adding a plugin, justify:

- why the feature is needed
- why the theme cannot already satisfy it
- the maintenance impact
- the performance impact
- the accessibility impact

---

## Decision rules for Codex

When several approaches are possible, choose the one that is:

- more accessible
- more mobile-friendly
- simpler
- lighter
- more robust across browsers/devices
- easier to maintain
- more consistent with Markdown-first static publishing
- more aligned with professional UX expectations

Do not optimize for novelty.
Do not optimize for cleverness.
Optimize for clarity, reliability, maintainability, and user trust.

---

## Forbidden patterns unless explicitly requested

Do not introduce any of the following by default:

- SPA-style architecture
- frontend frameworks for mostly static pages
- dependency-heavy UI systems
- complex animation systems
- custom navigation replacing theme navigation
- inaccessible custom controls
- decorative hero sections that bury key information
- large unoptimized images
- hover-only essential interactions
- auto-playing media
- excessive CSS overrides
- large JavaScript bundles
- arbitrary plugin accumulation
- duplicated content across multiple pages
- content written as generic marketing filler

---

## Review checklist before proposing changes

Before suggesting or committing any change, verify all of the following.

### Accessibility
- Is the structure semantic?
- Is the heading hierarchy correct?
- Is the page keyboard-usable?
- Are focus states visible?
- Are links descriptive?
- Are forms labeled?
- Are contrast and readability acceptable?

### UX
- Is the purpose of the page obvious?
- Is the content easy to scan?
- Is the next step clear?
- Has unnecessary friction been removed?
- Is the mobile view still the main design reference?

### Performance
- Is the change lightweight?
- Does it avoid unnecessary dependencies?
- Is asset weight reasonable?
- Does it preserve a fast baseline experience?

### Responsiveness
- Does it work well on narrow screens first?
- Does it avoid horizontal overflow?
- Do code blocks and tables remain usable?
- Is spacing still coherent on small screens?

### Maintainability
- Is the solution simple?
- Is it consistent with the rest of the site?
- Is the customization justified?
- Could a future maintainer understand and extend it easily?

### Content quality
- Is the wording concise?
- Is the tone credible and professional?
- Does the page avoid empty filler?
- Is the content relevant to public readers?

---

## Preferred outcome

The ideal website should feel like:

- a concise professional profile
- a curated technical documentation hub
- a lightweight static site
- a mobile-friendly experience
- an accessible and ergonomic interface
- a maintainable long-term public presence

The ideal contribution is one that improves the site while keeping it:
simple, fast, accessible, readable, and credible. t


# Core Principles regarding changes into markdown files

## 1. Separation of Concerns (MANDATORY)

- Markdown files MUST contain:
  - structure
  - semantics
  - content

- Markdown files MUST NOT contain:
  - inline CSS
  - <style> blocks
  - complex HTML layout
  - presentation logic

- Styling MUST be handled via:
  - MkDocs: `extra.css`
  - Obsidian: `.obsidian/snippets/*.css`
---

## 2. Markdown Compatibility Rules

All Markdown MUST be compatible with:

- CommonMark
- MkDocs Markdown parser
- Obsidian Markdown engine

### Allowed:
- headings (#, ##, ###)
- lists
- code blocks (```language)
- tables
- blockquotes
- links

### Avoid:
- raw HTML unless strictly necessary
- embedded scripts
- inline styles
- non-standard Markdown extensions unless justified

---

## 3. Linking Strategy (CRITICAL)

### Internal links MUST:

- Work in both systems

Use:
- relative paths for MkDocs compatibility:
  ```md
  [Architecture](../architecture/system-design.md)