def verif_y_monotonie(lista):
    for i in range(len(lista)-2):
        if lista[i][1] < lista[i+1][1]:
            return False
    return True

def verif_x_monotonie(lista):
    for i in range(len(lista)-2):
        if lista[i][0] > lista[i+1][0]:
            return False
    return True

n = int(input())
poligon = []
for _ in range(n):
    poligon.append([int(x) for x in input().strip().split()])


y_max = max(poligon, key=lambda x: x[1])
y_min = min(poligon, key=lambda x: x[1])
x_max = max(poligon, key=lambda x: x[0])
x_min = min(poligon, key=lambda x: x[0])


# X-MONOTONIE
a = poligon.index(x_min)
b = poligon.index(x_max)

if a < b:
    varfuri_sus = poligon[a:b+1].copy()
    varfuri_jos = poligon[b:] + poligon[:a+1]
    varfuri_jos = varfuri_jos[::-1]
else:
    varfuri_jos = poligon[a:] + poligon[:b+1]
    varfuri_sus = poligon[b:a+1]
    varfuri_sus = varfuri_sus[::-1]


if verif_x_monotonie(varfuri_jos) and verif_x_monotonie(varfuri_sus):
    print("YES")
else:
    print("NO")


# Y-MONOTONIE
a = poligon.index(y_min)
b = poligon.index(y_max)
if a < b:
    varfuri_dreapta = poligon[a:b+1].copy()
    varfuri_dreapta = varfuri_dreapta[::-1]
    varfuri_stanga = poligon[b:] + poligon[:a+1]
else:
    varfuri_dreapta = poligon[a:] + poligon[:b+1]
    varfuri_stanga = poligon[b:a+1].copy()
    varfuri_dreapta = varfuri_dreapta[::-1]

if verif_y_monotonie(varfuri_stanga) and verif_y_monotonie(varfuri_dreapta):
    print("YES")
else:
    print("NO")

