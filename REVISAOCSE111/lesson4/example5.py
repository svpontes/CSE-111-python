import math

#Default parameter values and optional arguments

def main():
    #chamando a função arc_length com somente UM ARGUMENTO
    len1 = arc_length(4.7) #quando não definimos o 2º argumento logo será 360
    #chamando a função arc_length com DOIS ARGUMENTOS
    len2 = arc_length(4.7, 270) # quando definimos um argumento ele passa a ser o padrão 
    
    print(f"the result for len1 is {len1:.2f} and len2 is {len2:.2f} ")

#definir uma função com 2 parametros. O segundo parametro tem um valor padrão de 360

def arc_length(radius, degrees=360):

    circumference = 2 * math.pi * radius

    length = circumference * degrees /360

    return length  

if __name__=="__main__":
    main()  