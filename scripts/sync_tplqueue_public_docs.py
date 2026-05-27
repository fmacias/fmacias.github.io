from __future__ import annotations

import argparse
import shutil
from pathlib import Path


LANGUAGES = ("en", "de")


def reset_directory(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copy_directory_contents(source_root: Path, target_root: Path) -> None:
    reset_directory(target_root)

    for source_item in source_root.iterdir():
        destination = target_root / source_item.name
        if source_item.is_dir():
            shutil.copytree(source_item, destination)
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_item, destination)


def remove_agents_files(target_root: Path) -> None:
    for source_file in sorted(target_root.rglob("*")):
        if not source_file.is_file():
            continue
        if source_file.name.lower() == "agents.md":
            source_file.unlink()


def rewrite_markdown(path: Path, replacements: dict[str, str]) -> None:
    if not path.exists():
        return

    text = path.read_text(encoding="utf-8")
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def normalize_adapter_entry_docs(target_root: Path) -> None:
    rewrite_markdown(
        target_root / "development" / "index.md",
        {
            "(../../test/README.md)": "(https://github.com/fmacias/TplQueue.Adapter/tree/main/test)",
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sync multilingual TplQueue documentation trees from source repositories into the site."
    )
    parser.add_argument(
        "--source-base",
        default="..",
        help="Base directory that contains TplQueue.Adapter and TplQueue.Usage.",
    )
    args = parser.parse_args()

    site_root = Path(__file__).resolve().parent.parent
    source_base = (site_root / args.source_base).resolve()
    adapter_docs = source_base / "TplQueue.Adapter" / "docs"

    for language in LANGUAGES:
        adapter_source = adapter_docs / language
        if not adapter_source.exists():
            raise FileNotFoundError(f"Cannot find adapter docs source: {adapter_source}")

        tplqueue_root = site_root / "docs" / language / "tplqueue"

        copy_directory_contents(adapter_source, tplqueue_root)
        remove_agents_files(tplqueue_root)
        normalize_adapter_entry_docs(tplqueue_root)

    print(f"Synced TplQueue docs from {source_base} into {site_root / 'docs'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
