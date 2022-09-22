import cases
import math

 
# function: function2()
def distance(p1: tuple[float], p2: tuple[float]) -> float:
    """returns the distance between two n-dimensional points
    implemented using dist function from math module"""
    
    return math.dist(p1, p2)


def testing(N: int) -> str:
    """tests the input-output pairs generated using cases.py
    N is the number of input-output pairs
    returns 'SUCCESS' if all input-output pairs match, 'FAILED' otherwise"""
    
    answer = "SUCCESS"
    
    for i in range(1, N+1):
        with open(f"input_{i}.txt") as f1, open(f"output_{i}.txt") as f2:
            p1, p2 = map(eval, f1.readlines())
            d1 = float(f2.read())
            d2 = distance(p1, p2)
            
            if d1 != d2:
                answer = "FAILED"
                break
    
    return answer


def main() -> None:
    """__main__ function"""
    
    # generate input-output pairs
    N = cases.generateData()
    
    print("\nTesting...")
    print("Results of testing:", testing(N))
    

if __name__ == "__main__":
    main()