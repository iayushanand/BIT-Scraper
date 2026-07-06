from pathlib import Path

from crawler.browser import Browser
from crawler.storage import (
    load_bit,
    save_bit,
    save_html,
)

from parsers.non_teaching import parse_non_teaching


HTML_DIR = Path("html/non_teaching")


def run():

    print("=" * 60)
    print("Stage 7 - Non Teaching Staff")
    print("=" * 60)

    HTML_DIR.mkdir(parents=True, exist_ok=True)

    departments = load_bit()

    browser = Browser()
    browser.start()

    try:

        for dept in departments:

            print(f"Scraping {dept['name']}")

            url = dept["urls"]["non_teaching"]

            if not url:
                print("No non-teaching page.")
                dept["non_teaching"] = []
                continue

            html = browser.download(url)

            save_html(
                HTML_DIR / f"{dept['id']}.html",
                html,
            )

            dept["non_teaching"] = parse_non_teaching(html)

            print(
                f"Found {len(dept['non_teaching'])} staff members."
            )

    finally:

        browser.close()

    save_bit(departments)

    print("\nStage 7 Complete.\n")