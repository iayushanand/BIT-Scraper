# BIT Scraper

A web scraping pipeline that extracts department and faculty data from the [BIT Bangalore](https://bit-bangalore.edu.in) college website. It downloads raw HTML pages, parses them with BeautifulSoup, and outputs a single structured JSON file containing all departments, HODs, teaching staff, faculty profiles, and non-teaching staff.

## How It Works

The pipeline runs sequentially through 7 stages:

| Stage | Description |
|-------|-------------|
| 1 | Scrapes the department listing page |
| 2 | Scrapes individual department about pages |
| 3 | Scrapes HOD pages for each department |
| 4 | Scrapes teaching faculty listing pages |
| 5 | Downloads individual teaching faculty profile pages |
| 6 | Parses downloaded faculty profile HTMLs into structured data |
| 7 | Scrapes non-teaching staff pages |

All scraped HTML is saved to `html/` for offline re-parsing. The final output is written to `data/bit.json`.

## Setup

```bash
git clone https://github.com/iayushanand/bit-scraper.git
cd bit-scraper
```

Create a virtual environment and install dependencies:

```bash
python -m venv env
source env/bin/activate        # Linux/macOS
env\Scripts\activate           # Windows

pip install -r requirements.txt
playwright install chromium
```

## Usage

```bash
python main.py
```

## Project Structure

```
bit-scraper/
├── main.py
├── config.py
├── requirements.txt
│
├── crawler/
│   ├── browser.py              # Playwright browser wrapper
│   └── storage.py              # HTML and JSON file I/O
│
├── parsers/
│   ├── departments.py          # Department list parser
│   ├── department.py           # Department about page parser
│   ├── hod.py                  # HOD page parser
│   ├── teaching.py             # Teaching faculty list parser
│   ├── faculty_profile.py      # Faculty profile page parser
│   └── non_teaching.py         # Non-teaching staff parser
│
├── pipeline/
│   ├── stage1.py .. stage7.py  # Pipeline stages
│
├── html/                       # Downloaded HTML pages
│
└── data/
    └── bit.json                # Final output
```

## Requirements

- Python 3.10+
- [Playwright](https://playwright.dev/python/) (Chromium)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) with lxml

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).