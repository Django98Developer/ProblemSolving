def mango(quantity, price):
    return (quantity-quantity/3)*price


q = float(input("Enter the quantity of mango :"))
p = float(input("Enter the price of mango :"))
print(mango(q, p))
