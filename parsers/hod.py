from bs4 import BeautifulSoup

BASE_URL = "https://bit-bangalore.edu.in"


def parse_hod(html: str) -> dict:

    soup = BeautifulSoup(html, "lxml")

    hod = {
        "name": None,
        "designation": None,
        "qualification": None,
        "email": None,
        "contact": None,
        "image": None,
        "read_more": None,
    }

    img = soup.select_one(".ttm_single_image-wrapper img")

    if img:

        src = img.get("src", "")

        if src.startswith("/"):
            src = BASE_URL + src

        hod["image"] = src

    for li in soup.select(".ttm-pf-detailbox-list li"):

        text = li.get_text(" ", strip=True)

        if text.startswith("Name"):

            hod["name"] = text.replace("Name :", "").strip()

        elif text.startswith("Designation"):

            hod["designation"] = text.replace("Designation :", "").strip()

        elif text.startswith("Qualification"):

            hod["qualification"] = text.replace("Qualification :", "").strip()

        elif text.startswith("Mail-ID"):

            hod["email"] = text.replace("Mail-ID :", "").strip()

        elif text.startswith("Contact Number"):

            hod["contact"] = text.replace("Contact Number :", "").strip()

        elif text.startswith("Read More"):

            a = li.find("a")

            if a:

                href = a.get("href", "")

                if href.startswith("/"):
                    href = BASE_URL + href

                hod["read_more"] = href

    return hod