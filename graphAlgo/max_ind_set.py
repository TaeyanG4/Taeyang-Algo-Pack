## taeyang's template (1.0.7)
# https://www.acmicpc.net/problem/2213
# https://velog.io/@heyksw/Python-백준-gold-2213-트리의-독립집합
# https://ko.wikipedia.org/wiki/%EB%8F%85%EB%A6%BD%EC%A7%91%ED%95%A9#cite_note-1
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


def max_ind_set(node):
    
    """
    최대 독립 집합 (maximal independent set)을 구하는 함수
    
        1은 자신을 포함하는 경우, 0은 자신을 포함하지 않는 경우를 뜻한다.
        visited[node] = True 이미 방문한 노드는 다시 방문하지 않도록 한다.
        
        자기자신을 포함하는 경우, 자식 노드는 포함하지 않는다.
        자기자신을 포함하지 않는 경우, 자식 노드는 포함할 수도 있고, 포함하지 않을 수도 있다.
    
    Args:
        node (int): 

    Returns:
        path[node]: 
            path[node][0]: 자신을 포함하지 않는 경우
            path[node][1]: 자신을 포함하는 경우
    """
    
    visited[node] = True
    memo[node][1] += weight[node]
    path[node][1].append(node)
    
    for x in tree[node]:
        if not visited[x]:
            curr_path = max_ind_set(x)
            
            # 자신을 포함하는 경우 
            memo[node][1] += memo[x][0]
            path[node][1].extend(curr_path[0])
            
            # 자신을 포함하지 않는 경우
            max_val_idx = max(enumerate(memo[x]), key=lambda x: x[1])[0]
            memo[node][0] += memo[x][max_val_idx]
            path[node][0].extend(curr_path[max_val_idx])
            
            # 자신을 포함하지 않는 경우 old version (위와 같음)
            # memo[node][0] += max(memo[x]) # max(memo[x][0], memo[x][1])
            # if memo[x][0] > memo[x][1]:
            #     path[node][0].extend(curr_path[0])
            # else:
            #     path[node][0].extend(curr_path[1])
    
    return path[node]

if __name__ == "__main__":
    input = sys.stdin.readline
    S = lambda: map(int, input().split())
    # INF = float('inf')
    # MOD = 10**9 + 7
    # sys.setrecursionlimit(10**6)
    # direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # input
    n = int(input())
    weight = [0] + [*map(int, input().split())]
    tree = defaultdict(list)
    for _ in range(n - 1):
        u, v = S()
        tree[u].append(v)
        tree[v].append(u)
    memo = [[0, 0] for _ in range(n + 1)]
    path = [[[], []] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    # get max independent set
    p_no, p_yes = max_ind_set(1)

    # output
    if memo[1][0] > memo[1][1]:
        print(memo[1][0])
        print(*sorted(p_no))
    else:
        print(memo[1][1])
        print(*sorted(p_yes))
