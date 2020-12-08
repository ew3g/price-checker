from model.product import Product
from model.site import Site
from model.siteType import SiteType
import configparser

class ConfigProperties:
    config = None

    def __init__(self):
        self.config = configparser.RawConfigParser() 
        self.config.read('config/configs.ini')

    def get_config_value(self, key):
        with open('config/config.properties') as f:
            for line in f:
                if "=" in line:
                    name, value = line.split("=", 1)
                    if name == key:
                        return value
            f.close()

    def save_config_value(self, key, value):
        with open('config/config.properties', 'a') as f:
            new_line = key + "=" + value + '\n'
            f.write(new_line)
            f.close()

    def get_all_products_configs(self):
        products_array = []
        with open('config/products.properties') as f:
            for line in f:
                if line is not None:
                    name = line.split('||||')[0]
                    value = line.split('||||')[1]
                    url = value.split(';')[0]
                    spreadsheet_id = value.split(';')[1]
                    
                    product = Product(name, url, spreadsheet_id)
                    products_array.append(product)

        return products_array

    def update_products_config(self, product: Product):
        with open('config/config.properties') as f:
            for line in f:
                 if "=" in line:
                    name, value = line.split("=", 1)
                    if name == product.name:
                        line = product.name + '||||' + product.url + ';' + product.spreadsheet_id
            f.close()

    def get_value(self, section, key):
        return self.config[section][key]
    
    def save_value(self, section, key, value):
        if section != 'DEFAULT':
            if not self.config.has_section(section):
                self.config.add_section(section)
        #if not self.config.has_option(section, key):
        self.config.set(section, key, value)
        
        ctg = open('config/configs.ini', 'w')
        self.config.write(ctg, space_around_delimiters=False)
        ctg.close()

    def get_products(self):
        '''sections = self.config.sections()
        products = []
        for section in sections:
            configs = dict(self.config.items(section))
            products.append(Product(section, configs.get('url'), configs.get('spreadsheet.id')))
        return products'''
        sites_list = []
        products = []
        for section in self.config.sections():
            #print(section)
            configs = dict(self.config.items(section))
            for c in configs:
                #print(SiteType._value2member_map_)
                key = c.upper()
                if key in SiteType._value2member_map_:  # works
                    site_type = SiteType(c.upper())
                    site = Site(site_type, configs.get(c))
                    sites_list.append(site)
                #if c == SiteType.KABUM.name:
                #    print(c + '=' + configs.get(c))
            
            products.append(Product(section,configs.get('spreadsheet.id'), sites_list))
        return products
        
'''
c = ConfigProperties()
print(c.get_products()._sites_list)'''