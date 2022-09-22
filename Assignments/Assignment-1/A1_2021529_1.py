import itertools


def right_angled_triangle(n: int) -> None:
    """Prints a right angled triangle pattern"""

    for i in range(1, n+1):
        print(*range(1, i+1), sep=" ")
        

def isosceles_triangle(n: int) -> None:
    """Prints an isosceles triangle pattern
    constraint: n is always even"""
    
    if n%2 != 0:
        print("'n' must be even")
        return
    
    for i in range(1, n+1):
        print(end=" "*(n-i))
        for j in range(1, 2*i):
            print(j, end="")
        print()


def kite(n: int) -> None:
    """Prints a kite pattern
    constraint: n is always even"""
    
    if n%2 != 0:
        print("'n' must be even")
        return
    
    # instead of writing the same loop with a different range again,
    # we combine the two ranges together and loop over them once
    
    for i in itertools.chain(range(1, n+1), range(n-1, 0, -1)):
        print(end=" "*(n-i))
        for j in range(1, 2*i):
            print(j, end="")
        print()


def half_kite(n: int) -> None:
    """Prints a half kite pattern"""
    
    # instead of writing the same loop with a different range again,
    # we combine the two ranges together and loop over them once
    
    for i in itertools.chain(range(1, n+1), range(n-1, 0, -1)):
        print(*range(1, i+1), sep=" ")
    

def pattern_X(n: int) -> None:
    """Prints a pattern "X"
    constraint: n is always even"""
    
    if n%2 != 0:
        print("'n' must be even")
        return
    
    # instead of writing the same loop with a different range again,
    # we combine the two ranges together and loop over them once
    
    for i in itertools.chain(range(n, 1, -1), range(1, n+1)):
        print(end=" "*(n-i))
        for j in range(1, 2*i):
            print(j, end="")
        print()


def valid(choice: str) -> bool:
    """returns True if the choice is valid and False otherwise"""
    
    return choice in ["right-angled triangle", "isosceles triangle", "kite", "half kite", "x"]
    
    
def main() -> None:
    """__main__ function"""
      
    while True:
        print("Enter 'Right-Angled Triangle' for pattern: right-angled triangle")
        print("Enter 'Isosceles Triangle' for pattern: isosceles triangle")
        print("Enter 'Kite' for pattern: kite")
        print("Enter 'Half Kite' for pattern: half kite")
        print("Enter 'X' for pattern: X")
        print("Enter 'Exit' to Exit \n")
        
        # for case-insensitive checking, use .casefold()
        choice = input("Enter your choice: ").casefold()

        if choice == "exit":
            break
        if not valid(choice):
            print("INVALID INPUT: Please enter a valid input. \n")
            continue
        
        n = int(input("Enter the value of n: "))
        if n <= 0:
            print("'n' must be a positive integer \n")
            continue
        
        print()
        
        if choice == "right-angled triangle":
            right_angled_triangle(n)
        
        elif choice == "isosceles triangle":
            isosceles_triangle(n)
        
        elif choice == "kite":
            kite(n)
        
        elif choice == "half kite":
            half_kite(n)
        
        else:
            pattern_X(n)
        
        print()


if __name__ == "__main__":
    main()