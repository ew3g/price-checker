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


#c = ConfigProperties()

#print(c.getValue('teste'))
#c.save_config_value('teste3', '123445')
