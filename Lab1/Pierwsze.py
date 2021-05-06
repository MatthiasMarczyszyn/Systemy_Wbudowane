import math


def equasion(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-1*b + math.sqrt(delta))/(2*a)
        x2 = (-1*b - math.sqrt(delta))/(2*a)
        print(f"Dwa pierwiastki {x1}, {x2} ")
    elif delta == 0:
        x = -1*b/(2*a)
        print(f"Jeden pierwiastek {x}")
    else:
        print("MicroPython nie osbługuje liczb zepolonych")


while(True):
    equasion(float(input("a=")), float(input("b=")), float(input("c=")))
    if input("Czy kontynuować Y/N:") == "N":
        break
