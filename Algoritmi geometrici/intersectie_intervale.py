import sys

n = int(input())

lx = []
ly = []
for _ in range(n):
    a, b, c = [int(x) for x in input().strip().split()]
    if a == 0:
        ly.append([b, c])
    if b == 0:
        lx.append([a, c])

stanga = -sys.maxsize - 1
dreapta = sys.maxsize
count_stanga = 0
count_dreapta = 0
for a, c in lx:
    if a > 0:
        if stanga < (0 - c) / a:
            stanga = (0 - c) / a
            count_stanga += 1
    else:
        if dreapta > (0 - c) / a:
            dreapta = (0 - c) / a
            count_dreapta += 1

if stanga > dreapta or (count_dreapta > 1 and count_stanga == 0) or (count_stanga > 1 and count_dreapta == 0):
    intersectie_verticala = True
else:
    intersectie_verticala = False

sus = sys.maxsize
jos = -sys.maxsize - 1
count_sus = 0
count_jos = 0
for b, c in ly:
    if b > 0:
        if jos < (0 - c) / b:
            jos = (0 - c) / b
            count_jos += 1
    else:
        if sus > (0 - c) / b:
            sus = (0 - c) / b
            count_sus += 1

if jos > sus or (count_jos > 1 and count_sus == 0) or (count_sus > 1 and count_jos == 0):
    intersectie_orizontala = True
else:
    intersectie_orizontala = False


if not intersectie_orizontala and not intersectie_verticala:
    print("VOID")
elif (not intersectie_orizontala and intersectie_verticala) or (intersectie_orizontala and not intersectie_verticala):
    print("UNBOUNDED")
elif intersectie_verticala and intersectie_orizontala:
    print("BOUNDED")

