def calculateTax(price, tax_rate):
    global my_price
    total = price + (price * tax_rate)
    my_price = 10000
    print "my_price (inside function) = ", my_price
    return total

my_price = float(raw_input ("Enter a price: "))

totalPrice = calculateTax(my_price, 0.06)
print "price = ", my_price, " Total price = ", totalPrice
print "my_price (outside function) = ", my_price

