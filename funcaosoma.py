import random
a = 10
b = 20

def soma (a, b):
    return a + b

#para exibir
resultado = soma (a, b)
print(f"O resultado da função soma com base nos argumentos definidos nas variáveis a e b é {resultado}")


def subtracao ( a , b):
    subt = (a - b)
    return subt

resultado = subtracao(a,b)
print(resultado)

valores = [1, 2, 3,4,5]

def quadrado(valores):
    quadrados = []
    for x in valores:
         quadrados.append(x**2)
    return quadrados
resultados = quadrado(valores)

for y in resultados:
    print (y)

quantity = 1


def get_determiner(quantity):
    
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word
result = get_determiner(quantity)
for i in result:
    print(i)

def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
        word = random.choice(words)
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
        word = random.choice(words)
        return word
result_noun = get_noun(quantity)
print(result_noun)