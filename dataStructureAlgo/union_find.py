# https://www.acmicpc.net/problem/1717 # 집합의 표현

import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def solution():
    for _ in range(m):
        typ, a, b = map(int, input().split())
        if typ == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                print('YES')
            else:
                print('NO')
        
if __name__ == '__main__':
    input = sys.stdin.readline
    
    # input
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    # parent = [find(i) for i in parent] # path compression (경로 압축)

    # output
    print(solution())

# input case
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1