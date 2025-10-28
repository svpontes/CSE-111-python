"""VARIABLE SCOPE 
O escopo de uma varável determina quanto tempo ela deve existir e aonde se usada
existe:
LOCAL ----> É DEFINIDA (UM VALOR ATRIBUIDO) DENTRO DA FUNÇÃO

GLOBA ----> QUANDO É DEFINIDA FORA DE TODAS AS FUNÇÕES

EXEMPLO
"""
g = 25 # ------> essa variável é GLOBAL definida fora de uma função

def main():
    x=1 #-----------> aqui a variável X é   LOCAL porque foi definida dentro de uma função. EXISTE ENQUANTO A FUNÇÃO
        # ESTÁ SENDO EXECUTADA, e em nenhum outro lugar.

#MUITOS PROGRAMADORES ASSUMEM QUE UMA VARIAVEL LOCAL PODE SER USADAS DENTRO DE OUTRAS FUNÇÕES.
# VEJAMOS O Example 3


import math

def main():
    radius = float(input("Enter the radius of a circle: ")) #VARIAVEL "radius" NA FUNÇÃO MAIN
    area = circle_area()
    print(f"area: {area:.1f}")

def circle_area():
    
    # Mistake! There is no variable named radius
    # defined inside this function, so the variable
    # radius cannot be used in this function.
    area = math.pi * radius * radius # VARIÁVEL "radius" NA FUNÇÃO circle_area. ESSA VARIÁVEL NÃO PODE SER USADA COMO SE                              FOSSE DA "main. daí O ERRO CONFORME O SUBLINHADO AMARELO que mostra que essa função                         não está DEFINIDA"
    return area

main()


# UMA MANEIRA DE RERSOLVER O PROBLEMA SERIA O SEGUINTE:

def main():
    radius = float(input("Enter the radius of a circle: ")) #VARIAVEL "radius" NA FUNÇÃO MAIN
    area = circle_area(radius)  #ADICIONAR UM  PARÂMENTRO PARA A A FUNÇÃO "circle_area()" onde
                                # a VARIÁVEL radius=float....recebe um valor e fica dentro de clircle_area(radius)
    print(f"area: {area:.1f}")

# DA FORMA ABAIXO O CODIGO FUNCIONA CORRETAMENTE

# Example 4

import math

def main():
    radius = float(input("Enter the radius of a circle: "))
    area = circle_area(radius)   #AQUI A VARIÁVEL area = O RESULTADO da função "circle_area" CONSIDERANDO           #                              #PARÂMETRO "radius"
    print(f"area: {area:.1f}")

def circle_area(radius):
    area = math.pi * radius * radius
    return area

main()

"""Python PERMITE QUE OS PARÂMETROS DA FUNÇÃO TENHAM VALORES PADRÃO
   SE UM PARÂMETRO TEM UM VALOR PADRÃO, ENTÃO SEU ARGUMENTO CORRESPONDENTE SERÁ OPCIONAL
   VEJAMOS O EXEMPLO ABAIXO"""

# Example 5

# Example 5

import math

def main():
    # Call the arc_length function with only one argument
    # even though the arc_length function has two parameters.
    len1 = arc_length(4.7) #AQUI SOMENTE HÁ O VALOR 4.7 QUE É VALOR QUE O PROGRAMADOR DEFINIU NO PARÂMETRO
                            #LOGO O VALOR A SER DEFINIDO PARA QUE A VARIÁVEL len1 ARMAZENE O RESULTADO DA FUNÇÃO arc_length
                            #  SERÁ O DEFINIDO anteriormente NA FUNÇÃO arc_lenght de 360 (def arc_length(radius, degrees=360)
    print(f"len1: {len1:.1f}")

    # Call the arc_length function again but
    # this time with two arguments.
    len2 = arc_length(4.7, 270) # AQUI FOI PASSADO DOIS ARGUMENTO 4.7 E 270, LOGO A função arc_length já tem valor para 
                                #radius 4.7 e 270º que será considerado no cálculo como segue:
                                #   circunference = 2 * 3.14 * 4.7
                                # length = 29.516(circunference) * 270(argumento) / 360(vaor padrão) = 22.1
    print(f"len2: {len2:.1f}")


#FUNÇÃO COM DOIS PARÂMETROS
# radius não está definido
#MAS "degrees tem um valor de 360 definido"
def arc_length(radius, degrees=360):   #OBSERVE QUE "radius" NÃO TEM UM VALOR PADRÃO DEFINIDO, MAS "degrees" TEM 360
                                    #isso SIGNIFICA QUE QUANDO A FUNÇÃO RODAR ELA PRECISARÁ DE UM VALOR PARA radius
    
    circumference = 2 * math.pi * radius
    length = circumference * degrees / 360
    return length


main()


    #RESUMINDO:
    # UM ARGUMENTO É UM VALOR QUE É PASSADO POR MEIO DE UM PARÂMETRO PARA UMA FUNÇÃO

    #UM PARÂMETRO É UMA VARIÁVEL CUJO VALOR VEM DE FORA DA FUNÇÃO


    """Compute and print the volume of a right circular cone."""

# Import the standard math module so that
# math.pi can be used in this program.

#PROBLEMA RESOLVIDO COMO PROPOSTO NA AULA


def main():
    # Call the cone_volume function to compute
    # the volume of an example cone.
    ex_radius = 2.8
    ex_height = 3.2
    ex_vol = cone_volume(ex_radius, ex_height )

    # Print several lines that describe this program.
    print("This program computes the volume of a right circular cone.")
    print(f"For example, if the radius of a cone is {ex_radius} and")
    print(f"the height is {ex_height}, then the volume is {ex_vol:.1f}")
    print()

    # Get the radius and height of the cone from the user.
    radius = float(input("Please enter the radius of the cone: "))
    height = float(input("Please enter the height of the cone: "))

    # Call the cone_volume function to compute the volume
    # for the radius and height that came from the user.
    vol = cone_volume(radius, height)

    # Print the radius, height, and
    # volume for the user to see.
    print(f"Radius: {radius}")
    print(f"Height: {height}")
    print(f"Volume: {vol:.1f}")


def cone_volume(radius, height):
    """Compute and return the volume of a right circular cone."""
    volume = math.pi * radius ** 2 * height / 3
    return volume


# Start this program by
# calling the main function.
main()

"""""In many countries, food is stored in steel cans (also known as tin cans) that are shaped like cylinders. There are many different sizes of steel cans. The storage efficiency of a can tells us how much a can stores versus how much steel is required to make the can. Some sizes of cans require a lot of steel to store a small amount of food. Other sizes of cans require less steel and store more food. A can size with a large storage efficiency is considered more friendly to the environment than a can size with a small storage efficiency.

The storage efficiency of a steel can is computed by dividing the volume of a can by its surface area.

storage_efficiency = 
volume
surface_area
In other words, the storage efficiency of a can is the space inside the can divided by the amount of steel required to make the can. The formulas for the volume and surface area of a cylinder are:

volume = π radius2 height
surface_area = 2π radius (radius + height)
π is the constant PI, the ratio of the circumference of a circle divided by its diameter (use math.pi)
radius is the radius of the cylinder
height is the height of the cylinder"""

