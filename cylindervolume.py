# Example 1

import math

# Define a function named print_cylinder_volume.
def main():
    radius = float(input("Enter the radius of a cylinder: "))
    height = float(input("Enter the height of a cylinder: "))
    
    volume = math.pi * radius**2 * height
    
    print(f"volume: {volume:.2f}")

main()