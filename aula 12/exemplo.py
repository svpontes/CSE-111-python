import pytest



def payment(amt, ar, y, ppy):
    """computes and returns the payments amount  for a loan with fixed annual interest rate"""

    r = ar / ppy
    n = y * ppy
    p = amt *r / (1-(1+r) ** -n)


    print(round(p, 2))
payment(10000, 0.07, 4, 12)

  