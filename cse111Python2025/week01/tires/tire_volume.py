from math import pi
from datetime import datetime
import os
import sys

#tax
tax = 0.05
total = 0
discount = 0.1
script_dir = os.path.dirname(os.path.abspath(__file__))

#Price list of inventory tires at priceList.txt and its path
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, "priceList.txt")

with open(file_path, "r", encoding="utf-8") as file:
    price_list = file.readlines()


current_date_time = datetime.now()
current_date_time_os = f"{current_date_time:%Y-%m-%d %H:%M}"
print(f"{current_date_time:%Y-%m-%d}")


#The size of a car tire in the United States is represented with three numbers like this: 205/60R15. 
t_width = int(input("What is the tire width? Please provide milimeters measure! "))
t_a_ratio = int(input("What is the tire aspect ratio ? "))
t_diameter = int(input("What is the  tire diameter? Please provide inches measure ? "))

#volume calc
t_volume = (pi*t_width**2*t_a_ratio*(t_width*t_a_ratio+2540*t_diameter)/10000000000)

print()
print(f"The volume of the tire you choose is {t_volume:.2f} liters")
print()

#checking prices from price_list.txt
tires = []
for line in price_list:
    width, aspect, rim, price = line.strip().split(',')
    tires.append({
        "width": int(width),
        "aspect": int(aspect),
        "rim": int(rim),
        "price": float(price)
    })

#after get the volume from client check if ther is in our list
tire_inTheList = False
for tire in tires:
    if tire["width"] == t_width and tire["aspect"] == t_a_ratio and tire["rim"] == t_diameter:
        print(f"The price for tire {t_width}/{t_a_ratio}R{t_diameter} is ${tire['price']:.2f}")
        found = True
        break

# Selling step
user_answer_for_buying = input("Would you like to buy it? Y/N: ").lower()

if user_answer_for_buying == "y":
    tire_quantity = int(input("How many tires? (Buying 4 tires gives FREE installation and 10% OFF): "))

    if tire_quantity > 0:
        # Register client
        client_number = input("Please provide your social security number: ")
        client_f_name = input("Your first name, please!: ")
        client_l_name = input("Your last name, please!: ")

        # Subtotal calc
        subtotal = tire['price'] * tire_quantity

        # Applied discount if buying 4 tires
        if tire_quantity == 4:
            applied_discount = subtotal * discount
            subtotal -= applied_discount
            print("\nYou win FREE installation and 10% OFF your purchase! Congratulations!")
        else:
            applied_discount = 0

        # Tax and total calc
        tax_paid = subtotal * tax
        total = subtotal + tax_paid

        # Print receipt
        print("\n---------- RECEIPT ----------")
        print(f"Date: {current_date_time_os}")
        print(f"Item: Tire {t_width}/{t_a_ratio}R{t_diameter}")
        print(f"Quantity: {tire_quantity}")
        print(f"Unit Price: ${tire['price']:.2f}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Discount: -${applied_discount:.2f}")
        print(f"Tax (5%): +${tax_paid:.2f}")
        print(f"TOTAL after tax: ${total:.2f}")
        print("-----------------------------\n")

        # Append data to sales.txt
        
        sales_file_path = os.path.join(script_dir, "sales.txt")
        with open(sales_file_path, "at") as sales_file:
            line_to_append = (
                f"\nDate: {current_date_time_os}"
                f"\nClient Number: {client_number}"
                f"\nClient Name: {client_f_name} {client_l_name}"
                f"\nItem: Tire {t_width}/{t_a_ratio}R{t_diameter}"
                f"\nQuantity: {tire_quantity}"
                f"\nAmount spent: ${subtotal:.2f}"
            )
            print(line_to_append, file=sales_file)

            print("\nSales registered at sales.txt")

    else:
        print("Invalid quantity. No purchase registered.")

else:
    print("No purchase at this time. Thanks!")



#code introduced just to make sure volumes.txt would be created and saved in my tires folder
#obtain the full path where __file__ point to volumes.txt
file_path = os.path.join(script_dir, "volumes.txt")
#Append data in a text file
with open(file_path, "at") as volumes_file:

    line_to_append = f"Date: {current_date_time_os} \nWidth: {t_width}, Aspect Ratio: {t_a_ratio}, Diameter: {t_diameter}, Volume: {t_volume:.2f}"

    print(line_to_append, file=volumes_file)

print("\nTire Volumes registered at volumes.txt")

