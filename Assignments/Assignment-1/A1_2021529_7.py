"""
My code can handle positive/negative float values for exponents,
lower and upper limits and for step value.
"""


array = list[float]


def polynomial(exponents: array) -> str:
    """returns the str representation of the polynomial described by the
    given exponents (all coeffs are 1 in this case)"""
    
    superscripts = str.maketrans("0123456789.+-", "⁰¹²³⁴⁵⁶⁷⁸⁹·⁺⁻")
    
    string = ""
    for exponent in exponents:
        exponent = int(exponent) if exponent.is_integer() else exponent
        string += f"x{str(exponent).translate(superscripts)} + "
    
    return string.rstrip(" + ")


def f(x: float, exponents: array) -> float:
    """returns the value of the polynomial described by exponents at x
    (all coeffs are 1 in this case)"""
    
    total = 0
    for exponent in exponents:
        try:
            # avoid cases where answer becomes complex
            if not (x < 0 and not exponent.is_integer()):
                total += x**exponent
        except ZeroDivisionError:
            # skip cases where division by zero occurs by 0**a, a < 0
            continue
    return total


def integral(exponents: array, a: float, b: float) -> float:
    """returns the approximate area under the polynomial function described by
    given exponents from a to b (all coeffs are 1 in this case)"""
    
    # return value according to given equation
    return ((b-a) / 6) * (f(a, exponents) + 4*f((a+b)/2, exponents) + f(b, exponents))
    
    
def calculate_area(l: array, a: float, b: float, d: float) -> float:
    """implements the Simpson's Algorithm for finding area under a
    polynomial whose coefficients are 1 and exponents are given in l
    for example, if l = [a, b, c] then f(x) = xᵃ + xᵇ + xᶜ"""
    
    # not using range() so that float values can be considered
    # increasing a in increments of d until we reach b
    
    if a > b:
        lower, upper = b, a
        if d >= 0:
            print("Calculation Not Possible! d must be negative")
            return
        d *= -1
    else:
        lower, upper = a, b
        if d <= 0:
            print("Calculation Not Possible! d must be positive")
            return
    
    area = 0
    while lower < upper:
        area += integral(l, lower, lower+d)
        lower += d
    
    return area if a < b else area*-1


def main() -> None:
    """__main__ function"""
    
    exponents = list(map(float, input("Enter space separated exponents: ").split()))
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    d = float(input("Enter the value of d: "))
    
    if (b-a) % d != 0:
        print("b - a is not divisible by d")
    else:
        area = calculate_area(exponents, a, b, d)
        if area is not None:
            area = round(area, 5)
            print("The equation you entered is f(x) =", polynomial(exponents))
            print(f"Calculated area under f(x) from a to b by Simpson's Algorithm =", area)


if __name__ == "__main__":
    main()