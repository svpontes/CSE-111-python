# Example 2

import csv


def main():
    # Index das colunas
    # do arquivo de texto dentists.csv 
    COMPANY_NAME_INDEX = 0
    ADDRESS_INDEX = 1
    PHONE_NUMBER_INDEX = 2
    PATIENTS_INDEX = 3

    #variavel = função ("filename", key a chave que defini foi o numero do telefone porque ão tem igual são unicos)
    dentists = read_dict("dentists.csv", PHONE_NUMBER_INDEX)

    # Print the dentists dictionary.
    print(dentists)


def read_dict(filename, key_column_index):
    """lÊ o arquivo e retorna como um dicionario

    Parametros(filename, key_column_index):
        filename: o nome do arquivo CSV a ser lido.
        key_column_index: o indexador da coluna a ser usado como CHAVE (KEY) DO dicionario
        
        Retorna : um dicionario que com o conteudo do arquivo csv dentist
    
    """
    # variavel recebe um dicionario vazio para receber o CSV file.
    dictionary = {}

    # abre o arquivo csv para leitura e armazena sua referencia 
    # abre o arquivo em uma variavel chamada csv_file
    with open(filename, "rt") as csv_file:

        # Usa o csv modulo para criar uma objeto de leitura
        # que lerá o arquivo aberto na variavel csv_file
        reader = csv.reader(csv_file)

        # A primeira linha do arquivo csv dentist contem uma coluna e somente tras o cabeçalho sem armazenar de fato o que precisamos
        # para pular essa linha usamos a função next() dentro do parenteses a variavel criada para ler o arquivo aberto (reader)
        next(reader)

        # lê uma linha do arquivo por vez
        # o reader retorna cada linha como uma lista.
        for row in reader:

            # da presente linha recuperar dados (mostrar dados), retrieve the data
            # da coluna que contem a chave.
            key = row[key_column_index]

            # Armazena os dados da linha em um dicionario
            dictionary[key] = row

    # Return the dictionary.
    return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()