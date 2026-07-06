from bs4 import BeautifulSoup

BASE_URL = "https://bit-bangalore.edu.in"


def parse_teaching(html: str) -> list[dict]:

    soup = BeautifulSoup(html, "lxml")

    faculty = []

    for card in soup.select(".featured-imagebox"):

        name = None
        designation = None
        thumbnail = None
        profile_url = None
        faculty_id = None

        h6 = card.select_one("h6")

        if h6:
            name = h6.get_text(" ", strip=True)

        small = card.select_one("small")

        if small:
            designation = small.get_text(" ", strip=True)

        img = card.select_one("img")

        if img:
            thumbnail = img.get("src")

        button = card.select_one("a.ttm-btn")

        if button:

            href = button.get("href", "")

            if href.startswith("/"):
                href = BASE_URL + href

            profile_url = href

            faculty_id = href.rstrip("/").split("/")[-1]

        faculty.append({

            "id": faculty_id,

            "name": name,

            "designation": designation,

            "thumbnail": thumbnail,

            "profile_url": profile_url,

            "details": None

        })

    return faculty