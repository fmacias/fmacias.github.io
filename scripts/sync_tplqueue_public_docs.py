from __future__ import annotations

import argparse
import shutil
from pathlib import Path


LANGUAGES = ("en", "de")

ADAPTER_DOC_ITEMS = (
    "index.md",
    "reference.md",
    "usage",
    "architecture",
    "development",
    "operations",
)

ADAPTER_STALE_ITEMS = (
    "overview.md",
    "getting-started.md",
    "architecture.md",
    "reference",
    "repositories",
)

CORE_DOC_ITEMS = (
    "index.md",
    "reference.md",
    "usage",
    "architecture",
    "development",
    "operations",
)


def remove_target_items(target_root: Path, items: tuple[str, ...]) -> None:
    target_root.mkdir(parents=True, exist_ok=True)

    for item_name in items:
        existing = target_root / item_name
        if existing.is_dir():
            shutil.rmtree(existing)
        elif existing.exists():
            existing.unlink()


def copy_doc_tree(source_root: Path, target_root: Path, items: tuple[str, ...]) -> None:
    remove_target_items(target_root, items)

    for item_name in items:
        source_item = source_root / item_name
        if not source_item.exists():
            continue

        destination = target_root / item_name
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
    core_docs = source_base / "TplQueue.Usage" / "TplQueue.Core" / "docs"

    for language in LANGUAGES:
        adapter_source = adapter_docs / language
        core_source = core_docs / language
        if not adapter_source.exists():
            raise FileNotFoundError(f"Cannot find adapter docs source: {adapter_source}")
        if not core_source.exists():
            raise FileNotFoundError(f"Cannot find core docs source: {core_source}")

        tplqueue_root = site_root / "docs" / language / "tplqueue"
        core_engine_root = tplqueue_root / "core-engine"

        remove_target_items(tplqueue_root, ADAPTER_STALE_ITEMS)
        copy_doc_tree(adapter_source, tplqueue_root, ADAPTER_DOC_ITEMS)
        remove_agents_files(tplqueue_root)
        normalize_adapter_entry_docs(tplqueue_root)

        copy_doc_tree(core_source, core_engine_root, CORE_DOC_ITEMS)
        remove_agents_files(core_engine_root)

        license_source = core_source / "license.md"
        if license_source.exists():
            shutil.copy2(license_source, core_engine_root / "license.md")
            shutil.copy2(license_source, tplqueue_root / "core-license.md")

    print(f"Synced TplQueue docs from {source_base} into {site_root / 'docs'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
