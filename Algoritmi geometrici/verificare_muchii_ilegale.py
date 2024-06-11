def verificare_punct(x1, y1, x2, y2, x3, y3, x4, y4):
    det = ((x1 - x4) * ((y2 - y4) * (x3 * x3 + y3 * y3 - x4 * x4 - y4 * y4) - (y3 - y4) * (x2 * x2 + y2 * y2 - x4 * x4 - y4 * y4)) -
           (x2 - x4) * ((y1 - y4) * (x3 * x3 + y3 * y3 - x4 * x4 - y4 * y4) - (y3 - y4) * (x1 * x1 + y1 * y1 - x4 * x4 - y4 * y4)) +
           (x3 - x4) * ((y1 - y4) * (x2 * x2 + y2 * y2 - x4 * x4 - y4 * y4) - (y2 - y4) * (x1 * x1 + y1 * y1 - x4 * x4 - y4 * y4)))

    return det


# CITIRE DATE:

ax, ay = [int(x) for x in input().strip().split()]
bx, by = [int(x) for x in input().strip().split()]
cx, cy = [int(x) for x in input().strip().split()]
dx, dy = [int(x) for x in input().strip().split()]


if verificare_punct(ax, ay, bx, by, cx, cy, dx, dy) > 0:
    print("AC: ILLEGAL")
else:
    print("AC: LEGAL")

if verificare_punct(ax, ay, dx, dy, cx, cy, bx, by) > 0:
    print("BD: ILLEGAL")
else:
    print("BD: LEGAL")
