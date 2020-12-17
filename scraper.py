import requests
from bs4 import BeautifulSoup
from model.siteType import SiteType
from fake_useragent import UserAgent
from constants.constants import StringConstants


class Scraper:

    def get_product_price(self, url, site_type: SiteType):
        ua = UserAgent()
        headers = {
            StringConstants.USER_AGENT: ua.random
        }
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html5lib")

        price = None
        if(site_type == SiteType.KABUM):
            price = soup.find("div", {"class": "preco_normal"})
        if(site_type == SiteType.TERABYTE):
            price = soup.find(id='valParc')
        if(site_type == SiteType.PICHAU):
            price = soup.find("span", {"class": "price"})
        if(site_type == SiteType.AMAZON):
            price = soup.find(id="olp_feature_div")
            if price:
                price = price.find(id="olp-upd-new")
                if price:
                    price = price.find("span", {"class": "a-declarative"})
                    if price:
                        price = price.find("a", {"class": "a-link-normal"})
                        if price:
                            price = price.find("span", {"class": "a-size-base a-color-price"})

        return price
