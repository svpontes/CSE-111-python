city_list = ["alberta", "nunavut", "yukon"]
tax_average = 0.05
ontario = 0.13

total = float(input("What is the total: "))
province = input("What is the province you live in? ")

if province.lower() in city_list:       
    tax_amount = total * tax_average
else:
    tax_amount = total * ontario    

print(f"The tax amount for the {total} in the province of {province} is {tax_amount} ")