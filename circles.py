import math

def circle_area(r):
    # Check if r is a number (int or float)
    if not isinstance(r, (int, float)):
        raise TypeError("The radius must be a real number (int or float).")
    
    # Check if r is negative
    if r < 0:
        raise ValueError("The radius cannot be negative.")
    
    return math.pi * (r ** 2)



