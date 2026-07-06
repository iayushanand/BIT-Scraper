from bs4 import BeautifulSoup

BASE_URL = "https://bit-bangalore.edu.in"


def parse_departments(html: str):

    soup = BeautifulSoup(html, "lxml")

    departments = []

    for card in soup.select("div.blog-post"):

        title = card.select_one(".blog-title a")

        if not title:
            continue

        about_url = BASE_URL + title["href"]

        slug = (
            about_url
            .split("/")[-1]
            .replace("-about", "")
        )

        image = None

        img = card.select_one(".blog-img img")

        if img:
            src = img.get("src", "")

            image = (
                BASE_URL + src
                if src.startswith("/")
                else src
            )

        email = None
        contact_url = None
        started = None
        hod = None

        desk = card.select_one(".blog-desk")

        if desk:

            contact = desk.select_one("a")

            if contact:
                email = (
                    contact.get_text(strip=True)
                    .replace("Contact :", "")
                    .strip()
                )

                href = contact.get("href", "")

                contact_url = (
                    BASE_URL + href
                    if href.startswith("/")
                    else href
                )

            lines = [
                x.strip()
                for x in desk.get_text("\n").split("\n")
                if x.strip()
            ]

            for line in lines:

                if line.startswith("Started In"):

                    try:
                        started = int(
                            line.replace(
                                "Started In :",
                                ""
                            ).strip()
                        )

                    except ValueError:
                        pass

                elif line.startswith("HOD"):

                    hod = (
                        line.replace(
                            "HOD :",
                            ""
                        ).strip()
                    )

        departments.append({

            "id": slug,

            "name": title.get_text(strip=True),

            "started": started,

            "hod_name": hod,

            "email": email,

            "about_url": about_url,

            "contact_url": contact_url,

            "image": image

        })

    return departments