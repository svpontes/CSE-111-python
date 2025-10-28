import math

num_items = int(input("Number of manufactered items: "))

num_pack = int(input("Enter the number of items per box: "))

packing_calc = math.ceil(num_items /num_pack)

print(f"Itens per box: {packing_calc}")