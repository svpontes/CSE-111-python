# Example 3

import csv

# Indexar as colunas
# no arquivo  dentists.csv
COMPANY_NAME_INDEX = 0
NUM_EMPLOYEES_INDEX = 3
NUM_PATIENTS_INDEX = 4


def main():
    # Essa função abre dentists.csv e armazena uma refrencia do arquivo aberto na variável dentist_file.
    with open("dentists.csv", "rt") as dentists_file:

        # Usa o módulo csvpara criar um leitor        # objecto que irá ler apartir do arquivo aberto.
        reader = csv.reader(dentists_file)

        #pular a primeira linha do do arquivo indo para a próxima next.
        next(reader)

        running_max = 0
        most_office = None

        # Le uma linha por vez .
        # O objeto reader retorna cada linha como uma lista
        for row in reader:

            #para cada linha corrente retornar os valores nas coluns indexadas, 0, 3 e 4
            company = row[COMPANY_NAME_INDEX]
            num_employees = int(row[NUM_EMPLOYEES_INDEX])
            num_patients = int(row[NUM_PATIENTS_INDEX])

            # calcula o numero de pacientes por cada empregado do consultorio dentista
            patients_per_employee = num_patients / num_employees

            # Se o escritorio que esta a ser lido tem mais mais pascientes por empregado entao o o máximo atribui running_max
            # e most_office para ser o escritorio corrente (atual) mostrando assim o que tem mais.
            if patients_per_employee > running_max:
                running_max = patients_per_employee
                most_office = company

    # Print the results for the user to see.
    print(f"{most_office} has {running_max:.1f} patients per employee")


# Call main to start this program.
if __name__ == "__main__":
    main()