from crawler.browser import Browser
from crawler.storage import (
    load_bit,
    save_bit,
    save_html,
)

from parsers.department import parse_department


def run():

    print("=" * 60)
    print("Stage 2 - Department Pages")
    print("=" * 60)

    departments = load_bit()

    browser = Browser()
    browser.start()

    try:

        for dept in departments:

            print(f"Scraping {dept['name']}")

            html = browser.download(
                dept["about_url"]
            )

            save_html(
                f"html/dept/{dept['id']}.html",
                html
            )

            parsed = parse_department(html)

            dept.update(parsed)

    finally:

        browser.close()

    save_bit(departments)

    print(
        f"Updated {len(departments)} departments."
    )

    print("Stage 2 Complete\n")