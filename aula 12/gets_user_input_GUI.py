"""
In order to test a program that gets user input from a graphical user
interface, separate the event functions (the ones that are executed
when a user types a value in a text field) into two functions. Move
the calculations out of an event function and into a calculation
function that takes parameters, performs a calculation, and returns a
result. Then write a test function for the new calculation function.
"""
    # This function is called each time the user releases a key.
    def calc(event):
        try:
            # Get the user input.
            w = txtWidth.get()
            a = txtRatio.get()
            d = txtDiam.get()

            # Compute the tire volume.
            v = tire_volume(w, a, d)

            # Display the volume for the user to see.
            lblResult.config(text=f"{v:.1}")

        except ValueError:
            # When the user deletes all the digits in one
            # of the text fields, clear the result labels.
                lblResult.config(text="")


def tire_volume(width, ratio, diam):
    """Compute and return the approximate volume of a tire."""
    vol = (math.pi * width * width * ratio *
            (width * ratio + 2540 * diam)) / 10_000_000
    return vol