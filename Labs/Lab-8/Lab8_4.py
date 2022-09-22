def combs(L, r):
    """returns all combinations of L with size r"""
    
    if len(L) == 1 or r == 1:
        return [{i} for i in L]
    
    combinations = []
    for i in L:
        copy = L.copy()
        copy.remove(i)
        for j in combs(copy, r-1):
            try:
                ele = set([i, *j])
            except TypeError:
                ele = set([i, j])
            if ele not in combinations:
                combinations.append(ele)

    return combinations


l = list(int(i) for i in input().split())
r = int(input())
print(combs(l, r))