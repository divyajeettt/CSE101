import math


# Type Aliases
Vector = list[float]
Matrix = list[Vector]

FILENAME: str = ".\\Data\\Q2\\IO.txt"


def add_vectors(v1: Vector, v2: Vector) -> Vector:
    """adds vectors v1 and v2 and returns the result, i.e. returns v1 + v2"""
    
    # v1ᵢ is the i-th entry of the vector v1
    # v2ᵢ is the i-th entry of the vector v2
    return [v1[i] + v2[i] for i in range(4)]


def scale_vector(vector: Vector, c: float) -> Vector:
    """scales vector v by c and returns the result, i.e. returns c * vector"""
    
    # vᵢ is the i-th entry of the vector v
    return [c * vi for vi in vector]


def multiply(vector: Vector, matrix: Matrix) -> Vector:
    """performs Matrix mulitplication with the Vector, i.e. returns M * v
    Mv = m₁v₁ + m₂v₂ + ... + mₙvₙ"""
    
    total = [0, 0, 0, 0]
    for vi, mi in zip(vector, matrix):
        # mᵢ is the i-th column of the matrix
        # vᵢ is the i-th entry of the vector
        total = add_vectors(total, scale_vector(mi, vi))
    return total


def transformation(query: str) -> Matrix:
    """returns a Matrix corresponding the the given transformation
    mᵢ is the i-th column of the matrix"""
    
    match query.split():
        case ["S", sx, sy, sz]:
            m1 = [float(sx), 0, 0, 0]
            m2 = [0, float(sy), 0, 0]
            m3 = [0, 0, float(sz), 0]
            m4 = [0, 0, 0, 1]

        case ["T", tx, ty, tz]:
            m1 = [1, 0, 0, 0]
            m2 = [0, 1, 0, 0]
            m3 = [0, 0, 1, 0]
            m4 = [float(tx), float(ty), float(tz), 1]
        
        case ["R", "x", phi]:
            sin, cos = math.sin(float(phi)), math.cos(float(phi))
            m1 = [1, 0, 0, 0]
            m2 = [0, cos, sin, 0]
            m3 = [0, -sin, cos, 0]
            m4 = [0, 0, 0, 1]

        case ["R", "y", phi]:
            sin, cos = math.sin(float(phi)), math.cos(float(phi))
            m1 = [cos, 0, -sin, 0] 
            m2 = [0, 1, 0, 0]
            m3 = [sin, 0, cos, 0]
            m4 = [0, 0, 0, 1]
        
        case ["R" ,"z", phi]:
            sin, cos = math.sin(float(phi)), math.cos(float(phi))
            m1 = [cos, sin, 0, 0]
            m2 = [-sin, cos, 0, 0]
            m3 = [0, 0, 1, 0]
            m4 = [0, 0, 0, 1]
    
    # it is a list of columns of the required matrix
    # i.e. the return value is the transpose of the required matrix
    return [m1, m2, m3, m4]


def write_file(inputs: list[list[str]], outputs: list[list[str]]) -> None:
    """writes the inputs and outputs in a textfile"""
    
    with open(FILENAME, "a") as file:
        for coordinates in inputs + outputs:
            for coordinate in coordinates:
                file.write(coordinate + " ")
            file.write("\n")
        file.write("\n")


def main() -> None:
    """__main__ function"""
    
    n = int(input("Enter the number of vertices n: "))
    x = list(map(float, input("Enter space separated xᵢ: ").split()))
    y = list(map(float, input("Enter space separated yᵢ: ").split()))
    z = list(map(float, input("Enter space separated zᵢ: ").split()))
    q = int(input("Enter number of queries q: "))
    print()
    
    # list of original points
    coordinates0 = [[i, j, k, 1] for i, j, k in zip(x, y, z)]
    
    inputs = [[], [], []]
    for i, j, k, _ in coordinates0:
        inputs[0].append(f"{i:.2f}")
        inputs[1].append(f"{j:.2f}")
        inputs[2].append(f"{k:.2f}")
        
    for _ in range(q):
        # Assumption: phi is in radians if given in a Rotation Query
        query = input("Enter transformation query: ")
        
        # transformation matrix
        matrix = transformation(query=query)
        
        # transform the points in each iteration
        coordinates1 = [multiply(point, matrix) for point in coordinates0]
        coordinates0 = coordinates1.copy()
        
    # transformed x, y, z separately
    outputs = [[], [], []]
    for i, j, k, _ in coordinates1:
        outputs[0].append(f"{i:.2f}")
        outputs[1].append(f"{j:.2f}")
        outputs[2].append(f"{k:.2f}")
    
    print("\nFinally Transformed Coordinates are:")
    for p, coordinates in zip("xyz", outputs):
        print(f"{p}'ᵢ:", *coordinates)
    
    write_file(inputs, outputs)


if __name__ == "__main__":
    # main()
    v = [1, 1, 1, 1]
    m = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    print(multiply(v, m))