from datetime import datetime
def main():
    genero = input("Qual o seu gênero: M ou F ")
    data_nasc = input("Qual sua data de nacimento: DD-MM-AAAA ")
    peso = float(input("Qual o seu peso em kilos: "))
    altura = float(input("Qual a sua altura em  centimetros: "))
    
    kg = kg_from_lb(peso)
    
    cm = cm_from_inch(altura)
    
    converte_kg_pouds = peso / 0.45359237
   
    converte_cm_inches = altura * 2.54
    
    idade = calcula_idade(data_nasc)
    
    bmi = body_mass_index(kg, cm)
    
    bmr = basal_metab_rate(genero, peso, altura, idade)



    print(f"Você tem {idade}")
    print(f"Dados inseridos:\nGenero: {genero.upper()}\nData de Nascimento: {data_nasc}\nPeso atual: {peso}Kilos\nAltura: {altura} centimetros")
    print(f"você pesa {peso} kilos ou {converte_kg_pouds:.2f} pounds")
    print(f"você tem {altura} centimetros ou {converte_cm_inches:.2f} inches de altura")
    print(f"Body mass index: {bmi:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr:.0f}")

def calcula_idade(nascimento):
    data_nascimento = datetime.strptime(nascimento, "%d-%m-%Y")
    hoje = datetime.now()

    anos = hoje.year - data_nascimento.year

    if data_nascimento.month > hoje.month or \
        (data_nascimento.month == hoje.month and data_nascimento.day > hoje.day):
        anos-=1
    return anos

def kg_from_lb(lb):
    kg = lb * 0.45359237
    return kg

def cm_from_inch(inch):
    cm = inch * 2.54
    return cm

def body_mass_index(peso, altura):
    bmi = peso / (altura**2) * 10000
    return bmi

def basal_metab_rate(genero, peso, altura, idade):
    if genero.upper() == "F":
        bmr = 447.593 + 9.247 * peso + 3.098 * altura - 4.330 * idade
        return bmr
    else:
        bmr = 88.366 + 13.39 * peso + 4.799 * altura - 5.677 * idade

        return bmr
main()
