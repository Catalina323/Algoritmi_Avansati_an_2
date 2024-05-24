# metoda dreptei de baleiere
# algoritm netestat (posibil cu buguri)

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


def caz_2(stiva):
    if len(stiva) > 2:
        a, b, c = orientare(stiva[-3][0], stiva[-3][1], stiva[-2][0], stiva[-2][1], stiva[-1][0], stiva[-1][1])
        if a:
            # caz 2 a
            pass
        if b:
            # caz 2 b
            stiva.pop(len(stiva)-2)
            ok = True
            while(ok and len(stiva) > 2):
                a, b, c = orientare(stiva[-3][0], stiva[-3][1], stiva[-2][0], stiva[-2][1], stiva[-1][0], stiva[-1][1])
                if b:
                    stiva.pop(len(stiva)-2)
                else:
                    ok = False

def caz_1(stiva, side):
    if side == "d":
        lista = varfuri_stanga
    elif side == "s":
        lista = varfuri_dreapta
    else:
        return
    while len(stiva) > 2 and stiva[-2] in lista:
        stiva.pop(-2)
    return


def monotonie(n, poligon):
    stiva = []
    last_side = ""
    for punct in poligon:
        stiva.append(punct)
        if punct in varfuri_dreapta:
            if last_side == "d":
                caz_2(stiva)
            else:
                caz_1(stiva, "d")
                last_side = "d"
        if punct in varfuri_stanga:
            if last_side == "s":
                caz_2(stiva)
            else:
                caz_1(stiva, "s")
                last_side = "s"

    if len(stiva) == 2:
        return "YES"
    else:
        return "NO"


n = int(input())
poligon = []
for _ in range(n):
    poligon.append([int(x) for x in input().strip().split()])

# n = 8
# poligon = [[-3, -1], [-1, -4], [9, -2], [7, 1], [4, 2], [2, 4], [1, 8], [-2, 6]]


varfuri_stanga = []
varfuri_dreapta = []

# y-monotonie
b = poligon.index(max(poligon, key=lambda x: x[1]))
a = poligon.index(min(poligon, key=lambda x: x[1]))
if a < b:
    varfuri_stanga = poligon[a:b].copy()
    varfuri_dreapta = poligon[b:] + poligon[:a]
else:
    varfuri_stanga = poligon[a:] + poligon[:b]
    varfuri_dreapta = poligon[b:a].copy()

poligon_copy = poligon.copy()
poligon_copy.sort(key=lambda x: -x[1])
print(monotonie(n, poligon_copy))

# x-monotonie

b = poligon.index(min(poligon, key=lambda x:x[0]))
a = poligon.index(max(poligon, key=lambda x:x[0]))
if a < b:
    varfuri_stanga = poligon[a:b].copy()
    varfuri_dreapta = poligon[b:] + poligon[:a]
else:
    varfuri_stanga = poligon[a:] + poligon[:b]
    varfuri_dreapta = poligon[b:a].copy()

poligon.sort(key=lambda x: x[0])
print(monotonie(n, poligon))

