def main():

    camaroDictionary = {

        "make" : "Chrevolet",
        "model" : "Camaro",
        "year" : "1971",
        "engine" : "350 CID",
        "Transmission" : "550 Turboglide",
        "carburetor" : "Carter 650 AFB Qadrojet" 
        }

    for key in camaroDictionary:
        print(key + ": " + camaroDictionary[key])


if __name__ == "__main__":
    main()