from typing import Union
import math


"""
APPROACH (Different than the one given in the problem statement):
• the directing vector d should be a unit vector
• d cannot be equal to the zero vector
• solving the equations of the ray and the sphere boils down to solving the quadratic:
    • ax² + bx + c = 0
    • a = ||d||² = 1 (since d is a unit vector)
    • b = 2 (d • (e-o))    # o is the centre of the sphere
    • c = ||o-p||² - r²

• if the equation has:
    • no positive roots: no point of intersection
    • 1 positive root: 1 point of intersection
    • 2 positive roots: 2 points of intersection

Using this approach, intersection can be found even for float values of parameter t,
which makes more sense, because the parameter should be a Real Number
"""


array = list[float]
SQ: str = "\N{SUPERSCRIPT TWO}"


def valid(v: str, check: str) -> bool:
    """returns True if v is a valid vector of format <x, y, z> or
    a valid point of format (x, y, z) and False in all other cases"""

    l, r = check
    if not (v.startswith(l) and v.endswith(r)):
        return False

    # remove brackets from either side
    if len(v := v.lstrip(l).rstrip(r).split(",")) != 3:
        return False

    for i in v:
        try:
            float(i)
        except ValueError:
            return False
    return True


def typecast(v: str, check: str) -> array:
    """returns a list of floats from a valid vector/point"""

    l, r = check
    return list(map(float, v.lstrip(l).rstrip(r).split(",")))


def normalize(v: array) -> array:
    """returns a unit vector in the direction of v"""

    return [i / math.hypot(*v) for i in v]


def solve(o: array, u: array, c: array, r: float) -> Union[tuple[array], tuple[None]]:
    """returns a pair of parameters t1, t2 where the sphere 
    described by c and r intersects the light 'line' described by o and u"""

    # difference of vectors o and c (o - c)
    diff = [i - j for i, j in zip(o, c)]
    
    # dot product of u and diff
    B = 2 * sum([i*j for i, j in zip(u, diff)])
    
    # ||diff||² - r²
    C = math.hypot(*diff)**2 - r**2

    disc = B**2 - 4*C
    if disc < 0:
        return None, None

    return ((-B + math.sqrt(disc)) / 2), ((-B - math.sqrt(disc)) / 2)


def format_point(e: array, d: array, t: float) -> str:
    """returns the Point on the ray described by e and d at t, properly formatted"""

    return str(tuple(f"{i + t*j:.2f}" for i, j in zip(e, d))).replace("'", "")


def main() -> None:
    """__main__ function"""

    while not valid((e := input("Enter components of e <ex, ey, ez>: ")), "<>"):
        print("Please enter a valid vector in format <ex, ey, ez>")

    while not valid((d := input("Enter components of d <dx, dy, dz>: ")), "<>"):
        print("Please enter a valid vector in format <dx, dy, dz>")

    # if d == <0, 0, 0>, take the input again
    while typecast(d, "<>") == [0, 0, 0]:
        print("'d' cannot be the zero vector")
        while not valid((d := input("Enter components of d <dx, dy, dz>: ")), "<>"):
            print("Please enter a valid vector in format <dx, dy, dz>")

    while not valid((x := input("Enter origin of sphere (x₀, y₀, z₀): ")), "()"):
        print("Please enter a valid point in format (x₀, y₀, z₀)")

    while (r := float(input("Enter radius of sphere: "))) <= 0:
        print("Radius of sphere msut be a positive float")

    d = dx, dy, dz = typecast(d, "<>")
    e = ex, ey, ez = typecast(e, "<>")
    x = x0, y0, z0 = typecast(x, "()")

    ray = f"p(t) = <{ex:.2f}, {ey:.2f}, {ez:.2f}> + t<{dx:.2f}, {dy:.2f}, {dz:.2f}>"
    sphere = f"(x - {x0:.2f}){SQ} + (y - {y0:.2f}){SQ} + (z - {z0:.2f}){SQ} = {r**2:.2f}"

    print()
    print(f"Equation of light ray:", ray)
    print(f"Equation of sphere:", sphere)
    
    # assumption: d is a unit vector
    # convert d to a unit vector if it isn't already
    d = normalize(d)
    t1, t2 = solve(e, d, x, r)
    print()

    # check the number of positive roots
    if t1 is None or (t1 < 0 and t2 < 0):
        print("The light ray and the sphere do NOT intersect")

    elif t1 == t2 or (t1 < 0 and t2 >= 0) or (t1 >= 0 and t2 < 0):
        print("The light ray intersects the sphere at ONE point")
        point = format_point(e, d, (t1 if t2 < 0 else t2))
        print("Point of intersection:", point)

    else:
        print("The light ray intersects the sphere at TWO points")
        print("1st Point of intersection:", format_point(e, d, t1))
        print("2nd Point of intersection:", format_point(e, d, t2))


if __name__ == "__main__":
    main()