## taeyang's template (1.0.7)
# https://www.acmicpc.net/problem/11758
#################################
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
# from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################

class Point:
    def __init__(self, x: int, y: int):
        self.x, self.y = x, y

# class Line:
#     def __init__(self, p1: Point, p2: Point):
#         self.p1, self.p2 = p1, p2
        
# p1, p2, p3가 반시계 방향이면 양수, 시계 방향이면 음수, 일직선이면 0
def ccw(p1: Point, p2: Point, p3: Point) -> int:
    return ((p2.x - p1.x) * (p3.y - p1.y)) - ((p2.y - p1.y) * (p3.x - p1.x))

# p1, p2, p3가 반시계 방향이면 양수, 시계 방향이면 음수, 일직선이면 0
def ccw_simple(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

def ccw_basic1(node):
    
    x1, y1 = node[0]
    x2, y2 = node[1]
    x3, y3 = node[2]
    
    res = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        return 0

def ccw_basic2(p1, p2, p3):
    
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    
    res = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        return 0

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    # n, m = map(int, input().split())
    # lst = [*map(int, input().split())]
    # n = int(input())
    
    # input
    node = []
    for _ in range(3):
        node.append(list(map(int, input().split())))

    # output
    print(ccw_basic1(node))
