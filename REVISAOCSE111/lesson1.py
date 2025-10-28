#example 1

a = "Her name is"
b = "Isabela"
c = a + b

print (f"a: {type(a)} {a}")
print (f"b: {type(b)} {b}")
print (f"c: {type(c)} { c}")

print()

d = False
e = True

print(f"d: {type(d)} {d} {e}")

span = float(input("enter the distance that cable must span in meter?" ))

dip = float(input("Distance the cable will sag in meters: "))

length = span + (8*dip**2) / (3 * span)


print(f" The lenght is: {length:.2f}")

