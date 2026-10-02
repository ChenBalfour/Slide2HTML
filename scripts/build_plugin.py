"""Build the ZIP users can import directly into Codex. No external dependencies."""
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "dist" / "slide2html-plugin.zip"


def build():
    portable = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8-sig"))
    codex = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8-sig"))
    for field in ("name", "version", "homepage", "repository"):
        if portable[field] != codex[field]:
            raise ValueError(f"Manifests disagree on {field}")
    if portable["extensions"]["com.openai"]["interface"] != codex["interface"]:
        raise ValueError("Manifests disagree on listing metadata")

    files = [ROOT / "plugin.json", ROOT / ".codex-plugin" / "plugin.json", ROOT / "README.md"]
    files += [p for p in (ROOT / "skills").rglob("*")
              if p.is_file() and "__pycache__" not in p.parts
              and p.suffix not in (".pyc", ".pyo")]
    entries = {p.relative_to(ROOT).as_posix(): p.read_bytes() for p in files}
    if "skills/slide2html/SKILL.md" not in entries:
        raise ValueError("Missing Slide2HTML skill entrypoint")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(OUTPUT, "w", compression=ZIP_DEFLATED) as archive:
        for name, content in sorted(entries.items()):
            entry = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            archive.writestr(entry, content)
    with ZipFile(OUTPUT) as archive:
        if set(archive.namelist()) != set(entries):
            raise ValueError("ZIP file list does not match source files")
        for name, content in entries.items():
            if archive.read(name) != content:
                raise ValueError(f"ZIP content mismatch: {name}")
    print(f"Built {OUTPUT} ({len(entries)} files, version {portable['version']})")


if __name__ == "__main__":
    build()
