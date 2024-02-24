class Point:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y
    
    # self.x, self.y를 반환 (x, y = point1)
    def __iter__(self):
        return iter((self.x, self.y))
        
class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1, self.p2 = p1, p2
    
    # self.p1, self.p2를 반환 (p1, p2 = line1)
    def __iter__(self):
        return iter((self.x, self.y))
    
###########################################
def slope(x1, y1, x2, y2):
    if x1 == x2:  # 분모가 0이 되는 경우
        return float('inf')  # 무한대를 반환 (수직선의 경우)
    return (y2 - y1) / (x2 - x1)

# 기울기 비교 함수
def slope_comparison_simple(x1, y1, x2, y2, x3, y3, x4, y4):
    """
        기울기1 = x2-x1 / y2-y1
        기울기2 = x4-x3 / y4-y3
        x2-x1 / y2-y1 = x4-x3 / y4-y3
        (y2-y1)*(x4-x3)=(y4-y3)*(x2-x1)
    """
    if (x4 - x3) * (y2 - y1) == (x2 - x1) * (y4 - y3):
        return True
    else:
        return False
    
x1, y1, x2, y2 = 1, 2, 3, 4
print(slope(x1, y1, x2, y2))
