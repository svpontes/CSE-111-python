#Testing functions

"""
ASSERT statements --> it is used to get computer to check if a comparation is TRUE.

if the computer find comparition is FALSE, the computer will raise an AssertionError - that will terminate the program. 
example 1:
"""
def main():

    amount = 100
    result = deposit(amount)

    print(result)

def deposit(amount):
    assert amount > 0
    return True
main()