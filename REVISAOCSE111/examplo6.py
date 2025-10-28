#get a cost of an item from the user:

cost= float(input("enter price cost: "))

if cost < 100:
    rate = 0.10
elif cost < 250:
    rate = 0.15
elif cost < 400:
    rate = 0.18
else:
    rate = 0.20

discount = cost * rate
cost -= discount

print(f"After discount: {cost:.2f}")