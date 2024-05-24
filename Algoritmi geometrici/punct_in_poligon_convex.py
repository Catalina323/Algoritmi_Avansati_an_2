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

n = int(input())
poligon = []
for _ in range(n):
    poligon.append([int(x) for x in input().strip().split()])

m = int(input())
pct = []
for _ in range(m):
    pct.append([int(x) for x in input().strip().split()])

# n = 8
# poligon = [[0, 0], [10, 0], [10, 2], [10, 5], [10, 10], [0, 10], [0, 5], [0, 2]]
# m = 2
# pct = [[0, 3], [5, 10]]


m = min(poligon, key=lambda x:(x[0], -x[1]))

lista_unghiuri = []
poligon_ordine = poligon[poligon.index(m):] + poligon[:poligon.index(m)]

def calc_produs_vect(m, punct, q):
    return (punct[0]-m[0]) * (q[1] - m[1]) - (q[0] - m[0]) * (punct[1] - m[1])

maxim_sup = max(poligon, key=lambda x:x[1])
minim_inf = min(poligon, key=lambda x:x[1])
maxim_dreapta = max(poligon, key=lambda x:x[0])
for q in pct:
    # verificam daca punctul e in afara poligonului (verificare cu coordonatele punctelor din margine)

    if q[0] < m[0] or maxim_sup[1] < q[1] or minim_inf[1] > q[1] or maxim_dreapta[0] < q[0]:
        print("OUTSIDE")
        continue

    #cautare binara:
    s = 0
    d = len(poligon)
    while d - s > 1:
        mij = (s+d)//2
        if calc_produs_vect(m, poligon[mij], q) > 0:
            s = mij
        else:
            d = mij
    # punctul cautat e s :)))

    a, b, c = orientare(poligon[s][0], poligon[s][1], poligon[(s+1) % len(poligon)][0], poligon[(s+1) % len(poligon)][1], q[0], q[1])
    if a:
        aa, bb, cc = orientare(poligon[(s+1)%len(poligon)][0], poligon[(s+1)%len(poligon)][1], poligon[(s+2)%len(poligon)][0], poligon[(s+2)%len(poligon)][1], q[0], q[1])
        aaa, bbb, ccc = orientare(poligon[(s-1)%len(poligon)][0], poligon[(s-1)%len(poligon)][1], poligon[s][0], poligon[s][1], q[0], q[1])
        if cc or ccc:
            print("BOUNDARY")
            continue
        print("INSIDE")
    if c:
        print("BOUNDARY")
    if b:
        print("OUTSIDE")
