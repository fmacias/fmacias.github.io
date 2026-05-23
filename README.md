# fmacias.github.io

Static documentation hub and professional website for Fernando Macias, built with MkDocs and Material for MkDocs.

## Purpose

This repository hosts:

- the public documentation hub for repositories under the `fmacias` GitHub account
- the main public documentation entry for the `TplQueue` ecosystem
- mirrored multilingual documentation from `TplQueue.Adapter` and `TplQueue.Core`
- concise `Services`, `Profile`, and `Contact` pages for Fernando Macias
- multilingual content in English and German, with Spanish planned later

## Site Structure

The site uses a multilingual folder-based content structure:

```text
docs/
  en/
    index.md
    services.md
    tplqueue/
      index.md
      usage/
      architecture/
      development/
      operations/
      core-engine/
      reference.md
      core-license.md
    profile.md
    contact.md
  de/
    index.md
    services.md
    tplqueue/
      index.md
      usage/
      architecture/
      development/
      operations/
      core-engine/
      reference.md
      core-license.md
    profile.md
    contact.md
  assets/
scripts/
  sync_tplqueue_public_docs.py
```

The public site is documentation-first. In the visible navigation, `TplQueue` should remain the first top-level item, while `Services`, `Profile`, and `Contact` remain available as secondary public pages.

Within `TplQueue`, the intended public structure is:

- the general ecosystem entry sourced from `TplQueue.Adapter/docs`
- a `Core Engine` section sourced from `TplQueue.Core/docs`
- the `Core License` page kept at the same tree level

The public landing pages are the language-specific `index.md` files under `docs/en/` and `docs/de/`.
Legacy `home.md` pages are not part of the current site structure.
Those landing pages are intentionally outside the visible top navigation.

Current language behavior:

- English is the default language at `/`
- German is available at `/de/`
- the landing pages are localized at `docs/en/index.md` and `docs/de/index.md`
- a small client-side script may redirect users from `/` to `/de/` when the browser language is German or a German preference was stored earlier

The sync script mirrors the TplQueue documentation trees from sibling repository `docs/<lang>/` folders. The generated `TplQueue` section in this repo should be treated as deployment/build output, not hand-maintained content.

## Sync Source Of Truth

`scripts/sync_tplqueue_public_docs.py` is the canonical refresh command for the TplQueue documentation content stored in this repository.

It has these responsibilities:

- sync `docs/en/` and `docs/de/` from `../TplQueue.Adapter/docs/` into the site `TplQueue` section
- sync `docs/en/` and `docs/de/` from `../TplQueue.Core/docs/` into the site `Core Engine` section
- sync `../TplQueue.Core/docs/<lang>/license.md` into the top-level `Core License` page for each language

Important rules for that sync:

- the source of truth is the `docs/<lang>/` folder inside each sibling repository
- `TplQueue.Adapter/docs/en/index.md` and `TplQueue.Adapter/docs/de/index.md` are the main public entries for the ecosystem on this site
- `TplQueue.Core/docs/en/index.md` and `TplQueue.Core/docs/de/index.md` are the main sources for the `Core Engine` branch on this site
- `Agents.md` or `AGENTS.md` files are instruction files only and must never be copied into the published site tree
- when rebuilding the site documentation, update the source repository docs first, then rerun `python .\scripts\sync_tplqueue_public_docs.py`

## Local Setup

Create and activate a virtual environment, then install the required packages:

```powershell
pip install -r requirements.txt
```

The current dependencies include:

- `mkdocs-material`
- `mkdocs-static-i18n`

If you prefer direct installation, this also works:

```powershell
pip install "mkdocs-static-i18n[material]"
```

## Local Development

Sync the public TplQueue documentation sources, then start the local development server:

```powershell
python .\scripts\sync_tplqueue_public_docs.py
python -m mkdocs serve
```

Useful local commands:

```powershell
python .\scripts\sync_tplqueue_public_docs.py
python -m mkdocs serve
python -m mkdocs build
python -m mkdocs build --clean
```

If `mkdocs` is already on your PATH, the equivalent commands are:

```powershell
mkdocs serve
mkdocs build
```

What to expect:

