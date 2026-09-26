import math

r = float(input("enter radius:"))
area = math.pi * r ** 2;
circumference = math.pi * r ** 2

print (area)
print(circumference);


def cylinder(r,h):
    area = 2 * math.pi * r * (r + h)
    volume = math.pi * r ** 2 * h
    return area,volume

r=float(input("enter radius:"))
h= float(input("enter hight"))

area , volume = cylinder(r,h)

print(area)
print(volume)


