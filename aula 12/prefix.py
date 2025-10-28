
def main():
    
    result = prefix("incontinente", "incopetente")
    
    print(f"o resultado é {result}")

   
    total = soma(10,50)
    print(f"a soma é {total}")

def prefix(s1, s2):
    """Return the prefix, if any, that appears in both s1 and s2. In
    other words, return a string of the characters that appear at the
    beginning of both s1 and s2. For example, if s1 is "inconceivable"
    and s2 is "inconvenient", this function will return "incon".
    """
    s1 = s1.lower()
    s2 = s2.lower()
    i = 0
    limit = min(len(s1), len(s2))
    while i < limit:
        if s1[i] != s2[i]:
            break
        i += 1
    return s1[0:i]

def soma(num1, num2):
    
    result = num1 + num2

    return result
        


if __name__ == "__main__":
    main()

