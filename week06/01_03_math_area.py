# write a function that takes the length and width of a rectangle and returns the area

# write another function that finds the area of a cube
# bonus challenge: use your first function inside this function!

def rectangle_area (length,width):
    area = length * width
    return area

length_01 = rectangle_area(12,15)
length_02 = rectangle_area(11.15,10)

print(length_01)
print(length_02)

def cube_area (side):
    area_cube = side*side
    return area_cube

area_01 = cube_area(12)
area_02 = cube_area(10.5)

print(area_01)
print(area_02)


# write a function that finds the area of a sphere
# hint: you can get `pi` by importing math (google it!)

from math import pi

def sphere_area(radius):
    return 4*pi*(radius)**2
    
area_01 = sphere_area(15)
print(area_01)

