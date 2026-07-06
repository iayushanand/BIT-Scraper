from bs4 import BeautifulSoup
import re

BASE_URL = "https://bit-bangalore.edu.in"


def _get_section(soup, title):
    for header in soup.select("h4.title"):
        if header.get_text(strip=True).lower() == title.lower():
            return header.find_parent(class_="section-title")
    return None


def _get_list(section):
    if not section:
        return []

    return [
        span.get_text(" ", strip=True)
        for span in section.select("ul li span.ttm-list-li-content")
    ]


def parse_department(html: str) -> dict:

    soup = BeautifulSoup(html, "lxml")

    image = None

    img = soup.select_one(".ttm-service-description img")

    if img:
        src = img.get("src", "")

        if src.startswith("/"):
            src = BASE_URL + src

        image = src

    description = []

    desc = soup.select_one(".ttm-service-description")

    if desc:

        for p in desc.select("p"):

            text = p.get_text(" ", strip=True)

            if text:
                description.append(text)

    description = "\n\n".join(description)

    stats = {}

    for box in soup.select(".counter-box"):

        p = box.find("p")
        span = box.find("span")

        if not p or not span:
            continue

        label = (
            p.get_text(" ", strip=True)
            .lower()
            .replace(".", "")
            .replace("-", " ")
            .replace("%", "percent")
        )

        value = span.get_text(strip=True)

        if not label or not value:
            continue

        try:
            value = int(value)
        except ValueError:
            pass

        key = re.sub(r"[^a-z0-9]+", "_", label)
        key = key.strip("_")

        stats[key] = value

    vision = None

    section = _get_section(soup, "Vision")

    if section:

        p = section.find("p")

        if p:
            vision = p.get_text(" ", strip=True)

    mission = _get_list(
        _get_section(soup, "Mission")
    )

    peos = _get_list(
        _get_section(
            soup,
            "Program Educational Objectives (PEO's)"
        )
    )

    program_outcomes = _get_list(
        _get_section(
            soup,
            "Program Outcomes"
        )
    )

    program_specific_outcomes = _get_list(
        _get_section(
            soup,
            "Program Specific Outcomes"
        )
    )

    urls = {
        "hod": None,
        "teaching": None,
        "non_teaching": None,
    }

    for a in soup.select(".widget-menu a"):

        href = a.get("href", "")

        if href.startswith("/department-hod/"):

            urls["hod"] = BASE_URL + href

        elif href.startswith("/teaching-faculties/"):

            urls["teaching"] = BASE_URL + href

        elif href.startswith("/non-teaching-faculties/"):

            urls["non_teaching"] = BASE_URL + href

    return {

        "image": image,

        "description": description,

        "stats": stats,

        "vision": vision,

        "mission": mission,

        "peos": peos,

        "program_outcomes": program_outcomes,

        "program_specific_outcomes": program_specific_outcomes,

        "urls": urls,
    }