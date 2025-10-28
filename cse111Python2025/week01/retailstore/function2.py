from datetime import datetime

#global variables
DISCOUNT = 0.1
TAX = 0.06
AMOUNT_TO_GET_DISCOUNT = 50

#discount based on day of the week (tuesday and wednesday)
day_of_week = datetime.now().strftime("%A").lower()

def calcPurchaseTotal():
    item_price = 0
    item_quant = 1
    total = 0
    missing_amount = 0
    print("\nPlease Provide item and price to calculate total! To finish type 0\n")
    while item_quant != 0:
        
        item_price = float (input("What is the item price?: "))
        item_quant= float (input("How many of this item do you want: "))
        total += item_price * item_quant
        
        if (item_quant == 0) or (item_price == 0):
            break
    if  total < AMOUNT_TO_GET_DISCOUNT:
            missing_amount = AMOUNT_TO_GET_DISCOUNT - total
            answer = input((f"Your total is ${total:.2f} - do not qualify for 10% discount\nit is missing ${missing_amount} \nDo you want to add items? (Y/N)")).lower()  
            if answer == "y":
                 return calcPurchaseTotal()
            else:
                print("Okay, we'll finalize your purchase.")       
    
    return total

#function to apply discount
def apply_discount(total: float):
    #variables 
    discount_aplied = False
    total_discount = 0
    tax_paid = 0
    t_payment = 0

    #verify if the day of week allow discount and the amount purchesed
    if total >= AMOUNT_TO_GET_DISCOUNT and (day_of_week == "tuesday" or day_of_week == "wednesday"):
        
        discount_aplied = True
        
    else:
       ""     
    
    if discount_aplied:

        total_discount = total * DISCOUNT
        total_after_discount = total - total_discount
        tax_paid = total_after_discount * TAX
        t_payment = total_after_discount + tax_paid 
    else:
                        
        print("\n No additional items added.")
        tax_paid = total * TAX
        t_payment = total + tax_paid     
  

# show receipt
    print("\n------------- Receipt ----------------\n")
    print(f"Subtotal:         ${total:.2f}")
    print(f"Discount:         ${total_discount:.2f}")
    print(f"Tax:              ${tax_paid:.2f}")
    print(f"Total payment:    ${t_payment:.2f}")
    print()
