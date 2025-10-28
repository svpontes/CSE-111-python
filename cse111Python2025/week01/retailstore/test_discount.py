#test discount program
import pytest

from function2 import calcPurchaseTotal

#input and expected outputs for testing 
"""> python discount.py
Please enter the subtotal: 42.75
Sales tax amount: 2.56
Total: 45.31
> python discount.py
Please enter the subtotal: 55.20
Sales tax amount: 3.31
Total: 58.51"""

def test_calcPurchaseTotal(monkeypatch):

    #testing total less than AMOUNT_TO_GET_DISCOUNT, user do not add more items
    #simulate user inputs
    inputs = iter([
        "20", "1", #item price, item quantity
        "0", "0",  #finish purchase
        "n"        #do not add more items
    ])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    total = calcPurchaseTotal()
    assert total == 20

def test_calc_total_add_more(monkeypatch):
    """Testa subtotal menor que AMOUNT_TO_GET_DISCOUNT, usuário adiciona mais itens."""
    # Inputs simulados:
    inputs = iter([
        "20", "1",   # item 1
        "0", "0",    # encerra compra inicial
        "y",         # usuário quer adicionar mais
        "40", "1",   # adiciona novo item
        "0", "0",    # encerra compra
        "n"          # não adiciona mais
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    total = calcPurchaseTotal()
    assert total == 60  # 20 + 40