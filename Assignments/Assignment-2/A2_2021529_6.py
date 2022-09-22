def format_print(matrix: list[list[int]]) -> None:
    """prints a formatted version of the matrix"""
    
    n = len(matrix)
    flat = {str(matrix[i][j]) for i in range(n) for j in range(n)}
    x = len(max(flat, key=len))
    
    for row in matrix:
        for entry in row:
            print(str(entry).rjust(x), end=" ")
        print()


def normal(matrix: list[list[int]]) -> list[int]:
    """returns the list of elements obtained (in order) in normal traversal
    normal traversal: left to right for each row"""
    
    n = len(matrix)
    return [matrix[i][j] for i in range(n) for j in range(n)]


def alternate(matrix: list[list[int]]) -> list[int]:
    """returns the list of elements obtained (in order) in alternate traversal
    alternate traversal: left to right for first row, right to left for second and so on"""
    
    answer = []
    for i in range(len(matrix)):
        answer.extend(matrix[i] if i%2 == 0 else matrix[i][::-1])
    return answer


def spiral(matrix: list[list[int]]) -> list[int]:
    """returns the list of elements obtained (in order) in spiral traversal
    APPROACH:
        spiral traversing is equivalent to getting the boundary of the matrix
        deleting the boundary from the matrix
        repeating until the matrix gets empty"""
    
    copy, answer = matrix.copy(), []
    
    while copy:
        answer.extend(boundary(copy))
        try:
            del copy[0], copy[-1]
        except IndexError:
            break
        for i in range(len(copy)):
            copy[i] = copy[i][1:-1]
    
    return answer


def boundary(matrix: list[list[int]]) -> list[int]:
    """returns the list of elements obtained (in order) in boundary traversal
    boundary traversal: left to right, right to bottom, right to left, bottom to up"""
    
    n, answer = len(matrix), []
    
    # add the entire first row
    answer.extend(matrix[0])
    
    # add the last element of each row (except of the first row)
    answer.extend([matrix[i][-1] for i in range(1, n)])
    
    # add the entire last row in reverse (except the last element)
    answer.extend(matrix[-1][-2::-1])
    
    # add the first element of each row (except of the first and last rows)
    answer.extend([matrix[i][0] for i in range(n-2, 0, -1)])
    
    return answer


def diagonal_rl(matrix: list[list[int]]) -> list[int]:
    """returns the list of elements obtained (in order) in right to left diagonal traversal"""
    
    n, copy = len(matrix), matrix.copy()
    for i in range(n):
        copy[i] = [None]*i + copy[i] + [None]*(n-i)
    
    answer = []
    for i in range(2*n):
        for j in range(n):
            if copy[j][i] is None:
                continue
            answer.append(copy[j][i])
    
    return answer


def diagonal_lr(matrix: list[list[int]]) -> list[int]:
    """returns the list of elements obtained (in order) in right to left diagonal traversal"""
    
    n, copy = len(matrix), matrix.copy()
    for i in range(n):
        copy[i] = [None]*(n-i) + copy[i] + [None]*i
     
    answer = []
    for i in range(2*n-1, -1, -1):
        for j in range(n):
            if copy[j][i] is None:
                continue
            answer.append(copy[j][i])
    
    return answer
    

def main() -> None:
    """__main__ function"""
    
    while (N := int(input("Enter a positive order N for the matrix: "))) <= 0:
        print("Please enter a positive integer")

    matrix = []
    for i in range(N):
        matrix.append([int(i) for i in input(f"Enter space separated row of {N} elements: ").split()])
    
    print("\nEntered Matrix:")
    format_print(matrix)
    print()
    
    while True:
        print("Enter 1. for normal traversal")
        print("Enter 2. for alternate traversal")
        print("Enter 3. for spiral traversal from outwards to inwards")
        print("Enter 4. for boundary traversal")
        print("Enter 5. for diagonal traversal from right to left")
        print("Enter 6. for diagonal traversal from left to right")
        print("Enter 7. to Exit")
        
        choice = input("Enter your choice: ")
        if choice not in tuple("1234567"):
            print("INVALID INPUT: Please enter a number from 1-7 \n")
            continue
        print()
        
        if choice == "1":
            print("Normal Traversal:", *normal(matrix))
        
        elif choice == "2":
            print("Alternate Traversal:", *alternate(matrix))
        
        elif choice == "3":
            print("Spiral Traversal:", *spiral(matrix))
            
        elif choice == "4":
            print("Boundary Traversal:", *boundary(matrix))
        
        elif choice == "5":
            print("Right to Left Diagonal Traversal:", *diagonal_rl(matrix))
            
        elif choice == "6":
            print("Left to Right Diagonal Traversal:", *diagonal_lr(matrix))
            
        else:
            break
    
        print()


if __name__ == "__main__":
    main()