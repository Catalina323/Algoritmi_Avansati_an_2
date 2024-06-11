
def verificare_punct(x1, y1, x2, y2, x3, y3, x4, y4):
    det = ((x1 - x4) * ((y2 - y4) * (x3 * x3 + y3 * y3 - x4 * x4 - y4 * y4) - (y3 - y4) * (x2 * x2 + y2 * y2 - x4 * x4 - y4 * y4)) -
           (x2 - x4) * ((y1 - y4) * (x3 * x3 + y3 * y3 - x4 * x4 - y4 * y4) - (y3 - y4) * (x1 * x1 + y1 * y1 - x4 * x4 - y4 * y4)) +
           (x3 - x4) * ((y1 - y4) * (x2 * x2 + y2 * y2 - x4 * x4 - y4 * y4) - (y2 - y4) * (x1 * x1 + y1 * y1 - x4 * x4 - y4 * y4)))

    if det == 0:
        print("BOUNDARY")
    elif det > 0:
        print("INSIDE")
    else:
        print("OUTSIDE")


# CITIRE DATE:

x1, y1 = [int(x) for x in input().strip().split()]
x2, y2 = [int(x) for x in input().strip().split()]
x3, y3 = [int(x) for x in input().strip().split()]

n = int(input())
list = []
for _ in range(n):
    list.append([int(x) for x in input().strip().split()])

for point in list:
    verificare_punct(x1, y1, x2, y2, x3, y3, point[0], point[1])
