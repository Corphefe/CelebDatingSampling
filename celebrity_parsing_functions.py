from bs4 import BeautifulSoup
import requests
import requests_cache
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# ---- Caching (before any sessions) ----
requests_cache.install_cache('scraper_cache', expire_after=3600)

# ---- One hardened Session reused everywhere ----
_session = requests.Session()
_session.headers.update({
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/118.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
})

retry = Retry(
    total=5, connect=5, read=5, status=5,
    backoff_factor=1.5,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET", "HEAD", "OPTIONS"]
)
adapter = HTTPAdapter(max_retries=retry)
_session.mount("https://", adapter)
_session.mount("http://", adapter)

def _fetch_soup(link, timeout=(5, 20)):
    """Return BeautifulSoup(html) or None on any network/HTTP failure."""
    try:
        r = _session.get(link, timeout=timeout)
        r.raise_for_status()
        return BeautifulSoup(r.text, "html.parser")
    except requests.RequestException:
        return None

def get_name(link):
    soup = _fetch_soup(link)
    if not soup:
        return None
    name_tag = soup.select_one(".ff-name")
    if not name_tag:
        return None
    # safer than find(string=True,...); handles nested spans/text nodes
    name = name_tag.find(string=True, recursive=False).strip()
    return name if name else None

def get_gender(link):
    soup = _fetch_soup(link)
    if not soup:
        return None
    gender_tag = soup.select_one('div[style*="padding-bottom:8px"]')
    if not gender_tag:
        return None
    gender_info = gender_tag.get_text(separator=" ", strip=True).lower()
    # Return 1 if contains "he" but not "she", else 0 if contains "she", else None
    if "he" in gender_info and "she" not in gender_info:
        return 1
    else:
        return 0

def get_age(link):
    soup = _fetch_soup(link)
    if not soup:
        return None
    age_info_tag = soup.select_one(".age")
    if not age_info_tag:
        return None
    age_tag = age_info_tag.select_one(".fact")
    if not age_tag:
        return None
    txt = age_tag.get_text(strip=True)
    try:
        return int(txt)
    except (TypeError, ValueError):
        return None

def relationship_links(link):
    soup = _fetch_soup(link)
    if not soup:
        return []
    relationship_tag = soup.select_one(".ff-dating-history, .ff-dating-history-grid")
    if not relationship_tag:
        return []
    relationships = []
    for box in relationship_tag.select(".ff-grid-box"):
        if box.select_one(".ff-rumour"):
            continue
        a_tag = box.select_one("a[href]")
        if a_tag and a_tag.get("href"):
            relationships.append(a_tag["href"])
    return relationships

SEARCH_BY_LETTER = "https://www.whosdatedwho.com/popular?letter="

def alphabet_links(letter):
    celebrities = []
    link = SEARCH_BY_LETTER + letter
    soup = _fetch_soup(link)
    if not soup:
        return []
    anchors = soup.select('.ff-grid-box')
    anchors.reverse()
    while (len(celebrities) < 5 and anchors):
        celeb = anchors.pop()
        a_tag = celeb.select_one("a")
        if a_tag and a_tag.get("href"):
            celebrities.append(a_tag["href"])
    return celebrities
