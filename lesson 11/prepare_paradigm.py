"""
Um paradigima é uma forma de pensar  ou uma forma de ver o mundo.

Há quatro tipos de paradigmas para programar um computador:

PROCEDURAL
DECLARATIVO
FUNCIONAL
ORIENTADO A OBJETO

Procedural --> foca no processo ou passos para completar a tarefa.

Declarativa --> Não foca no processo ou passos. Foca no que você quer do computador ou seja no resultado. A programação em SQL- Structured Query Language é um bom exemplo de programação declarativa. Assim você declara através do código para dizer ao computador o quer você quer de resultado e não os passos que o computador deve seguir para alcançar tais resultados.

Funcional --> Foca em funções e evita estado compartilhado, estado de mutação e efeitos colaterais.Há muitos conceitos e técnicas que fazem parte da programação funcional. No entanto, nessa lição vamos focar em 3:

1 - Podemos passar um função em outra função
2 - Uma função aniinhada é um a função definida      dentro  de outra função.
3 - Uma função lambda é uma pequena função anônima.

CONCEITOS:

A linguagem de programação pytho permite passar uma função como um argumento dentro de outra função. Uma função que aceita outra função em seus parâmetros é conhecida como higer-order function. 
Higher-Order Function são usadas frequentemente para processar uma lista.

considere o exemplo abaixo onde a função Higher-Order function não é utilizada, ao contrário utiliza um for loop para converter uma lista de temperaturas de fahrenheit para celsius .

exemplo 1
"""
def main():
    fahrenheit_temperatures = [72, 65, 71, 75, 82, 87, 68]

    #imprime as temperaturas:
    print(fahrenheit_temperatures)

    #criar uma lista vazia para converter cada valor de fahrenheit para celsius e armazenar os valores em celsius em uma lista chamada:celsius_tempertures

    celsius_temperatures = []
    for fahr in fahrenheit_temperatures:
        celsius = celsius_from_fahrenheit(fahr)
        celsius_temperatures.append(celsius) #append acrescenta a temperatura convertida para uma nova lista. 

        print(f"Celsius: {celsius}")

"""
a função celsius_from_fahrenheit  tem como para metro (fahr). essa função convert a tempreratura de fahrenheit para celsius 
"""
def celsius_from_fahrenheit(fahr):
    celsius = (fahr -32)*5/9
    return round(celsius, 1)

if __name__ == "__main__":
    main()

"""
Podemos utilizar as funções interna de ordem superior incorporadas no python (built-in) para realizar o mesmo processo do exemplo 1. Utilizamos a função map. A função map aceita uma função e uma lsta como argumentos e contem um loop interno. Logo ao utilizar a função map não será preciso fazer um loop.  

veja o exemplo 2:
"""
def main():

    fahrenheit_list = [72, 65, 71, 75, 82, 87, 68]
    #cels_temp = list(map(cels_from_fahren, fahrenheit)) list é uma classe e (map tambem é uma classe. Dentro de map tem um loop que vai pegar a função cels_from_fahr dentro da função map, assim a função map vai chamar cels_from_fahr para cada ellemento em fahr_temp_list
    
    cels_temp = list(map(cels_from_fahren,fahrenheit_list))
    print(fahrenheit_list)

def cels_from_fahren(fahr):
    cels = (fahr-32)*5/9
    return round(cels,1)
    
if __name__ == "__main__":
    main()
# Outras funções higher-order no python : sorted, filter e muitas outras encontradas em functools module.

"""
NESTED Functions

Função aninhada é uma função que é definida dentro de outra função e é util quando desejamos separar uma função maior em funções menores e será chamada somente pela função que a contem, ou seja a função onde ela está aninhada.  

veja o exemplo 3:
"""
def main():

    def converte_celsius_de_fahrenheit(fahrenheit):
        celsius = (fahrenheit-32)*5/9
        return round(celsius, 1)

    fahrenheit_list = [72, 65, 71, 75, 82, 87, 68]

    celsius_temperatura = list(map(celsius_from_fahrenheit, fahrenheit_list))

    print(celsius_temperatura)
        

if __name__ == "__main__":
    main()

"""
LAMBDA Functions

é uma pequena função anônima, ou seja sem nome. Possue sempre uma expressão porque o python restringe para que assim seja.    

veja o exemplo 4:
"""

def main():

    lista_temperatura_fahrenheit = [72, 65, 75, 71, 82, 87, 68]

    print(lista_temperatura_fahrenheit)
    
    celsius_de_fahrenheit = lambda fahr: round((fahr -32) *5/9, 1)


    celsius_temperatura = list(map(celsius_de_fahrenheit, lista_temperatura_fahrenheit))

    print(celsius_temperatura)

"""
LAMBDA Functions

outro exemplo de lambda dentro da estrutura lis(map    

veja o exemplo 5:
"""
#convert cada temperatura fahrenheit para celsius e armazena em uma lsita chamada cels_temps

#esse é um template para usar a função lanbda
def main():
    
    list_to_convert = [72, 65]

    cels_temps = list(map(lambda fahr: round((fahr -32)*5/9, 1),list_to_convert))
    print(cels_temps)

if __name__ == "__main__":
    main()


