# https://www.acmicpc.net/problem/1197 (최소 스패닝 트리)
# MST (Minimum Spanning Tree)를 구하는 알고리즘
# kruskal algorithm

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a, b = find(a), find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

def kruskal():
    
    # Kruskal algorithm
    ans = 0
    elist.sort(key=lambda x: x[2])
    for s, e, w in elist:
        sroot, eroot = find(s), find(e)
        if sroot != eroot:
            union(s, e)
            ans += w
    return ans
        
if __name__ == '__main__':
    
    # input
    v, e = map(int, input().split())
    parents = [i for i in range(v + 1)]
    elist = []
    for _ in range(e):
        a, b, w = map(int, input().split()) # start, end, weight
        elist.append((a, b, w))
    
    # output
    print(kruskal())