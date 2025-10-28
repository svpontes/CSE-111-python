from datetime import datetime

#str string f (formatada) %A dia da semana %B mÊs %

date = datetime.today().strftime("%A, %B %D, %Y")
#print(date)

day_of_week = datetime.today().strftime("%A")

print(day_of_week)

discount = 0.10
subtotal = 50
tax = 0.05

total_purchase = float(input("enter the total purchase value: "))
print()
if day_of_week == "wednesday" or "friday" and total_purchase >= subtotal:
    
    purchase_discount = total_purchase*discount
    print(f"the purchase discount is {purchase_discount}")
    print()
    tax_calc = total_purchase * tax
    print(f"You tax is: {tax_calc}")
    total_pay = total_purchase - tax_calc - purchase_discount
    print()
    print(f"You pay after tax and discount: {total_pay}")
    print()

elif day_of_week == "wednesday" or "friday" and total_purchase < subtotal:

    amount_to_get_discount = subtotal - total_purchase
    print()
    print(f" Your purchase amount is: {total_purchase:.2f}U$. Complete with another purchase in the value of   {amount_to_get_discount:.2f} and get a discount of 10%")
    print()
    add_purchase_question =input("Would like to add anything else? Y(yes) or N (no) ")
    print()

    if add_purchase_question.lower() == "y":
        add_purchase_amount = float(input("Enter the total: "))

        new_total = total_purchase + add_purchase_amount
        print()
        print(f"The new total is: {new_total}")
        tax_calc = new_total*tax
        print()
        print(f"Tax amount is :{tax_calc}")
        new_total_discount = (new_total-tax_calc) * discount
        print()

        print(f"Your discount is: {new_total_discount}")
        print()
    else:
       tax_calc = total_purchase*tax
       total_pay = total_purchase + tax_calc
    print(f"Your total plus tax is: {total_pay}")

else:
    tax_calc = total_purchase*tax
    total_pay = total_purchase + tax_calc
    print(f"Your total plus tax is: {total_pay}")