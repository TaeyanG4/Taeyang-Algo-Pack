import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def dist(p1, p2):
    return ((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2) ** 0.5

# 예제
x1, y1 = (1, 2)
x2, y2 = (4, 6)
print(distance(x1, y1, x2, y2))
