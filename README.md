# fmacias.github.io

Static personal and technical website for Fernando Macias, built with MkDocs and Material for MkDocs.

## Purpose

This repository hosts:

- the public professional profile of Fernando Macias
- curated technical documentation, including `Fmacias.TplQueue`
- multilingual content in English and German, with Spanish planned later

## Site Structure

The site uses a multilingual folder-based content structure:

```text
docs/
  en/
  de/
  assets/
```

Current language behavior:

- English is the default language at `/`
- German is available at `/de/`
- a small client-side script may redirect users from `/` to `/de/` when the browser language is German or a German preference was stored earlier

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

Start the local development server:

```powershell
mkdocs serve
```

Useful local commands:

```powershell
mkdocs serve
mkdocs build
mkdocs build --clean
```

If `mkdocs` is not on your PATH, run it through the selected Python environment instead:

```powershell
python -m mkdocs serve
python -m mkdocs build
```

What to expect:

- English pages are served from `/`
- German pages are served from `/de/`
- the multilingual build depends on the `i18n` plugin from `mkdocs-static-i18n`

## Release Notes For Maintainers

Before releasing or deploying:

1. Install dependencies from `requirements.txt`.
2. Verify that `mkdocs serve` works locally.
3. Verify that English pages resolve under `/`.
4. Verify that German pages resolve under `/de/`.
5. Run `mkdocs build` and confirm the static output is generated without configuration errors.
6. Ensure the deployment workflow installs both Material for MkDocs and `mkdocs-static-i18n` before building.

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
2. `mkdocs serve`
3. `mkdocs build --clean`
4. push to `main`
5. confirm the GitHub Actions workflow passed
6. confirm Pages is configured to publish from `gh-pages`

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
