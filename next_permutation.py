## taeyang's template (1.0.7)
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


def solution(lst):
    for i in range(n-1, 0, -1):
        if lst[i-1] < lst[i]:
            for j in range(n-1, 0, -1):
                if lst[i-1] < lst[j]:
                    lst[i-1], lst[j] = lst[j], lst[i-1]
                    lst = lst[:i] + sorted(lst[i:])
                    return lst
    return [-1]


if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    n = int(input())
    lst = [*map(int, input().split())]
    
    # output
    print(*solution(lst))