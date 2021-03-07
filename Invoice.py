class Invoice:

    def __init__(self):
        self.items = {}

    def addProduct(self, qnt, price, discount):
        self.items['qnt'] = qnt
        self.items['unit_price'] = price
        self.items['discount'] = discount
        return self.items

    def totalImpurePrice(self, products):
        total_impure_price = 0
        for k, v in products.items():
            total_impure_price += float(v['unit_price']) * int(v['qnt'])
        total_impure_price = round(total_impure_price, 2)
        return total_impure_price

    def totalDiscount(self, products):
        total_discount = 0
        for k, v in products.items():
            total_discount += (int(v['qnt']) * float(v['unit_price'])) * float(v['discount']) /100
        total_discount = round(total_discount, 2)
        self.total_discount = total_discount
        return total_discount

    def totalPurePrice(self, products):
        total_pure_price = self.totalImpurePrice(products) - self.totalDiscount(products)
        return total_pure_price

    # Returns the most expensive single item after discount from the list
    def getMostExpensiveItemAfterDiscount(self, products):
        most_expensive_product = None
        max_price_found = -1
        for key in products:
            product = products[key]
            # product price is equal to the base price * the discounted rate
            #                               base price * 1 - 5 (%)/100
            #                               base price * 1 - .05
            #                               base price * .95
            product_price = product['unit_price'] * (1 - product['discount']/100)
            if product_price > max_price_found:
                max_price_found = product_price
                most_expensive_product = key
        return most_expensive_product

    # Returns the least expensive single item after discount from the list
    def getLeastExpensiveItemAfterDiscount(self, products):
        least_expensive_product = None
        min_price_found = None
        for key in products:
            product = products[key]
            product_price = product['unit_price'] * (1 - product['discount']/100)
            if min_price_found == None or product_price < min_price_found:
                min_price_found = product_price
                least_expensive_product = key
        return least_expensive_product

    def inputAnswer(self, input_value):
        while True:
            userInput = input(input_value)
            if userInput in ['y', 'n']:
                return userInput
            print("y or n! Try again.")

    def inputNumber(self, input_value):
        while True:
            try:
                userInput = float(input(input_value))
            except ValueError:
                print("Not a number! Try again.")
                continue
            else:
                return userInput