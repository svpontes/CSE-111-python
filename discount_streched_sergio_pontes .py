"""Problem Statement
You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store's slowest sales days. On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, the store will discount the customer's subtotal by 10%.

Assignment
Write a Python program named discount.py that gets a customer's subtotal as input and gets the current day of the week from your computer's clock. Your program must not ask the user to enter the day of the week. Instead, it must get the day of the week from your computer's clock.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. Your program must print the discount amount if applicable, the sales tax amount, and the total amount due."""

from datetime import datetime

date = datetime.today().strftime("%A, %B %D, %Y")#Return Computer Date where %A represents the Day of the Week
print(date)
print()
subtotal = float(input("What is the Subtotal? U$ "))
print()
disc = 0.1  
tax = 0.06
dayofweek = datetime.today().strftime("%A") #Return the day of the week
promotion = 50 #Base amount to get a discount. Used To calculate how much is missing from the Amout entered by the client 
keep_byuing = True 
total_with_disc = subtotal - subtotal * disc

if (dayofweek == "Monday") or (dayofweek == "Tuesday") and subtotal <=49.99:
    print(f" Your subtotal is U$ {subtotal:.2f}, to get a 10% discount is missing U$ {promotion- subtotal}\n")
    print()
    keep_byuing = input("Would you like to buy anything else? Y or N ").upper()#IF client wants to complete his order to get a discount Y, IF not N goes to ELSE
    print()

if keep_byuing == "Y": 
    new_subtotal = float(input("What is the subtotal? U$ "))
    print()
    print(f"You place a new order of U$ {new_subtotal:.2f}\n\nThe new subtotal is U$ {subtotal + new_subtotal:.2f}\n\nYour discount is U$ {(subtotal+new_subtotal)*(disc):.2f}\n\nYour Tax is U$ {((subtotal+new_subtotal)-((subtotal+new_subtotal)*disc))*tax:.2f}\n\nYour TOTAL is U$ {((subtotal+new_subtotal)-((subtotal+new_subtotal)*disc))*tax + ((subtotal+new_subtotal)-((subtotal+new_subtotal)*disc)):.2f}\n")

elif (dayofweek == "Monday") or (dayofweek == "Tuesday") and subtotal >=50:
        print(f"Your subtotal is U$ {subtotal:.2f}\n\nYour Discount is U$ {subtotal-total_with_disc:.2f}\n\nYour Tax is U$ {total_with_disc*tax:.2f}\n\nYour TOTAL is U$ {(total_with_disc*tax)+(total_with_disc):.2f}\n")

else:
    print(f"Your subtotal is U$ {subtotal:.2f}\n\nPlus Tax the TOTAL is U$ {subtotal*tax + subtotal:.2f}\n")