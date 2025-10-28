"""MAP e FILTER functions:

Na lição 9 o checkpoint exigia um progrma que substituisse todas as ocorrências de AB em uma lista pelo nome Alberta e contasse quantas vezes o nome "Alberta" aparecesse na lista

Vamos usar mapa e filtro (MAP and FILTER) para resolver:

Example 5:

"""

from typing import Counter


def main():
    lista_de_provincias = ["Alberta", "Ontario", "Prince Edward Island", "Ontario",
        "Quebec", "Saskatchewan", "AB", "Nova Scotia", "Alberta",
        "Northwest Territories", "Saskatchewan", "Nunavut",
        "Nova Scotia", "Prince Edward Island", "Alberta",
        "Nova Scotia", "Prince Edward Island", "Saskatchewan",
        "Nova Scotia", "Newfoundland and Labrador", "Ontario",
        "Ontario", "Ontario", "British Columbia", "Ontario",
        "Nova Scotia", "Prince Edward Island", "Saskatchewan",
        "Newfoundland and Labrador", "Ontario", "Ontario",
        "Manitoba", "British Columbia", "Ontario", "Alberta",
        "Saskatchewan", "Ontario", "Manitoba", "Ontario",
        "New Brunswick", "Yukon", "British Columbia", "Yukon",
        "Newfoundland and Labrador", "Manitoba", "Ontario",
        "Yukon", "British Columbia", "Yukon", "Ontario", "AB",
        "Newfoundland and Labrador", "Nova Scotia", "Yukon",
        "Northwest Territories", "Nunavut", "Yukon", "Nunavut",
        "Ontario", "British Columbia", "AB", "Saskatchewan",
        "Prince Edward Island", "Saskatchewan",
        "Prince Edward Island", "Alberta", "Ontario", "Alberta",
        "Manitoba", "AB", "British Columbia", "Alberta"]

    print("The original list of provinces:")
    print(lista_de_provincias)
    print()

#definir uma função aninhada (nested function) para converter AB para Alberta

    def converte_AB_Alberta(nome_provincia):
        if nome_provincia == "AB":
            nome_provincia = "Alberta"
        return nome_provincia

        #com a função map passar a função criada AB_Alberta

    nova_lista = list(filter(converte_AB_Alberta,lista_de_provincias))
    print("Converted list of provinces")
    print(nova_lista)

    #essa função aminhada retorna True se nome_provincia for "Alberta", de outra forma retorna False:

    def checa_se_é_alberta(nome_provincia):
        return nome_provincia == "Alberta"

        #filtrar uma nova lista para somente armazenar as provincias vindas de Alberta chamando as funcções checa_se_é_alberta e nova lista:

    lista_filtrada = list(map(checa_se_é_alberta, nova_lista))
    print(lista_filtrada)

    contagem = len(lista_filtrada)
    print(contagem)



if __name__ == "__main__":
    main()


# Example 5

def main():
    # Create a list that contains the names of Canadian provinces.
    lista_de_provincias = [
        "Alberta", "Ontario", "Prince Edward Island", "Ontario",
        "Quebec", "Saskatchewan", "AB", "Nova Scotia", "Alberta",
        "Northwest Territories", "Saskatchewan", "Nunavut",
        "Nova Scotia", "Prince Edward Island", "Alberta",
        "Nova Scotia", "Prince Edward Island", "Saskatchewan",
        "Nova Scotia", "Newfoundland and Labrador", "Ontario",
        "Ontario", "Ontario", "British Columbia", "Ontario",
        "Nova Scotia", "Prince Edward Island", "Saskatchewan",
        "Newfoundland and Labrador", "Ontario", "Ontario",
        "Manitoba", "British Columbia", "Ontario", "Alberta",
        "Saskatchewan", "Ontario", "Manitoba", "Ontario",
        "New Brunswick", "Yukon", "British Columbia", "Yukon",
        "Newfoundland and Labrador", "Manitoba", "Ontario",
        "Yukon", "British Columbia", "Yukon", "Ontario", "AB",
        "Newfoundland and Labrador", "Nova Scotia", "Yukon",
        "Northwest Territories", "Nunavut", "Yukon", "Nunavut",
        "Ontario", "British Columbia", "AB", "Saskatchewan",
        "Prince Edward Island", "Saskatchewan",
        "Prince Edward Island", "Alberta", "Ontario", "Alberta",
        "Manitoba", "AB", "British Columbia", "Alberta"
    ]

    # As a debugging aid, print the entire list.
    print("Original list of provinces:")
    print(lista_de_provincias)
    print()

    # Define a nested function that converts AB to Alberta.
    def Muda_AB_para_Alberta(nome_da_provincia):
        if nome_da_provincia == "AB":
            nome_da_provincia = "Alberta"
        return nome_da_provincia


    # Replace all occurrences of "AB" with "Alberta" by
    # calling the map function and passing the ablerta_from_ab
    # function and provinces_list into the map function.
    nova_lista = list(map(Muda_AB_para_Alberta, lista_de_provincias))
    print("List of provinces after AB was changed to Alberta:")
    print(nova_lista)
    print()

    # Define a nested function that returns True if
    # province_name is Alberta and returns False otherwise.
    def checa_se_é_alberta(nome_provincia):
        return nome_provincia == "Alberta"

    # Filter the new list to only those provinces that
    # are "Alberta" by calling the filter function and
    # passing the is_alberta function and new_list.
    lista_filtrada = list(filter(checa_se_é_alberta, nova_lista))
    print("List filtered to Alberta only:")
    print(lista_filtrada)
    print()

    # Because all the elements in filtered_list are
    # "Alberta", we can count how many elements are
    # "Alberta" by simply calling the len function.
    count = len(lista_filtrada)

    print(f"Alberta occurs {count} times in the modified list.")


# Call main to start this program.
if __name__ == "__main__":
    main()