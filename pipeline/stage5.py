from pathlib import Path

from crawler.browser import Browser
from crawler.storage import (
    load_bit,
    save_html,
)


def run():

    print("=" * 60)
    print("Stage 5 - Teaching Faculty Profiles")
    print("=" * 60)

    departments = load_bit()

    browser = Browser()
    browser.start()

    try:

        for dept in departments:

            dept_id = dept["id"]

            folder = Path(f"html/teaching_profiles/{dept_id}")
            folder.mkdir(parents=True, exist_ok=True)

            print(f"\nDepartment: {dept['name']}")

            for teacher in dept["teaching"]:

                url = teacher["profile_url"]

                if not url:
                    continue

                print(f"  Downloading {teacher['name']}")

                html = browser.download(url)

                save_html(
                    folder / f"{teacher['id']}.html",
                    html
                )

    finally:

        browser.close()

    print("\nStage 5 Complete.\n")