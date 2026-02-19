"""Create a new project by copying a local template and renaming package identifiers."""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

TEMPLATE_NAMES = ("app", "library", "research")
TEXT_SUFFIXES = {".py", ".md", ".txt", ".toml", ".yaml", ".yml", ".ipynb"}
PACKAGE_PLACEHOLDER = "template_pkg"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments for project generation."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("template", choices=TEMPLATE_NAMES, help="Template type to copy.")
    parser.add_argument("destination", type=Path, help="Folder where the new project will be created.")
    parser.add_argument("--package-name", required=True, help="Python package name for src/<package_name>.")
    parser.add_argument("--project-name", default="", help="Optional display name for docs and run names.")
    return parser.parse_args()


def validate_package_name(package_name: str) -> None:
    """Validate package naming constraints."""
    if not re.fullmatch(r"[a-zA-Z_][a-zA-Z0-9_]*", package_name):
        raise ValueError(
            "Invalid package name. Use a valid Python identifier like 'my_project_pkg'."
        )


def copy_template(template_name: str, destination: Path) -> None:
    """Copy selected template tree into destination."""
    repo_root = Path(__file__).resolve().parents[1]
    template_dir = repo_root / "templates" / template_name
    if not template_dir.exists():
        raise FileNotFoundError(f"Template not found: {template_dir}")
    if destination.exists():
        raise FileExistsError(f"Destination already exists: {destination}")

    shutil.copytree(template_dir, destination)


def rename_package_folder(destination: Path, package_name: str) -> None:
    """Rename src package folder from placeholder to package_name."""
    src_dir = destination / "src"
    old_pkg_dir = src_dir / PACKAGE_PLACEHOLDER
    new_pkg_dir = src_dir / package_name
    if not old_pkg_dir.exists():
        raise FileNotFoundError(f"Expected placeholder package folder: {old_pkg_dir}")
    old_pkg_dir.rename(new_pkg_dir)


def replace_text_tokens(destination: Path, package_name: str, project_name: str) -> None:
    """Replace placeholder tokens in text-like files."""
    run_name = (project_name or destination.name).replace(" ", "-").lower() + "-run"

    for path in destination.rglob("*"):
        if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
            continue

        content = path.read_text(encoding="utf-8")
        content = content.replace(PACKAGE_PLACEHOLDER, package_name)
        content = re.sub(r"(?:app|library|research)-template-run", run_name, content)
        content = content.replace("template-run", run_name)

        if project_name and path.name in {"README.md", "config.yaml"}:
            content = content.replace("Template", project_name)

        path.write_text(content, encoding="utf-8")


def main() -> int:
    """Generate a project from a local template."""
    args = parse_args()
    validate_package_name(args.package_name)

    copy_template(args.template, args.destination)
    rename_package_folder(args.destination, args.package_name)
    replace_text_tokens(args.destination, args.package_name, args.project_name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
