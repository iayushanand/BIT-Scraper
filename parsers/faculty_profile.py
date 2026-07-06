from bs4 import BeautifulSoup


def parse_faculty_profile(html: str) -> dict:

    soup = BeautifulSoup(html, "lxml")

    details = {
        "image": None,
        "phone": None,
        "email": None,
        "qualification": None,
        "specialization": None,
        "teaching_interest": None,
    }

    img = soup.select_one(".featured-thumbnail img")

    if img:
        details["image"] = img.get("src")

    for li in soup.select(".info-list li"):

        text = li.get_text(" ", strip=True).lower()

        span = li.find("span")

        if not span:
            continue

        value = span.get_text(" ", strip=True)

        if "phone" in text:
            details["phone"] = value

        elif "email" in text:
            details["email"] = value

        elif "qualification" in text:
            details["qualification"] = value

    for heading in soup.select("div[style*='background-color']"):

        title = heading.get_text(" ", strip=True).lower()

        body = heading.find_next("div", class_="member-info-box")

        if not body:
            continue

        text = body.get_text(" ", strip=True)

        if "specialization" in title:
            details["specialization"] = text

        elif "teaching interest" in title:
            details["teaching_interest"] = text

    return details