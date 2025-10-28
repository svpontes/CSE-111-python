import math
def compute_cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def main():
    radius = float(input("enter de radius: "))
    height = float(input("enter the height: "))
    volume = compute_cylinder_volume(radius, height)

    print(f"volume: {volume:.2f}")
main()