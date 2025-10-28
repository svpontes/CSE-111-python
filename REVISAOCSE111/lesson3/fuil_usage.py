def main():

    start_point = float(input("Enter the value: "))
    end_point = float(input("Enter the value: "))
    amount_of_gallons = float(input("Enter the value: "))

    mpg = miles_per_gallon(start_point, end_point, amount_of_gallons)

    lp100k = lp100k_from_mpg(mpg)
    print(f"{mpg:.1f} miles per gallon")
    print(f"{lp100k:.1f} liters per 100 kilometers")

def miles_per_gallon(start_point, end_point, amount_of_gallons):

    mpg = abs(end_point - start_point)/amount_of_gallons
    return mpg

def lp100k_from_mpg(mpg):

    lp100k =  235.215 / mpg
    return lp100k

if __name__ == "__main__":
    main()