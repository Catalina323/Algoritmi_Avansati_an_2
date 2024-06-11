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


stanga = sys.maxsize
dreapta = -sys.maxsize -1
count_stanga = 0
count_dreapta = 0
for a, c in lx:
    if a > 0:
        count_stanga += 1
        if stanga > (0 - c) / a:
            stanga = (0 - c) / a
    else:
        count_dreapta += 1
        if dreapta < (0 - c) / a:
            dreapta = (0 - c) / a


infinit = False
infinit2 = False

if (count_stanga == 1 and count_dreapta == 0) or (count_stanga == 0 and count_dreapta == 1):
    intersectie_verticala = False
    infinit = True
else:
    if stanga > dreapta or (count_dreapta > 1 and count_stanga == 0) or (count_stanga > 1 and count_dreapta == 0):
        intersectie_verticala = True
        if (count_dreapta > 1 and count_stanga == 0) or (count_stanga > 1 and count_dreapta == 0):
            infinit = True
    else:
        intersectie_verticala = False

sus = -sys.maxsize -1
jos = sys.maxsize
count_sus = 0
count_jos = 0
for b, c in ly:
    if b > 0:
        count_jos += 1
        if jos > (0 - c) / b:
            jos = (0 - c) / b
    else:
        count_sus += 1
        if sus < (0 - c) / b:
            sus = (0 - c) / b

if (count_jos == 1 and count_sus == 0) or (count_jos == 0 and count_sus == 1):
    intersectie_orizontala = False
    infinit2 = True
else:
    if jos > sus or (count_jos > 1 and count_sus == 0) or (count_sus > 1 and count_jos == 0):
        intersectie_orizontala = True
        if (count_jos > 1 and count_sus == 0) or (count_sus > 1 and count_jos == 0):
            infinit2 = True
    else:
        intersectie_orizontala = False


if not intersectie_orizontala and not intersectie_verticala:
    print("VOID")
elif (not intersectie_orizontala and intersectie_verticala) or (intersectie_orizontala and not intersectie_verticala):
    print("UNBOUNDED")
elif intersectie_verticala and intersectie_orizontala:
    if infinit or infinit2:
        print("UNBOUNDED")
    else:
        print("BOUNDED")

