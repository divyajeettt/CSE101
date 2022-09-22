def smallest_two(l):
    if len(l) == 2:
        return l
    else:
        lar = 0
        for i in range(len(l)):
            if l[i] > l[lar]:
                lar = i
        return smallest_two(l[:lar] + l[lar+1:])


l = list(int(i) for i in input().split())
print(smallest_two(l))