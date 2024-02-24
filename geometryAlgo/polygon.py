## taeyang's template (1.0.7)
# https://www.acmicpc.net/problem/2166
# https://ko.wikihow.com/다각형-넓이-구하기#:~:text=정다각형의%20넓이를%20구,의%20중심으로%20모이는%20선분
# https://ko.wikipedia.org/wiki/%EC%8B%A0%EB%B0%9C%EB%81%88_%EA%B3%B5%EC%8B%9D
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

# area = 1/2 * | ∑_i=1^n-1 (xiyi+1 + xny1) - ∑_i=1^n-1 (xi+1yi + x1yn) |
def get_polygon_area(n, node):

    # 신발끈 공식
    x, y = [], []
    for i in range(n):
        
        # 각 꼭지점의 좌표를 y, x에 저장
        x.append(node[i][0])
        y.append(node[i][1])
    
    # 첫번째 꼭지점을 마지막에 추가
    x.append(x[0])
    y.append(y[0])
    
    # 신발끈 공식 적용
    xy, yx = 0, 0
    for i in range(n):
        xy += x[i] * y[i+1]
        yx += y[i] * x[i+1]
    
    return abs(xy-yx) / 2

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    n = int(input())
    node = []
    for _ in range(n):
        node.append([*map(int, input().split())])

    # output
    print(round(get_polygon_area(n, node), 1))
