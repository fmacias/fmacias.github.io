from __future__ import annotations

import argparse
import shutil
from pathlib import Path


REPOSITORIES = {
    "TplQueue.Abstractions": "abstractions",
    "TplQueue.Adapter": "adapter",
    "TplQueue.Usage": "usage",
}

ROOT_FILES = {
    "README.md",
    "Directory.Build.props",
    "NuGet.config",
    "build.ps1",
    "test.ps1",
    "coverage.ps1",
    "pack-local.ps1",
}


def should_copy(repo_relative: Path) -> bool:
    parts = repo_relative.parts
    if repo_relative.as_posix() in ROOT_FILES:
        return True
    if parts and parts[0] == "docs" and repo_relative.suffix.lower() == ".md":
        return True
    if len(parts) >= 2 and parts[0] == "src" and repo_relative.name.lower() == "readme.md":
        return True
    if len(parts) >= 2 and parts[0] == "samples" and repo_relative.name.lower() == "readme.md":
        return True
    if len(parts) >= 2 and parts[0] == "test" and repo_relative.name.lower() == "readme.md":
        return True
    if parts and parts[0] == "consumers" and repo_relative.suffix.lower() == ".md":
        return True
    return False


def copy_repo_docs(source_repo: Path, target_repo: Path) -> None:
    if target_repo.exists():
        shutil.rmtree(target_repo)
    target_repo.mkdir(parents=True, exist_ok=True)

    copied_root_readme = False

    for source_file in sorted(source_repo.rglob("*")):
        if not source_file.is_file():
            continue
        repo_relative = source_file.relative_to(source_repo)
        if not should_copy(repo_relative):
            continue

        destination = target_repo / repo_relative
        destination.parent.mkdir(parents=True, exist_ok=True)

        if repo_relative == Path("README.md"):
            shutil.copy2(source_file, target_repo / "index.md")
            copied_root_readme = True
            continue

        shutil.copy2(source_file, destination)

    if not copied_root_readme:
        raise FileNotFoundError(f"Missing README.md in {source_repo}")


def create_placeholder(path: Path, title: str, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# {title}\n\n{body}\n", encoding="utf-8")


def rewrite_markdown(path: Path, replacements: dict[str, str]) -> None:
    if not path.exists():
        return

    text = path.read_text(encoding="utf-8")
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def duplicate_readme_as_index(path: Path) -> None:
    if not path.exists():
        return

    index_path = path.with_name("index.md")
    index_path.write_text(path.read_text(encoding="utf-8"), encoding="utf-8")


def ensure_usage_placeholders(target_repo: Path) -> None:
    create_placeholder(
        target_repo / "samples" / "QueueObserverConsole" / "Logs.md",
        "Logs",
        "The runtime-generated log files are not imported into the site build. See the sample README for the logging behavior and create the logs by running the sample locally.",
    )
    create_placeholder(
        target_repo
        / "docs"
        / "test"
        / "integration"
        / "Fmacias.TplQueue.Usage.Integration.Test.md",
        "Integration Project",
        "This path refers to the package-based integration project in the source repository. The project file itself is not mirrored into the site, but the surrounding documentation remains available here.",
    )
    rewrite_markdown(
        target_repo / "docs" / "reference.md",
        {
            "(test/integration/Fmacias.TplQueue.Usage.Integration.Test)": "(test/integration/Fmacias.TplQueue.Usage.Integration.Test.md)",
        },
    )
    rewrite_markdown(
        target_repo / "samples" / "QueueObserverConsole" / "README.md",
        {
            "[Logs](Logs)": "[Logs](Logs.md)",
        },
    )


def normalize_adapter_docs(target_repo: Path) -> None:
    test_readme = target_repo / "test" / "README.md"
    duplicate_readme_as_index(test_readme)
    if test_readme.exists():
        test_readme.unlink()
    rewrite_markdown(
        target_repo / "docs" / "development" / "index.md",
        {
            "(../../test/README.md)": "(../../test/index.md)",
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync public TplQueue repository markdown into the site documentation tree."
    )
    parser.add_argument(
        "--source-base",
        default="..",
        help="Base directory that contains TplQueue.Abstractions, TplQueue.Adapter, and TplQueue.Usage.",
    )
    parser.add_argument(
        "--target-root",
        default="docs/en/tplqueue/reference",
        help="Target root inside the site repository.",
    )
    args = parser.parse_args()

    site_root = Path(__file__).resolve().parent.parent
    source_base = (site_root / args.source_base).resolve()
    target_root = (site_root / args.target_root).resolve()
    target_root.mkdir(parents=True, exist_ok=True)

    for repo_name, slug in REPOSITORIES.items():
        source_repo = source_base / repo_name
        if not source_repo.exists():
            raise FileNotFoundError(f"Cannot find source repository: {source_repo}")
        repo_target = target_root / slug
        copy_repo_docs(source_repo, repo_target)
        if slug == "usage":
            ensure_usage_placeholders(repo_target)
        if slug == "adapter":
            normalize_adapter_docs(repo_target)

    print(f"Synced public TplQueue docs from {source_base} into {target_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
