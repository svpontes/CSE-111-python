from datetime import datetime

# Constantes globais
DISCOUNT = 0.1
TAX = 0.05
AMOUNT_TO_GET_DISCOUNT = 50

# Obter o dia da semana atual
day_of_week = datetime.now().strftime("%A").lower()  # 'tuesday', 'wednesday', etc.
print(f"Today is: {day_of_week}")

def apply_discount(total):
    """Aplica desconto e imposto, dependendo do dia da semana e valor total."""
    
    # Garante que as variáveis existam em todos os cenários
    total_discount = 0
    tax_paid = 0
    t_payment = 0

    # Verifica se é dia de desconto e se o valor já é suficiente
    if (day_of_week == "tuesday" or day_of_week == "wednesday") and total >= AMOUNT_TO_GET_DISCOUNT:
       

        # Se o valor ainda for menor que o necessário para desconto
        if total < AMOUNT_TO_GET_DISCOUNT:
            
            while total < AMOUNT_TO_GET_DISCOUNT:
                missing = AMOUNT_TO_GET_DISCOUNT - total
                answer = input(f"Your total (${total:.2f}) does not qualify for the 10% discount. "
                            f"Would you like to add more items? You need ${missing:.2f} more (Y/N): ").lower()
                
                if answer == "y":
                    amount_added = float(input("Enter the amount of additional items: "))
                    total += amount_added
                else:
                    print("\nNo additional items added.")
                    break  # sai do loop se o cliente não quiser adicionar mais
            
            # Após o loop, verifica novamente se atingiu o desconto
                if (day_of_week == "tuesday" or day_of_week == "wednesday") and total >= AMOUNT_TO_GET_DISCOUNT:
                
                    tax_paid = total * TAX
                    t_payment = total + tax_paid

        # Caso padrão — compras já qualificadas sem desconto (outros dias)
        else:
            tax_paid = total * TAX
            t_payment = total + tax_paid
            print("\nThanks for your purchase!")
    
    total_discount = total * DISCOUNT
    total_after_discount = total - total_discount
    tax_paid = total_after_discount * TAX
    t_payment = total_after_discount + tax_paid
    
   
    # Exibe o recibo
    print("\n------------- Receipt ----------------")
    print(f"Subtotal:         ${total:.2f}")
    print(f"Discount:         ${total_discount:.2f}")
    print(f"Tax:              ${tax_paid:.2f}")
    print(f"Total payment:    ${t_payment:.2f}")