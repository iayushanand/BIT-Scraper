from crawler.browser import Browser
from crawler.storage import (
    load_bit,
    save_bit,
    save_html,
)

from parsers.teaching import parse_teaching


def run():

    print("=" * 60)
    print("Stage 4 - Teaching Faculty")
    print("=" * 60)

    departments = load_bit()

    browser = Browser()
    browser.start()

    try:

        for dept in departments:

            print(f"Scraping {dept['name']}")

            html = browser.download(
                dept["urls"]["teaching"]
            )

            save_html(
                f"html/teaching/{dept['id']}.html",
                html
            )

            dept["teaching"] = parse_teaching(html)

    finally:

        browser.close()

    save_bit(departments)

    print("Stage 4 Complete\n")