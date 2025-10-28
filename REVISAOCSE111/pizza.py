number_of_toppings = int(input("How many toppings? "))

price_per_top = 1.45
price = 10.95

tooping_cost = number_of_toppings * price_per_top

total = price + tooping_cost

print(f"the price is: {total:.2f}")