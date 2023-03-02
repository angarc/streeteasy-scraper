from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def get_page_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/108.0.0.0 Safari/537.36"
    }
    soup = None

    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, "html.parser")

    return soup
