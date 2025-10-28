""""valores = []
for count in range(0,4):
    valores.append(int(input("Entre o valor: ")))

for v in enumerate (valores):
    print(f"A lista contem os valores {valores}")
    print(f". A lista tem {len(valores)}")
    print(f"A lista em ordem crescente é {valores.sort()})")

print("Cheguei ao fim da lista: ")"""

def main():
    print("main()")
    x = 5
    lx = [7, -2]
    print(f"    Before calling modify_args(): x {x}  lx {lx}")

    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)

    print(f"    After calling modify_args():  x {x}  lx {lx}")
if __name__ == "__main__":
    main()
