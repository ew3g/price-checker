import requests
from bs4 import BeautifulSoup

class Scraper:
    
    def get_product_details(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        details = {"name": "", "price": 0, "deal": True, "url": ""}
        #_url = (url)
        #if _url == "":
        #    details = None
        #else:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")
        #title = soup.find(id="productTitle")
        #price = soup.find(id="priceblock_dealprice")

        print(soup.find(id="productTitle").get_text())
        '''if price is None:
            price = soup.find(id="priceblock_ourprice")
            details["deal"] = False
        if title is not None and price is not None:
            details["name"] = title.get_text().strip()
            details["price"] = get_converted_price(price.get_text())
            details["url"] = _url
        else:
            return None
        return details
'''



scraper = Scraper()
print(scraper.get_product_details('https://www.amazon.com.br/GALAX-GeForce-1-Click-192-Bit-26NRL7HPX7OC/dp/B07NF7KB62/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=rtx+2060&qid=1606765964&sr=8-1'))