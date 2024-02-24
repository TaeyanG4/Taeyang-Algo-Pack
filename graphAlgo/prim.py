# https://www.acmicpc.net/problem/1197 (최소 스패닝 트리)
# MST (Minimum Spanning Tree)를 구하는 알고리즘
# Prim algorithm

from collections import *
from heapq import *

def prim():
    
    # Prim algorithm
    ans, cnt = 0, 0
    while pq:
        if cnt == v:
            break
        w, s = heappop(pq)
        if not visited[s]:
            visited[s] = True
            ans += w
            cnt += 1
            for i in elist[s]:
                heappush(pq, i)
                
    return ans

if __name__ == '__main__':
    
    # Prim algorithm
    # input
    v, e = map(int, input().split())
    visited = [False] * (v + 1)
    elist = [[] for _ in range(v + 1)]
    pq = [[0, 1]]
    for _ in range(e):
        s, e, w = map(int, input().split())
        elist[s].append([w, e])
        elist[e].append([w, s])
    
    # output
    print(prim())