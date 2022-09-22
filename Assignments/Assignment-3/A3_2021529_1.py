import math


Vector = list[float]
Matrix = list[Vector]


def matmul(A: Matrix, B: Matrix) -> Matrix:
    """returns the result obtained when Matrix A is multipled with Matrix B
    i.e. returns C = AB"""

    ans = [[None for _ in range(len(B[0]))] for _ in range(len(A))]

    for i, rowAi in enumerate(A):
        for j in range(len(B[0])):
            colBj = [rowB[j] for rowB in B]
            ans[i][j] = sum(rowAi[k] * colBj[k] for k in range(len(colBj)))
    
    return ans


def scale(x: Vector, y: Vector, z: Vector, sx: float, sy: float, sz: float) -> Matrix:
    """returns [x', y', z'] which is the scaled version of [x, y, z]"""
    
    x_, y_, z_ = [], [], []
    
    for i, j, k in zip(x, y, z):
        i_, j_, k_ = matmul(
            [[sx, 0, 0, 0], [0, sy, 0, 0], [0, 0, sz, 0], [0, 0, 0, 1]], [[i], [j], [k], [1]]
        )[:-1]
        x_.extend(i_)
        y_.extend(j_)
        z_.extend(k_)
    
    return [x_, y_, z_]


def translate(x: Vector, y: Vector, z: Vector, tx: float, ty: float, tz: float) -> Matrix:
    """returns [x', y', z'] which is the translated version of [x, y, z]"""
    
    x_, y_, z_ = [], [], []
    
    for i, j, k in zip(x, y, z):
        i_, j_, k_ = matmul(
            [[1, 0, 0, tx], [0, 1, 0, ty], [0, 0, 1, tz], [0, 0, 0, 1]], [[i], [j], [k], [1]]
        )[:-1]
        x_.extend(i_)
        y_.extend(j_)
        z_.extend(k_)
    
    return [x_, y_, z_]


def rotate(x: Vector, y: Vector, z: Vector, axis: str, phi: float) -> Matrix:
    """returns [x', y', z'] which is the rotated version of [x, y, z]"""
    
    sin, cos = math.sin(phi), math.cos(phi)
    x_, y_, z_ = [], [], []
    
    if axis == "x":
        matrix = [[1, 0, 0, 0], [0, cos, -sin, 0], [0, sin, cos, 0], [0, 0, 0, 1]]
    elif axis == "y":
        matrix = [[cos, 0, sin, 0], [0, 1, 0, 0], [-sin, 0, cos, 0], [0, 0, 0, 1]]
    else:
        matrix = [[cos, -sin, 0, 0], [sin, cos, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    
    for i, j, k in zip(x, y, z):
        i_, j_, k_ = matmul(matrix, [[i], [j], [k], [1]])[:-1]
        x_.extend(i_)
        y_.extend(j_)
        z_.extend(k_)
    
    return [x_, y_, z_]