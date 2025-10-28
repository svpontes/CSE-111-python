def main():
    sum = 0

    for _ in range(10):
        number= float(input("please enter a number: "))
        if number ==0:
            break
        sum+= number

    print(f"sum: {sum}")

if __name__ == "__main__":

    main()