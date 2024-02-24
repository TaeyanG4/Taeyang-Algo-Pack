## 참고했던 자료글들
# 선분 교차1
# https://velog.io/@jini_eun/백준-17386번-선분-교차-1-Java-Python

# 선분 교차2
# https://johoonday.tistory.com/107
# https://hsdevelopment.tistory.com/390

# 선분 교차3
# https://yiyj1030.tistory.com/508
# https://fusionit.tistory.com/46 # 직선 방정식을 이용한 풀이

# 선분 그룹
# https://velog.io/@sunkyuj/@sunkyuj/python-백준-2162-선분-그룹

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
        return iter((self.p1, self.p2))

###########################################
# p1, p2, p3가 반시계 방향이면 양수, 시계 방향이면 음수, 일직선이면 0
def ccw(p1: Point, p2: Point, p3: Point) -> float:
    return ((p2.x - p1.x) * (p3.y - p1.y)) - ((p2.y - p1.y) * (p3.x - p1.x))


# ccw 벡터의 외적을 이용한 방법 (선분이 겹칠 경우)
def ccw_direction(p1: Point, p2: Point, p3: Point) -> int:
    
    # 두 벡터의 외적을 구하면 두 벡터가 이루는 사각형의 넓이가 나온다.
    dx1, dy1 = p2.x - p1.x, p2.y - p1.y # p1 -> p2
    dx2, dy2 = p3.x - p1.x, p3.y - p1.y # p1 -> p3
    
    # ((p2.x - p1.x) * (p3.y - p1.y)) - ((p2.y - p1.y) * (p3.x - p1.x))과 본질은 비슷하다 '-'자리에 >, <, =를 넣어서 방향을 구한다.
    if dx1 * dy2 > dy1 * dx2:
        return 1
    elif dx1 * dy2 < dy1 * dx2:
        return -1
    else:
        # p1와 p2가 같은 위치에 있을 경우 (점)
        if dx1 == 0 and dy1 == 0:
            return 0
        # p1을 기준으로 p2와 p3가 서로 반대 방향에 있을 경우 예) p2 <-> p1 <-> p3
        elif (dx1 * dx2 < 0) or (dy1 * dy2 < 0):
            return -1
        # p1에서 p3까지의 거리가 p1에서 p2까지의 거리보다 길다면 1을 반환 p1 <-> p2 -/- p3
        elif (dx1 * dx1 + dy1 * dy1) < (dx2 * dx2 + dy2 * dy2):
            return 1
        else:
            return 0
###########################################


###########################################
# ccw_direction과 intersect_base를 조합해서 사용하면 intersect보다 빠르다.
def intersect_base(line1: Line, line2: Line) -> bool:
    A, B = line1
    C, D = line2
    # if ccw(A, B, C) * ccw(A, B, D) <= 0 and ccw(C, D, A) * ccw(C, D, B) <= 0: # ccw_direction() 사용시
    if ccw(A, B, C) * ccw(A, B, D) < 0 and ccw(C, D, A) * ccw(C, D, B) < 0:
        return True
    else:
        return False


def intersect_simple(l1, l2):
    p1, p2 = l1
    p3, p4 = l2
    ab = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    cd = ccw(p3, p4, p1) * ccw(p3, p4, p2)
    if ab == 0 and cd == 0:
        if p1 > p2:
            p1, p2 = p2, p1
        if p3 > p4:
            p3, p4 = p4, p3
        return p3 <= p2 and p1 <= p4
    return ab <= 0 and cd <= 0


