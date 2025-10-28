import math

def main():

    name = "#1 Picnic"
    height = 6.83
    radius = 10.16
    cost = 0.28

    calc_volume = compute_volume(radius, height)
    
    print(calc_volume)
    
    calc_surface_area = surface_area(radius, height)
    print(calc_surface_area)

    calc_efficiency = efficiency(calc_volume, calc_surface_area)
    print(f"{name} {calc_efficiency:.1f}")

    calc_cost_efficiency = compute_cost_efficiency(calc_volume, cost)
    print(f"The cost efficiency is: {calc_cost_efficiency}")

    calc_storage_efficiency = compute_storage_efficicency(radius, height)
    print(f"The sttorage efficiency is : {calc_storage_efficiency}")

def compute_storage_efficicency(radius, height):

    volume = compute_volume(radius, height)
    surf_area = surface_area(radius, height)
    efficiency = volume / surf_area
    return efficiency

def compute_cost_efficiency(radius, height, cost):
    
    volume = compute_volume(radius, height)
    efficiency_cost = volume / cost
    
    return efficiency_cost

def efficiency(volume, surface_area):

    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def surface_area(radius, height):
    surface_area = 2 * math.pi *radius*(radius + height)
    return surface_area


    

if __name__ == "__main__":
    main()