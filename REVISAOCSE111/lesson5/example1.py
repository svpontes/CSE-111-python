#write a pytest function



from _pytest.config import main

def main():

    fahr = -28.5

    cels = cels_from_fahr(fahr)

    print(cels)

def cels_from_fahr(fahr):
    #this function convert a temperature in fahrenheit to celsius and return CELSIUS temperature.

    cels = (fahr -32) *5/9
    return cels

if __name__ == "__main__":
    main()