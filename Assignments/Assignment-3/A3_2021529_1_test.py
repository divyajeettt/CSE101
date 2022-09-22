import A3_2021529_1


Vector = A3_2021529_1.Vector
Matrix = A3_2021529_1.Matrix


def test_matmul(A: Matrix, B: Matrix, true_C: Matrix) -> bool:
    """returns True if matmul(A, B) matches with true_C, False otherwise"""
    
    try:
        assert A3_2021529_1.matmul(A, B) == true_C
        return True
    except AssertionError:
        return False


def test_scale(
        x: Vector, y: Vector, z: Vector, sx: float, sy: float, sz: float, 
        true_x: Vector, true_y: Vector, true_z: Vector
    ) -> bool:
    """returns True if scale(x, y, z, sx, sy, sz) matches with [true_x, true_y, true_z]"""
    
    try:
        assert A3_2021529_1.scale(x, y, z, sx, sy, sz) == [true_x, true_y, true_z]
        return True
    except AssertionError:
        return False


def test_translate(
        x: Vector, y: Vector, z: Vector, tx: float, ty: float, tz: float, 
        true_x: Vector, true_y: Vector, true_z: Vector
    ) -> bool:
    """returns True if translate(x, y, z, tx, ty, tz) matches with [true_x, true_y, true_z]"""
    
    try:
        assert A3_2021529_1.translate(x, y, z, tx, ty, tz) == [true_x, true_y, true_z]
        return True
    except AssertionError:
        return False


def test_rotate(
        x: Vector, y: Vector, z: Vector, axis: str, phi: float, true_x: Vector, true_y: Vector, true_z: Vector
    ) -> bool:
    """returns True if rotate(x, y, z, axis, phi) matches with [true_x, true_y, true_z]"""
    
    try:
        assert A3_2021529_1.rotate(x, y, z, axis, phi) == [true_x, true_y, true_z]
        return True
    except AssertionError:
        return False


