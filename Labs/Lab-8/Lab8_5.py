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
            combinations.append(ele)

    return combinations


def possible(l, d):
    combinations = []
    for i in range(1, len(l)+1):
        combinations.extend(combs(l, i))
    
    for sub1 in combinations:
        for sub2 in combinations:
            n1, n2 = len(sub1), len(sub2)
            if (n1 + n2 != n) or sub1.intersection(sub2):
                continue
            if sum(sub1) - sum(sub2) == d:
                return True
    
    return False


n = int(input())
l = [int(i) for i in input().split()]
d = int(input())

if possible(l, d):
    print("Yes")
else:
    print("No")