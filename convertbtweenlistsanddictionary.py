#é possivel converter 2 listas em um dicionario usando as funções internas dopython zip e dic.
#o conteudo da primeira lista torna-se  key (chave) e o segundo torna-se os valores (value)
#IMPORTANTE
#AS DUAS LISTAS DEVEM TER O MESMO TAMANHO E OS ELEMENTOS DA PRIMEIRA LISTA DEVEM SER UNICOS E DIFERENTES PORQUE UM DICIONARIO NAO PODE USAR KEYS DIFERENTES

#TAMBEM É POSSIVEL CONVERTER DUAS LISTAS EM DICIONARIO USANDO key e value métodos. exemplos abaixo:


def main():
    numbers = ["42-039-4736", "61-252-3698", "45-587-963"]

    names = ["Sergio Pontes", "Tatiana Pontes", "Murilo Pontes"]

    student_dictionary = dict(zip(numbers, names))

    print(student_dictionary)

if __name__ == "__main__":
    main()