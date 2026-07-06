from pathlib import Path

from crawler.storage import (
    load_bit,
    save_bit,
    load_html,
)

from parsers.faculty_profile import parse_faculty_profile


def run():

    print("=" * 60)
    print("Stage 6 - Faculty Profile Details")
    print("=" * 60)

    departments = load_bit()

    for dept in departments:

        print(f"\nDepartment: {dept['name']}")

        folder = Path(
            f"html/teaching_profiles/{dept['id']}"
        )

        for teacher in dept["teaching"]:

            file = folder / f"{teacher['id']}.html"

            if not file.exists():
                print(f"Missing: {file.name}")
                continue

            html = load_html(file)

            teacher["details"] = parse_faculty_profile(html)

            print(f"Updated {teacher['name']}")

    save_bit(departments)

    print("\nStage 6 Complete.\n")