- English pages are served from `/`
- German pages are served from `/de/`
- English content uses root-relative routes such as `/services/`
- German content uses `/de/`-prefixed routes such as `/de/services/`
- the multilingual build depends on the `i18n` plugin from `mkdocs-static-i18n`
- the imported TplQueue public reference pages are refreshed by `scripts/sync_tplqueue_public_docs.py`

## Release Notes For Maintainers

Before releasing or deploying:

1. Install dependencies from `requirements.txt`.
2. Run `python .\scripts\sync_tplqueue_public_docs.py`.
3. Verify that `mkdocs serve` works locally.
4. Verify that English pages resolve under `/`.
5. Verify that German pages resolve under `/de/`.
6. Run `mkdocs build` and confirm the static output is generated without configuration errors.
7. Ensure the deployment workflow installs both Material for MkDocs and `mkdocs-static-i18n` before building.

Important operational points:

- GitHub Pages serves generated static files only
- `mkdocs-static-i18n` is a build-time dependency, not a runtime server dependency
- the language preference logic is client-side JavaScript and only affects browser navigation
- for this user site repository, root-relative links such as `/` and `/de/` are appropriate

## GitHub Pages

This repository should be deployed through a GitHub Actions build, not by publishing the raw repository contents directly.

Important:

- the `.github/workflows/ci.yml` workflow is required for deployment
- without that workflow, GitHub Pages will not install MkDocs, Material, or `mkdocs-static-i18n`
- without that workflow, the public TplQueue docs from the sibling repositories will not be imported into the site tree
- without that workflow, the multilingual site should be considered not deployable in its intended form

The deployment environment must:

- install Python dependencies
- run the MkDocs build from `mkdocs.yml`
- publish the generated static site to GitHub Pages

The repository includes a workflow at `.github/workflows/ci.yml` based on the Material for MkDocs publishing guide. On every push to `main`, GitHub Actions:

- checks out the repository
- configures git credentials for deployment
- installs Python
- restores the MkDocs / Material cache
- installs dependencies from `requirements.txt`
- checks out the public `TplQueue.Abstractions`, `TplQueue.Adapter`, and `TplQueue.Usage` repositories
- runs `python scripts/sync_tplqueue_public_docs.py --source-base .external-src`
- runs `mkdocs gh-deploy --force`

For GitHub Pages to publish correctly, ensure the repository Pages setting uses:

- source branch: `gh-pages`
- folder: `/ (root)`

Expected behavior after a push to `main`:

1. GitHub Actions starts the workflow from `.github/workflows/ci.yml`.
2. The workflow installs the dependencies from `requirements.txt`.
3. MkDocs builds the multilingual static site from `mkdocs.yml`.
4. `mkdocs gh-deploy --force` publishes the generated output to `gh-pages`.
5. GitHub Pages serves the published static files from that branch.
6. The site is available at `https://fmacias.github.io/`.
7. English resolves at `/`.
8. German resolves at `/de/`.
9. The browser-side language-preference script may redirect users from `/` to `/de/` when German is the stored or detected preference.

Expected behavior if the workflow is missing or disabled:

- the site will not be rebuilt automatically on push
- GitHub Pages will not receive the generated multilingual output
- plugin-dependent features such as `mkdocs-static-i18n` will not be applied during deployment
- the published result may be outdated, incomplete, or broken

Release / deployment checklist:

1. `pip install -r requirements.txt`
2. `python .\scripts\sync_tplqueue_public_docs.py`
3. `python -m mkdocs serve`
4. `python -m mkdocs build --clean`
5. push to `main`
6. confirm the GitHub Actions workflow passed
7. confirm Pages is configured to publish from `gh-pages`

## References

- Material for MkDocs publishing guide:
  https://squidfunk.github.io/mkdocs-material/publishing-your-site/
- Material for MkDocs getting started:
  https://squidfunk.github.io/mkdocs-material/getting-started/
- MkDocs static i18n installation:
  https://ultrabug.github.io/mkdocs-static-i18n/getting-started/installation/
- MkDocs static i18n quick start:
  https://ultrabug.github.io/mkdocs-static-i18n/getting-started/quick-start/
- GitHub Pages overview:
  https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages
- GitHub Pages and GitHub Actions context:
  https://docs.github.com/github/working-with-github-pages/about-github-pages-and-jekyll
