from model.product import Product
from model.site import Site
from model.siteType import SiteType
from constants import ConfigConstants, FileConstants, StringConstants
import configparser


class ConfigProperties:
    config = None

    def __init__(self):
        self.config = configparser.RawConfigParser() 
        self.config.read(ConfigConstants.CONFIG_FILE_PATH)

    def get_value(self, section, key):
        return self.config[section][key]

    def save_value(self, section, key, value):
        if section != ConfigConstants.DEFAULT:
            if not self.config.has_section(section):
                self.config.add_section(section)
        self.config.set(section, key, value)

        ctg = open(ConfigConstants.CONFIG_FILE_PATH, FileConstants)
        self.config.write(ctg, space_around_delimiters=False)
        ctg.close()

    def get_products(self):
        sites_list = []
        products = []
        for section in self.config.sections():
            configs = dict(self.config.items(section))
            for c in configs:
                key = c.upper()
                if key in SiteType._value2member_map_:
                    site_type = SiteType(c.upper())
                    site = Site(site_type, configs.get(c))
                    sites_list.append(site)

            products.append(Product(section,
                            configs.get(StringConstants.SPREADSHEET_ID),
                            sites_list))
        return products
