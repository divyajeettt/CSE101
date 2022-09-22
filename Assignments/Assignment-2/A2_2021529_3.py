import string


"""
NOTES:
    • MAXIMUM RADIX ALLOWED: 36, i.e. 1 < radix <= 36
    • This is done as RADIX > 36 is VERY RARELY used, and there are 26 alphabets only
    • part 7 of menu (radix A to radix B) has also been implemented
    • built-in bin(), oct() and hex() functions exist in python, but HAVE NOT been used in this program
"""


TO_INT: dict[str, int] = {
    **{str(i): i for i in range(10)},
    **{chr(i): i-ord("A")+10 for i in range(65, 91)}
}

TO_STR: dict[int, str] = {j: i for i, j in TO_INT.items()}

SUBSCRIPTS = str.maketrans("1234567890", "₁₂₃₄₅₆₇₈₉₀")

VALID: str = string.digits + string.ascii_uppercase


def represent(n: str, r: int) -> str:
    """represens numbers in different radix, for e.g.:
    1202 (radix = 3) -> (1202)₃"""
    
    return f"({n}){str(r).translate(SUBSCRIPTS)}"


def check(n: str, r: int) -> bool:
    """returns True if n is a valid number in radix r, False otherwise"""
    
    for i in n:
        if VALID.index(i) > r-1:
            return False
    return True


def convert(n: str, A: int, B: int) -> str:
    """radix A -> radix B"""
    
    if set(n) == {"0"}:
        return "0"
    
    if A != 10:
        total, digits = 0, len(n)
        for i in range(digits):
            total += TO_INT[n[digits-i-1]] * A**i
    else:
        total = int(n)
    
    converted = []
    while total:
        converted.insert(0, TO_STR[total%B])
        total //= B
    return "".join(converted)


def main() -> None:
    """__main__ function"""
    
    d, b, o, h = "decimal", "binary", "octal", "hexadecimal"
    
    options: dict[str, tuple[str, str]] = {
        "1": (d, b), "2": (d, h), "3": (d, o), "4": (b, h), "5": (b, o), "6": (h, o)
    }
    
    while True:
        print(f"Enter 1. to convert from {d} to {b} and vice-versa")
        print(f"Enter 2. to convert from {d} to {h} and vice-versa")
        print(f"Enter 3. to convert from {d} to {o} and vice-versa")
        print(f"Enter 4. to convert from {b} to {h} and vice-versa")
        print(f"Enter 5. to convert from {b} to {o} and vice-versa")
        print(f"Enter 6. to convert from {h} to {o} and vice-versa")
        print("Enter 7. to convert from radix A to radix B")
        print("Enter 8. to Exit")
        
        choice1 = input("\nEnter your choice: ")
        
        if choice1 == "8":
            break
        
        print()
        if choice1 not in tuple("1234567"):
            print("INVALID CHOICE: Please enter a number from 1-8 \n")
            continue
        
        if choice1 != "7":
            r1, r2 = options[choice1]
            print(f"Enter 1. for {r1} to {r2}")
            print(f"Enter 2. for {r2} to {r1}")
            
            while (choice2 := input("Enter your choice: ")) not in tuple("12"):
                print("Please enter 1 or 2")
                
            print()
            while not (num := input("Enter number: ").upper()).isalnum():
                print("Please enter a valid integer with radix 2-36")  
            print()
                
            if choice1 == "1":
                A, B = (10, 2) if choice2 == "1" else (2, 10)
            
            elif choice1 == "2":
                A, B = (10, 16) if choice2 == "1" else (16, 10)
        
            elif choice1 == "3":
                A, B = (10, 8) if choice2 == "1" else (8, 10)
                
            elif choice1 == "4":
                A, B = (2, 16) if choice2 == "1" else (16, 2)
            
            elif choice1 == "5":
                A, B = (2, 8) if choice2 == "1" else (8, 2)
            
            elif choice1 == "6":
                A, B = (16, 8) if choice2 == "1" else (8, 16)
        
        else:
            A = int(input("Enter radix A: "))
            B = int(input("Enter radix B: "))
            while not (num := input("Enter number: ").upper()).isalnum():
                print("Please enter a valid integer with radix 2-36")  
            print()
        
        if not check(num, A):
            print(f"{num} is not a valid number for radix {A} \n")
        else:
            print(represent(num, A), "=", represent(convert(num, A, B), B), "\n")


if __name__ == "__main__":
    main()