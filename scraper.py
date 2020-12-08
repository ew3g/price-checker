import requests
from bs4 import BeautifulSoup
from model.siteType import SiteType
from fake_useragent import UserAgent

class Scraper:
    
    def get_product_details(self, url, site_type: SiteType):
        ua = UserAgent()
        print(ua.random)
        headers = {
            "User-Agent": ua.random
            #"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }
        details = {"name": "", "price": 0, "deal": True, "url": ""}
        #_url = (url)
        #if _url == "":
        #    details = None
        #else:
        proxies = {
            "http": 'http://200.152.101.194:8080', 
            #"https": 'http://116.197.134.222:8080'
        }
        page = requests.get(url, headers=headers, proxies=proxies)
        soup = BeautifulSoup(page.content, "html5lib")
        #print(page.text)
        #title = soup.find(id="productTitle")
        #price = soup.find(id="priceblock_dealprice")

        #print('\n\n')
        #print(site_type.value)
        price = None
        '''if(site_type.value == SiteType.KABUM):
            price = soup.find("div",{"class":"preco_normal"}).get_text().strip()
        if(site_type.value == SiteType.TERABYTE):
            price = ''
        if(site_type.value == SiteType.PICHAU):
            price = ''
        if(site_type == SiteType.AMAZON):
            price = '''''
        
        
        
        print(soup)
        #print()
        
        
        '''print(soup.find(
            id='preco_desconto'
            self.get_price_id_field(site_type)))'''
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

    def get_price_id_field(self, site_type: SiteType):
        switcher = {
            SiteType.KABUM: 'preco_desconto',
            SiteType.TERABYTE: 'valVista',
            SiteType.PICHAU: 'price-boleto',
            SiteType.AMAZON: 'priceblock_dealprice',
        } 
        return switcher.get(site_type, None)

scraper = Scraper()
#print(s.get_price_id_field(SiteType('KABUM')))
kabum='https://www.kabum.com.br/produto/100235/placa-de-v-deo-galax-nvidia-geforce-rtx-2060-6gb-gddr6-26nrl7hpx7oc'
terabyte='https://www.terabyteshop.com.br/produto/10304/placa-de-video-galax-geforce-rtx-2060-1-click-oc-6gb-26nrl7hpx7oc-gddr6-pci-exp'
pichau='https://www.pichau.com.br/hardware/placa-de-video/placa-de-video-galax-geforce-rtx-2060-6gb-gddr6-1-click-oc-192-bit-26nrl7hpx7oc'
amazon='https://www.amazon.com.br/GALAX-GeForce-1-Click-192-Bit-26NRL7HPX7OC/dp/B07NF7KB62'


'''scraper.get_product_details(
    'https://www.kabum.com.br/produto/100235/placa-de-v-deo-galax-nvidia-geforce-rtx-2060-6gb-gddr6-26nrl7hpx7oc'
    ,SiteType('KABUM'))
       ''' 


print(
    scraper.get_product_details(
        'https://www.terabyteshop.com.br/produto/10304/placa-de-video-galax-geforce-rtx-2060-1-click-oc-6gb-26nrl7hpx7oc-gddr6-pci-exp'
        ,SiteType('TERABYTE'))
        )

'''
print(
    scraper.get_product_details(
        'https://www.pichau.com.br/hardware/placa-de-video/placa-de-video-galax-geforce-rtx-2060-6gb-gddr6-1-click-oc-192-bit-26nrl7hpx7oc'
        ,SiteType('PICHAU'))
        )


print(
    scraper.get_product_details(
        'https://www.amazon.com.br/GALAX-GeForce-1-Click-192-Bit-26NRL7HPX7OC/dp/B07NF7KB62'
        ,SiteType('AMAZON'))
        )'''