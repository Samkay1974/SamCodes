import math


def Square():
    a= (int(input("Enter the length of the square: ")))
    L = a*a
    print(f"The Area of the square is {L}")
def Rectangle():
    a = (int(input("Enter the length of the Rectangle: ")))
    b = (int(input("Enter the breadth/width of the Rectangle:")))
    A = int(a*b)
    print(f"The Area of the Rectangle is {A}")
def Triangle():
    b= (int(input("Enter the base of the Triangle: ")))
    h = (int(input("Enter the height of the Triangle: ")))
    A = int((1/2)* (b*h))
    print(f"The Area of the triangle is {A}")
def Circle():
    pi = float(22/7)
    r = (float(input("Enter the radius of the Circle: ")))
    A = float(pi * r**2)
    print(f"The Area of the Circle is {A:.2f}")
def Parallelogram():
    b = float(input("Enter the base of the parrellelogram:"))
    h = float(input("Enter the height of the parrallelogram:"))
    A = float(b*h)
    print(f"The Area of the Parrallelogram is {A:.2f} ")
def Trapezium():
    a =float(input("Enter the length of one side: "))
    b = float(input("Enter the other side of the trapezium: "))
    h = float(input("Enter the height of the trapezium: "))
    A = float(1/2 * (a+b)* h)
    print(f"The Area of the Trapezoid is {A:.2f}")
def SAcylinder():
    r = float(input("Enter the radius of the Cylinder: "))
    pi = float(math.pi)
    h = float(input("Enter the height of the cylinder: "))
    A = float(2*pi*r*(r+h))
    print(f"The Surface Area of the cylinder is {A:.2f}")
def Vcylinder():
    pi = float(math.pi)
    r = float(input("Enter the radius of the cylinder: ")) 
    h = float(input("Enter the height of the Cylinder: "))
    V  = float(pi*r**2*h)
    print(f"The Volume of the Cylinder is {V:.2f}")

user = int(input("Choose from the menu:\n1. Square\n2. Rectangle\n3. Triangle\n4. Circle\n5. Parallelogram\n6. Trapezoid\n7. SACylinder\n8. Vcylinder\n"))
if user == 1:
    Square()
elif user == 2:
    Rectangle()
elif user == 3:
    Triangle()
elif user == 4:
    Circle()
elif user == 5:
    Parallelogram()
elif user == 6:
    Trapezium()
elif user == 7:
    SAcylinder()
elif user == 8:
    Vcylinder()
else:
    print("Invalid choice. Please choose a number from 1 to 8.")