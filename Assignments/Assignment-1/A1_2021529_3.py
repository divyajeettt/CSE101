from typing import Callable


"""
The values of all coefficients and limits can be any positive/negative floats
The value of leading coefficient CANNOT be equal to zero (as per definition of polynomials)
If the given polynomial is y = f(x), my code can handle NEGATIVE y values:
    • Example:
        • degree = 2
        • a, b, c = 1, -3, -5
        • x varies from -5, 5 with step value 0.5
"""


def polynomial(degree: int) -> Callable[[float], int]:
    """returns a polynomial function with the given degree
    coeffs are taken as input inside this function"""
    
    while (coeff1 := float(input("Enter coefficient 1: "))) == 0:
        print("Leading Coefficient cannot be zero")
    
    coeffs = [coeff1] + [
        float(input(f"Enter coefficient {i}: ")) for i in range(2, degree+2)
    ]
    
    def func(x: float) -> int:
        """returns the rounded value of polynomial function with x as input
        i.e. y = round(f(x))"""
        
        total = 0
        for i, coeff in enumerate(coeffs):
            total += coeff * x**(degree-i)
        return round(total)

    # return the function created with the given coefficients
    return func


def main() -> None:
    """__main__ function"""

    print("Provide details for the Polynomial Function")
    
    while (degree := int(input("Enter degree: "))) not in range(4):
        print("Degree of polynomial must be between 0 to 3")
    print()
    
    # create a polynomial of given degree
    f = polynomial(degree)
    
    lower = float(input("Enter Lower Bound for x: "))
    
    while (upper := float(input("Enter Upper Bound for x: "))) <= lower:
        print("Upper Bound must be greater than Lower Bound")
    
    while (step := float(input("Provide step value to increment x: "))) <= 0:
        print("Step must be a positive integer/float")
    
    print("=" * 80)
    
    # create a list of output values
    x, values = lower, []
    while x <= upper:
        values.append(f(x))
        x += step
    
    neg = abs(min(values))
    for num in values:
        if num >= 0:
            # print spaces before the "*"s
            print(f"{' '*(neg+1)}|{num*'*'}")
        else:
            # print spaces after the "*"s
            print(f"{abs(num)*'*'}|".rjust(neg+2))


if __name__ == "__main__":
    main()