from model.product import Product

class ConfigProperties:

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


#c = ConfigProperties()

#print(c.getValue('teste'))
#c.save_config_value('teste3', '123445')
