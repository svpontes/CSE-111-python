"""
Exemplo : sorting (classificando) uma lista composta

Python built-in higher-order function sorted aceita uma lsita como argumento e retorna uma nova lista classificada. Chamando a função sorted direto para uma lista simples como uma lsita de strings ou uma lsita de números

Vejamos o exemplo 6

"""

def main():

    countries = ["Canada", "France", "Ghana",  "Brazil", "Japan"]
    print(countries)

    #classificar a lista sorted the lsita

    sorted_list = sorted(countries)
    print(sorted_list)

# classificar uma lista composta

    countries_list = [
# [country_name, land_area, population, gdp_per_capita]
        ["Mexico", 1972550, 126014024, 21362],
        ["France",  640679,  67399000, 45454],
        ["Ghana",   239567,  31072940,  7343],
        ["Brazil", 8515767, 210147125, 14563],
        ["Japan",   377975, 125480000, 41634]
    ]
# o elemento que queremos utilizar como filtro chamasse key element (elemento chave). Para usar  função sorted para uma lista composta precisamos definir qual será a chave que faremos passando uma pequena função como um argumento dentro da funbção sorted.

#Essa pequena função é chamada de key function e extrai o element key de uma lista. Vejamos o exemplo 7 
    print("Lista original:")
    print(countries_list)

    for country in countries_list:
        print(country)
        print()

    #vamos utilizar uma função lambda como função chave key. Esssa função extrai  os dados da população dos paises. Population vai ser a chave (key) para countries_list 
    
    população_index = 2
    função_população = lambda country: country[população_index]

    #classificar a lista pela população:

    sorted_list = sorted(countries_list, key=função_população)

    print("Lista de países pela população")
    for country in sorted_list:
        print(country)

if __name__ == "__main__":
    main()

       