def main() -> None:
    """__main__ function"""
    
    # Test Cases for matmul(A, B)
    
    A1 = [[1, 0], [0, 1]]
    B1 = [[2, 5], [-6, 3]]
    C1 = B1
    
    if test_matmul(A1, B1, true_C=C1):
        print("matmul(A, B) successful for Test Case #1")
    else:
        print("matmul(A, B) failed for Test Case #1")
    
    A2 = [[3, 2, 1], [1, 4, 0]]
    B2 = [[-1, -1, -1], [2, 4, 1], [-5, 0, 1]]
    C2 = [[-4, 5, 0], [7, 15, 3]]
    
    if test_matmul(A2, B2, true_C=C2):
        print("matmul(A, B) successful for Test Case #2")
    else:
        print("matmul(A, B) failed for Test Case #2")
    
    A3 = [[1, 2], [3, 4], [5, 6]]
    B3 = [[7, 8, 9], [10, 11, 12]]
    C3 = [[27, 30, 33], [61, 68, 75], [95, 106, 117]]
    
    if test_matmul(A3, B3, true_C=C3):
        print("matmul(A, B) successful for Test Case #3")
    else:
        print("matmul(A, B) failed for Test Case #3")
    
    print()
    
    # Test Cases for scale(x, y, z, sx, sy, sz)
    
    x1, y1, z1, sx1, sy1, sz1 = [1, 2, 3], [1, 4, 1], [2, 2, 3], 4, 5, 6
    true_x1, true_y1, true_z1 = [4, 8, 12], [5, 20, 5], [12, 12, 18]
    
    if test_scale(x1, y1, z1, sx1, sy1, sz1, true_x1, true_y1, true_z1):
        print("scale(x, y, z, sx, sy, sz) successful for Test Case #1")
    else:
        print("scale(x, y, z, sx, sy, sz) failed for Test Case #1")
    
    x2, y2, z2, sx2, sy2, sz2 = [0, -1], [1, 9], [0, 0], 1, -2, 3
    true_x2, true_y2, true_z2 = [0, -1], [-2, -18], [0, 0]
    
    if test_scale(x2, y2, z2, sx2, sy2, sz2, true_x2, true_y2, true_z2):
        print("scale(x, y, z, sx, sy, sz) successful for Test Case #2")
    else:
        print("scale(x, y, z, sx, sy, sz) failed for Test Case #2")
        
    x3, y3, z3, sx3, sy3, sz3 = [4], [-5], [0], 0, 1, 2
    true_x3, true_y3, true_z3 = [0], [-5], [0]
    
    if test_scale(x3, y3, z3, sx3, sy3, sz3, true_x3, true_y3, true_z3):
        print("scale(x, y, z, sx, sy, sz) successful for Test Case #3")
    else:
        print("scale(x, y, z, sx, sy, sz) failed for Test Case #3")
        
    print()
    
    # Test Cases for translate(x, y, z, tx, ty, tz)
    
    x1, y1, z1, tx1, ty1, tz1 = [1, 2, 3], [1, 4, 1], [2, 2, 3], 4, 5, 6
    true_x1, true_y1, true_z1 = [5, 6, 7], [6, 9, 6], [8, 8, 9]
    
    if test_translate(x1, y1, z1, tx1, ty1, tz1, true_x1, true_y1, true_z1):
        print("translate(x, y, z, tx, ty, tz) successful for Test Case #1")
    else:
        print("translate(x, y, z, tx, ty, tz) failed for Test Case #1")
    
    x2, y2, z2, tx2, ty2, tz2 = [0, -1], [1, 9], [0, 0], 1, -2, 3
    true_x2, true_y2, true_z2 = [1, 0], [-1, 7], [3, 3]
    
    if test_translate(x2, y2, z2, tx2, ty2, tz2, true_x2, true_y2, true_z2):
        print("translate(x, y, z, tx, ty, tz) successful for Test Case #2")
    else:
        print("translate(x, y, z, tx, ty, tz) failed for Test Case #2")
        
    x3, y3, z3, tx3, ty3, tz3 = [4], [-5], [0], 0, 1, 2
    true_x3, true_y3, true_z3 = [4], [-4], [2]
    
    if test_translate(x3, y3, z3, tx3, ty3, tz3, true_x3, true_y3, true_z3):
        print("translate(x, y, z, tx, ty, tz) successful for Test Case #3")
    else:
        print("translate(x, y, z, tx, ty, tz) failed for Test Case #3")
        
    print()
    
    # Test Cases for rotate(x, y, z, axis, phi)
    
    x1, y1, z1, axis1, phi1 = [1, 1, 1], [3, 5, -4], [0, 0, 3], "x", A3_2021529_1.math.pi
    true_x1, true_y1, true_z1 = [1, 1, 1], [-3.0, -5.0, 3.9999999999999996], [3.6739403974420594e-16, 6.123233995736766e-16, -3.0000000000000004]
    
    if test_rotate(x1, y1, z1, axis1, phi1, true_x1, true_y1, true_z1):
        print("rotate(x, y, z, axis, phi) successful for Test Case #1")
    else:
        print("rotate(x, y, z, axis, phi) failed for Test Case #1")
    
    x2, y2, z2, axis2, phi2 = [0, 0], [0, 1], [1, 4], "z", A3_2021529_1.math.pi/2
    true_x2, true_y2, true_z2 = [0.0, -1.0], [0.0, 6.123233995736766e-17], [1, 4]
    
    if test_rotate(x2, y2, z2, axis2, phi2, true_x2, true_y2, true_z2):
        print("rotate(x, y, z, axis, phi) successful for Test Case #2")
    else:
        print("rotate(x, y, z, axis, phi) failed for Test Case #2")

    x3, y3, z3, axis3, phi3 = [-2], [3], [-4], "y", A3_2021529_1.math.pi/2
    true_x3, true_y3, true_z3 = [-4], [3], [1.9999999999999998]
    
    if test_rotate(x3, y3, z3, axis3, phi3, true_x3, true_y3, true_z3):
        print("rotate(x, y, z, axis, phi) successful for Test Case #3")
    else:
        print("rotate(x, y, z, axis, phi) failed for Test Case #3")


if __name__ == "__main__":
    main()