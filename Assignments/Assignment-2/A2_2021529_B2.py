def transpose(matrix: list[list[str]]) -> list[list[str]]:
    """returns the transpose of a matrix"""
    
    m, n = len(matrix), len(matrix[0])
    return [[matrix[j][i] for j in range(m)] for i in range(n)]
  

def main() -> None:
    """__main__ function"""
    
    P, Q = map(int, input("Enter the number of grammys won by Doja Dog and DJ Snack: ").split())
    M, N = map(int, input("Enter M and N: ").split())
    
    skyscrapers = [[i for i in input("Enter row: ")] for _ in range(M)]
    
    print("\nInitial state of FanVille:")
    for row in skyscrapers:
        print("".join(row))
    print()
    
    D = S = 0
    ss_transpose = transpose(skyscrapers)
    copy = ss_transpose.copy()
    
    for i in range(N):
        highest = max(copy)
        height = sum(int(i) for i in highest)
        index = ss_transpose.index(highest)
        
        # select the artist and increase their reputaiton
        if i%2 == 0:
            artist = "D"
            D += height * P
        else:
            artist = "S"
            S += height * Q
        
        # occupy the skyscraper in the transposed matrix
        for j in range(M):
            if ss_transpose[index][j] != "0":
                ss_transpose[index][j] = artist
    
        # remove the highest skyscraper from the copy list
        copy.remove(highest)
        
        # increase the number of grammys    
        P, Q = P+1, Q+1
    
    # take transpose of the transposed matrix to get the original matrix
    skyscrapers = transpose(ss_transpose)
    
    print("Total reputation of Doja Dog:", D)
    print("Total reputation of DJ Snake:", S)
    print("\nFinal state of FanVille:")
    for row in skyscrapers:
        print("".join(row))


if __name__ == "__main__":
    main()