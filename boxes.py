import math

number_items = int(input("Enter the number of items "))

number_items_per_box = int(input("Enter the number of items per box "))

num_box = (number_items / number_items_per_box)

print(f"For {number_items} items, fit in {number_items_per_box} per box, you will need {math.ceil(num_box)} boxes")