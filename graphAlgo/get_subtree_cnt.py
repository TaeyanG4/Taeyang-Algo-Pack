## taeyang's template (1.0.7)
# https://www.acmicpc.net/problem/2213 # 트리와 쿼리
# https://jainn.tistory.com/74
## my import lines
import sys
import math
# import copy
# import ast
# import re
# import time
# import json
# import pprint
from collections import *
# from heapq import *
# from queue import PriorityQueue
# from itertools import *
# from statistics import *
# from datetime import *
# from bisect import *
# from fractions import Fraction
# from decimal import *
#################################

def get_subtree_cnt(x):
    cnt[x] = 1
    for i in graph[x]:
        if not cnt[i]:
            cnt[x] += get_subtree_cnt(i) # 서브트리의 노드 개수를 구하기위한 dfs
    return cnt[x]

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # sys.setrecursionlimit(10**6)
    
    # input
    n, r, q = map(int, input().split()) # n: 정점의 개수, r: 루트 노드, q: 쿼리의 개수
    cnt = [0] * (n+1)
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    get_subtree_cnt(r) # r을 루트로 하는 트리의 서브트리의 노드 개수를 구함
    
    for _ in range(q):
        
        # output
        print(cnt[int(input())])

## input 1
# 9 5 3 # n: 정점의 개수, r: 루트 노드, q: 쿼리의 개수
# 1 3
# 4 3
# 5 4
# 5 6
# 6 7
# 2 3
# 9 6
# 6 8
# 5
# 4
# 8