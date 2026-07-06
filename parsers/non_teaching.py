from bs4 import BeautifulSoup


def parse_non_teaching(html: str) -> list:

    soup = BeautifulSoup(html, "lxml")

    staff = []

    for card in soup.select(".featured-imagebox"):

        image = None
        name = None
        designation = None
        phone = None

        img = card.select_one(".featured-thumbnail img")

        if img:
            image = img.get("src")

        h6 = card.select_one("h6")

        if h6:
            name = h6.get_text(strip=True)

        smalls = card.select(".post-meta small")

        if len(smalls) >= 1:
            designation = smalls[0].get_text(strip=True)

        if len(smalls) >= 2:
            phone = smalls[1].get_text(strip=True)

        staff.append(
            {
                "name": name,
                "designation": designation,
                "phone": phone,
                "image": image,
            }
        )

    return staff