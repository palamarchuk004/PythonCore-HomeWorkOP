          # Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump > mpg * fuel_left:
        return 0
    else:
        return 1
print(zero_fuel(50, 25, 2))
    