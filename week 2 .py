# let's build a simple calculator
price = float(input("how much does energy drink cost?"))
quantity = int(input("how many energy drinks do you want to buy?"))

total= price * quantity

# let's print the total cost
print(f"energy drink cost: ${price:.2f}")
print(f"the number of energy drinks you want to buy is {quantity}")
print(f"the total price of energy drunk you want to buy is ksh{total:.2f}")