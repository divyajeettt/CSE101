def countNum(array):
    """recursive function to find the length of list"""
    
    if array == []:
        return 0
    else:
        return 1 + countNum(array[1:])


l = list(int(i) for i in input().split())
print(countNum(l))