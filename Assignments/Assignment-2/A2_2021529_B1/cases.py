import math
import os


# function: function1()
def distance(p1: tuple[float], p2: tuple[float]) -> float:
    """returns the distance between two n-dimensional points, implemented manually"""
    
    dist = 0
    for i, j in zip(p1, p2):
        dist += (i-j) ** 2
    return dist ** 0.5


def generateData() -> int:
    """generates input-output pairs and stores them in separate files
    returns the number of pairs generated"""
    
    N = int(input("Enter the number of input-output pairs: "))
    
    # for some reason, my current working directory IS NOT the B1 folder, so change working directory
    os.chdir(os.path.join(os.getcwd(), "A2_2021529_B1"))
    
    for i in range(1, N+1):
        f_in = f"input_{i}.txt"
        f_out = f"output_{i}.txt"
        
        p1 = tuple(map(float, input("Enter space-separated elemnts of point 1: ").split()))
        p2 = tuple(map(float, input("Enter space-separated elemnts of point 2: ").split()))
        dist = distance(p1, p2)
        
        with open(f_in, "w") as f1, open(f_out, "w") as f2:
            f1.write(str(p1) + "\n")
            f1.write(str(p2))
            f2.write(str(dist))
        
        print(f"Inputs({i}) and Ouputs({i}) stored in files \n")
    
    return N