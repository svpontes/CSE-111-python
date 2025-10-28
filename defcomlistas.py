def dobra(lst):
    posicao = 0
    while posicao < len(lst):
        lst[posicao]*=2
        posicao+=1


valores = [1,2,3,4,5]
dobra(valores)
print(valores)