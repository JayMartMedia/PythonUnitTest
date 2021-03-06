from Invoice import Invoice

products = {}
total_amount = 0
repeat = ''
while True:
    product = input('What is your product : ')
    unit_price = Invoice().inputNumber("Please enter unit price :")
    qnt = Invoice().inputNumber("Please enter quantity of product : ")
    discount = Invoice().inputNumber("Discount percent (%) : ")
    repeat = Invoice().inputAnswer("Another product? (y,n) : ")
    result = Invoice().addProduct(qnt, unit_price, discount)
    products[product] = result
    if repeat == "n":
        break

total_amount = Invoice().totalPurePrice(products)
most_expensive_item = Invoice().getMostExpensiveItemAfterDiscount(products)

print("Your total pure price is: ", total_amount)
print("Your most expensive item is: ", most_expensive_item)