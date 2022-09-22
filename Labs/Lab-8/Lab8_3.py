def move_knight(x, y, n):
    """returns a list of positions that a knight can reach in 1 step
    only returns the points that are in the board"""
    
    xm1, xm2, xp1, xp2 = x - 1, x - 2, x + 1, x + 2
    ym1, ym2, yp1, yp2 = y - 1, y - 2, y + 1, y + 2
    
    moves = [
        (xm1, ym2), (xm1, yp2), (xm2, ym1), (xm2, yp1),
        (xp1, ym2), (xp1, yp2), (xp2, ym1), (xp2, yp1)
    ]
    
    return [(i, j) for (i, j) in moves if 0 <= i <= n-1 and 0 <= j <= n-1 ]


def check_knight(x, y, u, v, t, n):
    """returns True if box (u, v) can be reached by a knight starting from (x, y) in t steps"""

    if t == 0:
        return False
    
    answer = False
    moves = move_knight(x, y, n)
    
    if (u, v) in moves:
        return True
    
    for (i, j) in moves:
        next_moves = move_knight(x, y, n)
        answer = answer or check_knight(i, j, u, v, t-1, n)

    return answer

# size of board nxn
n = int(input())    

# initial position (x, y)
x = int(input())
y = int(input())

# final position (u, v)
u = int(input())
v = int(input())

# steps = t
t = int(input())

# pieces
pieces = ["Knight", "Queen", "Bishop", "Rook"]


for piece in pieces:
    answer = ((x, y) == (u, v)) and t >= 0
    
    if piece == "Rook":
        answer = answer or ((x == u or y == v) and t >= 1) or t >= 2
    
    elif piece == "Bishop":
        initial = (x+y) % 2
        final = (u+v) % 2
        if (initial, final) in [(0, 1), (1, 0)]:
            answer = False
        else:
            answer = answer or ((x+y == u+v or x-y == u-v) and t >= 1) or t >= 2
    
    elif piece == "Queen":
        answer = answer or ((x == u or y == v) or (x+y == u+v or x-y == u-v) and t >= 1) or t >= 2
        
    else:
        if not answer:
            answer = check_knight(x, y, u, v, t, n)

    print(f"{piece}: {answer=}")