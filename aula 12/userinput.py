def get_int(prompt, min, max):
    """Prompt the user for an integer, verify that it is
    between min and max inclusive, and return the integer.
    """
    num = None
    while num is None:
        try:
            text = input(prompt)
            prospect = int(text)
            if prospect < min:
                print(f"Invalid input: number must be {min} or greater.")
            elif prospect > max:
                print(f"Invalid input: number must be {max} or less.")
            else:
                num = prospect
        except ValueError as val_err:
            print(f"Invalid integer: {text}. Please try again.")
    return num
