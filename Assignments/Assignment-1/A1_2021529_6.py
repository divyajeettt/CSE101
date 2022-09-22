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


def f(x: float, coeffs: array, exponents: array) -> float:
    """returns the value of the polynomial described by coeffs and exponents at x"""
    
    total = 0
    for coeff, exponent in zip(coeffs, exponents):
        try:
            # avoid cases where answer becomes complex
            if not (x < 0 and not exponent.is_integer()):
                total += coeff * x**exponent
        except ZeroDivisionError:
            # skip cases where division by zero occurs by 0**a, a < 0
            continue
    return total


def differentiate(coeffs: array, exponents: array) -> tuple[array, array]:
    """returns the coeffs and exponents of the polynomial obtained
    by differentiating the polynomial described by given coeffs and exponents"""
    
    # differentiating polynomials:
    #     • multiply coefficients by corresponding power
    #     • reduce powers by 1, if power is not zero
    for i in range(len(coeffs)):
        coeffs[i] *= exponents[i]
        exponents[i] -= 1 if exponents[i] != 0 else 0
    
    return coeffs, exponents


def find_roots(l: array) -> float:
    """implements the Newton-Raphson method for finding roots to a
    polynomial whose coefficients are 1 and exponents are given in l
    for example, if l = [a, b, c] then f(x) = xᵃ + xᵇ + xᶜ"""

    cfs0, exp0 = [1 for _ in l], l.copy()     
    cfs1, exp1 = differentiate(cfs0.copy(), exp0.copy())
    
    x0 = 1
    while True:
        try:
            x1 = x0 - f(x0, cfs0, exp0) / f(x0, cfs1, exp1)
        except ZeroDivisionError:
            # if denominator is zero, try for a different x0
            x0 += 1
        else:
            break

    # tolerance of 1e-10, can be decreased for a more precise solution
    while abs(x1-x0) > 1e-10:
        x0 = x1
        try:
            x1 = x0 - f(x0, cfs0, exp0) / f(x0, cfs1, exp1)
        except ZeroDivisionError:
            # if denominator is zero, stop the loop
            break

    return x1


def main() -> None:
    """__main__ function"""
    
    exponents = list(map(float, input("Enter space separated exponents: ").split()))
    root = round(find_roots(exponents), 5)
    print("The equation you entered is f(x) =", polynomial(exponents))
    print(f"Calculated root of f(x) by Newton-Raphson Method =", root)
    

if __name__ == "__main__":
    main()