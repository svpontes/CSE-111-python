# Example 1

# Create variables of different data types and then
# print the variable names, data types, and values.

a = "Her name is "  # string
b = "Isabella"      # string
c = a + b           # string plus string makes string
print(f"a: {type(a)} {a}")
print(f"b: {type(b)} {b}")
print(f"c: {type(c)} {c}")
print()

d = False  # boolean
e = True   # boolean
print(f"d: {type(d)} {d}")
print(f"e: {type(e)} {e}")
print()

f = 15     # number
g = 7.62   # number
h = f + g  # number plus number makes number
print(f"f: {type(f)} {f}")
print(f"g: {type(g)} {g}")
print(f"h: {type(h)} {h}")
print()

i = "True"   # string because of the surrounding quotes
j = "2.718"  # string because of the surrounding quotes
print(f"i: {type(i)} {i}")
print(f"j: {type(j)} {j}")
print()

# The input function always returns a string.
k = input("Please enter a number: ")        # string
m = input("Please enter another number: ")  # string
n = k + m          # string plus string makes string
print(f"k: {type(k)} {k}")
print(f"m: {type(m)} {m}")
print(f"n: {type(n)} {n}")
print()

# The int and float functions convert a string to a number.
p = int(input("Please enter a number: "))          # number
q = float(input("Please enter another number: "))  # number
r = p + q                 # number plus number makes number
print(f"p: {type(p)} {p}")
print(f"q: {type(q)} {q}")
print(f"r: {type(r)} {r}")