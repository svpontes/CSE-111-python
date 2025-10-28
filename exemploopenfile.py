pneus = [({"tire": "2056015", "price": "39.99"}),
            ({"tire": "2056016", "price": "39.99"}),
            ({"tire": "2056017", "price": "39.99"}),
            ({"tire": "2056018", "price": "39.99"}),
            ({"tire": "2056019", "price": "39.99"}),
            ({"tire": "2056020", "price": "39.99"}),
            ({"tire": "2056022", "price": "39.99"}),
            ({"tire": "2056025", "price": "39.99"}),
            ({"tire": "2056030", "price": "39.99"}),]
contador = 0
for pneu in pneus:
    contador += 1
    if pneu ["price"] == "39.99":
        continue
        print(pneu["price"], "Custa", pneu["tire"])
        break 
