import json
from pathlib import Path

from config import DATA_FILE


def save_html(path, html):
    path = Path(path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    path.write_text(
        html,
        encoding="utf-8"
    )


def load_html(path):
    return Path(path).read_text(
        encoding="utf-8"
    )


def save_bit(data):
    path = Path(DATA_FILE)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


def load_bit():
    path = Path(DATA_FILE)

    if not path.exists():
        return []

    with open(path, encoding="utf-8") as f:
        return json.load(f)