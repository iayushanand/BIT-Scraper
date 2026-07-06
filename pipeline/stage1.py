from config import BASE_URL

from crawler.browser import Browser
from crawler.storage import (
    save_html,
    save_bit,
)

from parsers.departments import (
    parse_departments,
)


def run():

    print("=" * 60)
    print("Stage 1 - Department List")
    print("=" * 60)

    browser = Browser()

    browser.start()

    try:

        html = browser.download(
            f"{BASE_URL}/department-list"
        )

        save_html(
            "html/department_list.html",
            html
        )

        departments = parse_departments(html)

        save_bit(departments)

        print(
            f"Found {len(departments)} departments."
        )

    finally:

        browser.close()

    print("Stage 1 Complete\n")