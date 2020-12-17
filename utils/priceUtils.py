class PriceUtils:

    @staticmethod
    def get_percentage_price_variation(old_value, new_value):
        variance = new_value - old_value
        return (variance / old_value) * 100

    def remove_currency_from_price(price):
        return price.replace("R$", "")
