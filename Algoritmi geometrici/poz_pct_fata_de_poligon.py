def orientare(px, py, qx, qy, rx, ry):
    d = (px - rx) * (qy - ry) - (py - ry) * (qx - rx)
    left = 0
    right = 0
    touch = 0
    if d > 0:
        left = 1
    if d < 0:
        right = 1
    if d == 0:
        touch = 1
    return left, right, touch

def intersectie(p1, p2, ext, pct):

    a1, b1, c1 = orientare(p1[0], p1[1], p2[0], p2[1], ext[0], ext[1])
    if c1:
        ext[0] += 1
        a1, b1, c1 = orientare(p1[0], p1[1], p2[0], p2[1], ext[0], ext[1])

    a2, b2, c2 = orientare(p1[0], p1[1], p2[0], p2[1], pct[0], pct[1])
    
    if c2:
        x_min = min(p1[0], p2[0])
        x_max = max(p1[0], p2[0])
        y_min = min(p1[1], p2[1])
        y_max = max(p1[1], p2[1])
        if pct[0] <= x_max and pct[0] >= x_min and pct[1] <= y_max and pct[1] >= y_min:
            return "boundary"
    
    a3, b3, c3 = orientare(ext[0], ext[1], pct[0], pct[1], p1[0], p1[1])
    a4, b4, c4 = orientare(ext[0], ext[1], pct[0], pct[1], p2[0], p2[1])

    if a1 != a2 and b1 != b2 and a3 != a4 and b3 != b4:
        return "intersect"

    # returneaza boundary atunci cand pct se afla pe segmentul p1p2

    return False


n = int(input())
poligon = []
for _ in range(n):
    poligon.append([int(x) for x in input().strip().split()])

m = int(input())
pct = []
for _ in range(m):
    pct.append([int(x) for x in input().strip().split()])

# n = 12
# m = 1
# poligon = [[0, 6], [0, 0], [6, 0], [6, 6], [2, 6], [2, 2], [4, 2], [4, 5], [5, 5], [5, 1], [1, 1], [1, 6]]
# pct = [[-1, 1]]


ext = [max(poligon)[0] * 11, max(poligon)[1] * 7]

for punct in pct:
    count = 0
    for i in range(len(poligon)):
        p1 = poligon[i]
        p2 = poligon[(i + 1) % n]
        f = intersectie(p1, p2, ext, punct)
        if f == "intersect":
            count += 1
        if f == "boundary":
            count = -1
            break
    if count == -1:
        print("BOUNDARY")
    else:
        if count % 2 == 0:
            print("OUTSIDE")
        else:
            print("INSIDE")
