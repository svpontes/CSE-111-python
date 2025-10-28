import math
"""maneiras de escolher k itens de n itens sem repetição e sem ordem. Basicamente, é avaliado como n! / (k! * (n – k)!) quando k n. Também é conhecido como coeficiente binomial porque é equivalente ao coeficiente do termo k-ésimo na expansão polinomial da expressão (1 + x) n """

n = 10
k = 2

nCk = math.comb(n, k)

print(nCk)