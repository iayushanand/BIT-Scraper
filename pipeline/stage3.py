from crawler.browser import Browser
from crawler.storage import (
    load_bit,
    save_bit,
    save_html,
)

from parsers.hod import parse_hod


def run():

    print("=" * 60)
    print("Stage 3 - HOD")
    print("=" * 60)

    departments = load_bit()

    browser = Browser()
    browser.start()

    try:

        for dept in departments:

            print(f"Scraping HOD - {dept['name']}")

            html = browser.download(
                dept["urls"]["hod"]
            )

            save_html(
                f"html/hod/{dept['id']}.html",
                html
            )

            dept["hod"] = parse_hod(html)

    finally:

        browser.close()

    save_bit(departments)

    print("Stage 3 Complete\n")