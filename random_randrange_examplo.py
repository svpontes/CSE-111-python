import random

r = random.randrange(5)

numbers = int(input("digite um número de 0 a 30: "))


if numbers == r:
    print("acertou")
else:
    print("errou")
