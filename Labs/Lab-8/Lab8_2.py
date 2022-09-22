stored = {0: 0, 1: 0, 2: 1}

def tribonacci(n):
    """recursive function to return the n-th tribonacci number"""
    
    if n > 40:
        return "Invalid Input"
    if n in (0, 1, 2):
        return stored[n]
    else:
        if n in stored:
            return stored[n]
        else:
            x = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
            stored[n] = x
            return x


x = int(input())
print(tribonacci(x))