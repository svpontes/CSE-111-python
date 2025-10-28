import math
def main():

    radius = float(input("enter number: "))    
    height = float(input("enter number: "))

    volume = compute_cylinder_volume(radius, height)

    print(f"the volume is: {volume:.2f}")

def compute_cylinder_volume(radius, height):
    volume = math.pi * radius** 2 * height
    return volume

if __name__ =="__main__":
    main()