def intersect(line1: Line, line2: Line) -> bool:
    
    A, B = line1
    C, D = line2
    
    # 평행할 경우 리턴값이 0이다.
    ccwABC = ccw(A, B, C)
    ccwABD = ccw(A, B, D)
    ccwCDA = ccw(C, D, A)
    ccwCDB = ccw(C, D, B)
    
    # 두 선분중 하나의 선분의 작은 끝점이 다른 선분의 끝점보다 크거나 같아야 하고
    # 두 선분중 하나의 선분의 큰 끝점이 다른 선분의 끝점보다 작거나 같아야 겹친다.
    mx1, my1,  = min(A.x, B.x), min(A.y, B.y)
    mx2, my2,  = max(A.x, B.x), max(A.y, B.y)
    mx3, my3,  = min(C.x, D.x), min(C.y, D.y)
    mx4, my4,  = max(C.x, D.x), max(C.y, D.y)
    
    # for debugging
    # print(ccwABC, ccwABD, ccwCDA, ccwCDB)
    # print(mx1, my1, mx2, my2, mx3, my3, mx4, my4)
    
    # 평행하는 경우
    if ccwABC * ccwABD == 0 and ccwCDA * ccwCDB == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4  and my3 <= my2:
            return True
    
    # 교차하는 경우
    else:
        if ccwABC * ccwABD <= 0 and ccwCDA * ccwCDB <= 0:
            return True
    
    return False

# 주석 없는 버전
def intersect(line1: Line, line2: Line) -> bool:
    
    A, B = line1
    C, D = line2
    
    ccwABC = ccw(A, B, C)
    ccwABD = ccw(A, B, D)
    ccwCDA = ccw(C, D, A)
    ccwCDB = ccw(C, D, B)
    
    mx1, my1,  = min(A.x, B.x), min(A.y, B.y)
    mx2, my2,  = max(A.x, B.x), max(A.y, B.y)
    mx3, my3,  = min(C.x, D.x), min(C.y, D.y)
    mx4, my4,  = max(C.x, D.x), max(C.y, D.y)
    
    if ccwABC * ccwABD == 0 and ccwCDA * ccwCDB == 0:
        if mx1 <= mx4 and mx3 <= mx2 and my1 <= my4  and my3 <= my2:
            return True
    else:
        if ccwABC * ccwABD <= 0 and ccwCDA * ccwCDB <= 0:
            return True
    
    return False
###########################################


###########################################
# 기울기 비교 함수
def slope_comparison(line1, line2):
    """
        기울기1 = x2-x1 / y2-y1
        기울기2 = x4-x3 / y4-y3
        x2-x1 / y2-y1 = x4-x3 / y4-y3
        (y2-y1)*(x4-x3)=(y4-y3)*(x2-x1)
    """
    p1, p2 = line1
    p3, p4 = line2
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    if (x4 - x3) * (y2 - y1) == (x2 - x1) * (y4 - y3):
        return True
    else:
        return False
###########################################


###########################################
# 교차점 좌표 구하기
def get_intersect_point(line1: Line, line2: Line) -> Point:
    
    A, B = line1
    C, D = line2
    A, B, C, D = tuple(A), tuple(B), tuple(C), tuple(D)
    x1, y1, x2, y2, x3, y3, x4, y4 = A + B + C + D
    
    if slope_comparison(line1, line2): # 기울기 비교
        if max(x1, x2) == min(x3, x4) or max(x3, x4) == min(x1, x2): # 한 점일 경우
            if A in [C, D]:
                print(*A)
            elif B in [C, D]:
                print(*B)
    else:
        A, B = line1
        C, D = line2
        
        # 두 직선의 방정식
        a1 = B.y - A.y
        b1 = A.x - B.x
        c1 = a1 * A.x + b1 * A.y
        
        a2 = D.y - C.y
        b2 = C.x - D.x
        c2 = a2 * C.x + b2 * C.y
        
        # Cramer의 규칙 (행렬식); 0이면 평행, 아니면 교차
        determinant = a1 * b2 - a2 * b1
        if determinant == 0:
            return None
        else:
            x = (b2 * c1 - b1 * c2) / determinant
            y = (a1 * c2 - a2 * c1) / determinant
            return x, y
###########################################