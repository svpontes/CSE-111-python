from function2 import apply_discount
from function2 import calcPurchaseTotal

def main():

    #determine the subtotal
        
    subtotal = calcPurchaseTotal()
    apply_discount(subtotal)
    
if __name__ == "__main__":
    main()