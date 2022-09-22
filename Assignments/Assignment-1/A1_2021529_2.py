from math import pi


SHAPES_2D: list[str] = ["Square", "Rectangle", "Rhombus", "Parallelogram", "Circle"]
SHAPES_3D: list[str] = [
    "Cube", "Cuboid", "Right-Circular Cone", "Hemisphere", "Sphere", "Solid Cylinder", "Hollow Cylinder"
]


def menu_2D() -> None:
    """displays menu for 2D shapes"""
    
    for i, shape in enumerate(SHAPES_2D, start=1):
        print(f"Enter {i}. for {shape}")
    print()
    
    valid = tuple("12345")
    while (choice := input("Enter your choice: ")) not in valid:
        print("Please enter a valid choice")
    print()
    
    selected = SHAPES_2D[int(choice)-1]
    
    perimeter: float
    area: float
    
    if choice == "1":
        s = float(input("Enter side s: "))
        perimeter = 4*s
        area = s**2
    
    elif choice == "2":
        l = float(input("Enter length l: "))
        b = float(input("Enter breadth b: "))
        perimeter = 2 * (l+b)
        area = l*b
        
    elif choice == "3":
        a = float(input("Enter side a: "))
        d1 = float(input("Enter diagonal d1: "))
        d2 = float(input("Enter diagonal d2: "))
        perimeter = 4*a
        area = d1*d2 / 2
    
    elif choice == "4":
        l = float(input("Enter length l: "))
        b = float(input("Enter breadth b: "))
        h = float(input("Enter perpendicular height h: "))
        perimeter = 2 * (l+b)
        area = b*h
           
    else:
        r = float(input("Enter radius r: "))
        perimeter = 2 * pi * r
        area = pi * r**2
    
    print(f"1. Perimeter of the {selected} = {round(perimeter, 2)} units")
    print(f"2. Area of the {selected} = {round(area, 2)}", "units\N{SUPERSCRIPT TWO}")


def menu_3D() -> None:
    """displays menu for 3D shapes"""
    
    for i, shape in enumerate(SHAPES_3D, start=1):
        print(f"Enter {i}. for {shape}")
    print()
    
    valid = tuple("1234567")
    while (choice := input("Enter your choice: ")) not in valid:
        print("Please enter a valid choice")
    print()
    
    selected = SHAPES_3D[int(choice)-1]
    
    lsa: float
    tsa: float
    volume: float
    
    if choice == "1":
        s = float(input("Enter side s: "))
        lsa = 4 * s**2
        tsa = 6 * s**2
        volume = s**3
    
    elif choice == "2":
        l = float(input("Enter length l: "))
        b = float(input("Enter breadth b: "))
        h = float(input("Enter height h: "))
        lsa = 2 * h * (l+b)
        tsa = 2 * (l*b + b*h + h*l)
        volume = l*b*h
    
    elif choice == "3":
        r = float(input("Enter base radius r: "))
        h = float(input("Enter vertical height h: "))
        l = float(input("Enter slant height l: "))
        lsa = pi * r * l
        tsa = pi * r * (r+l)
        volume = pi * r**2 * h / 3
    
    elif choice == "4":
        r = float(input("Enter radius r: "))
        lsa = 2 * pi * r**2
        tsa = 3 * pi * r**2
        volume = 2/3 * pi * r**3
    
    elif choice == "5":
        r = float(input("Enter radius r: "))
        lsa = tsa = 4 * pi * r**2
        volume = 4/3 * pi * r**3
    
    elif choice == "6":
        r = float(input("Enter radius r: "))
        h = float(input("Enter height h: "))
        lsa = 2 * pi * r * h
        tsa = 2 * pi * r * (r+h)
        volume = pi * r**2 * h
    
    else:
        r1 = float(input("Enter radius r1: "))
        r2 = float(input("Enter radius r2: "))
        h = float(input("Enter height h: "))
        lsa = 2 * pi * (r1+r2) * h
        tsa = lsa + 2*pi * abs(r1**2 - r2**2)
        volume = pi * abs(r1**2 - r2**2) * h
        
    print(f"1. L.S.A of the {selected} = {round(lsa, 2)}", "units\N{SUPERSCRIPT TWO}")
    print(f"2. C,S.A of the {selected} = {round(tsa, 2)}", "units\N{SUPERSCRIPT TWO}")
    print(f"3. Volume of the {selected} = {round(volume, 2)}", "units\N{SUPERSCRIPT THREE}")


def main() -> None:
    """__main__ function"""

    n = int(input("Enter the number of students: "))
    print()
    
    for _ in range(n):
        while (dimension := input("Enter dimension (2D or 3D): ")) not in ("2D", "3D"):
            print("Please enter a valid value (2D or 3D)")

        print()
        if dimension == "2D":
            menu_2D()
        else:
            menu_3D()
        print()


if __name__ == "__main__":
    main()