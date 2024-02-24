"""
    LCA란 Lowest Common Ancestor의 약자로, 최소 공통 조상이라고 한다.
    가장 가까운 공통 조상(Nearest Common Anscestor)을 구하는 알고리즘이다.
    시간복잡도는 O(logN)이며 쿼리를 처리하는데 O(MlogN)이 걸린다.

        위키: https://namu.wiki/w/LCA
        동빈나 유튜브: https://www.youtube.com/watch?v=O895NbxirM8
        백준 LCA 기본문제: https://www.acmicpc.net/problem/3584 (가장 가까운 공통 조상)
        백준 LCA 기본문제2: https://www.acmicpc.net/problem/11437 (LCA)
        백준 LCA 기본문제3: https://www.acmicpc.net/problem/11438 (LCA2)
        https://www.crocus.co.kr/660 (LCA(Lowest Common Ancestor) 알고리즘이란?)
        https://blog.naver.com/amazingspidy/222997482394
        https://bbbyung2.tistory.com/75
    
    # 이진 높이 점프 (Binary Lifting)를 사용한 효율적인 방법.
    # 개선된 LCA 관련 정보 (시간복잡도: O(logN))
        동빈나 유튜브: https://www.youtube.com/watch?v=O895NbxirM8
        https://bbbyung2.tistory.com/76
        https://everenew.tistory.com/94
    
"""

################################################################################################
# targetA와 targetB의 LCA를 구하는 함수
# https://ddiyeon.tistory.com/8
# 부모를 알때 사용하는 방법
# 시간복잡도: O(N)

import sys
from collections import *

def lca_basic(a, b):
    parentA, parentB = [a], [b]
    
    # 각 노드의 부모 노드를 루트 노드까지 찾아서 저장
    while parent[a]:
        parentA.append(parent[a])
        a = parent[a]
    
    while parent[b]:
        parentB.append(parent[b])
        b = parent[b]

    # 같은 레벨로 맞춰줌
    levelA, levelB = len(parentA) - 1, len(parentB) - 1
    
    # 루트 노드부터 내려오면서 부모 노드가 같은지 확인 
    while parentA[levelA] == parentB[levelB]:
        levelA -= 1
        levelB -= 1
    
    return parentA[levelA + 1]

################################################################################################
# https://www.acmicpc.net/problem/11437 (LCA)
# 시간복잡도: O(N)
import sys
from collections import *

def dfs_simple(node, depth):
    
    visited[node] = True
    level[node] = depth
    for child in graph[node]:
        if not visited[child]:
            parent[child] = node
            dfs_simple(child, depth + 1)

def lca_simple(a, b):
    
    if level[a] > level[b]:
        a, b = b, a
    
    # 깊이가 다르면 같은 깊이로 맞춰줌
    while level[a] != level[b]:
        b = parent[b]
    
    # 같은 깊이로 맞춰줬는데 같은 노드면 그게 LCA 아니라면 부모로 올라감
    while a != b:
        a = parent[a]
        b = parent[b]
        
    return a

################################################################################################
# https://www.acmicpc.net/problem/11438 (LCA2)
# 시간복잡도: O(logN)
import sys
import math
from collections import *

def dfs(node, depth):
    
    visited[node] = True # 방문 여부
    level[node] = depth # 노드의 깊이를 저장
    for child in graph[node]:
        if not visited[child]:
            parent[child][0] = node # 부모 노드를 저장
            dfs(child, depth + 1)

# sparse table를 이용하여 모든 노드의 2^i번째 부모 노드를 찾는다.
def set_parent():
    
    # 2^0번째 부모 노드 찾기
    dfs(1, 0) # 루트, 깊이
    
    # set_sparse_table
    # 각 노드의 2^i번째 부모 노드를 찾는다.
    for i in range(1, int(math.log2(n) + 1)):
        for j in range(1, n + 1):
            # 각 노드의 2^i번째 부모 노드는 2^(i - 1)번째 부모 노드의 2^(i - 1)번째 부모 노드와 같다.
            parent[j][i] = parent[parent[j][i-1]][i-1]

def lca(a, b):
    
    # b가 더 깊도록 설정
    if level[b] < level[a]:
        a, b = b, a
    
    # level[b] - level[a]가 0이 될 때까지 올라간다.(level[b] - level[a]가 0이면 두 노드의 깊이가 같다는 뜻이다.)
    for i in range(int(math.log2(n)), -1, -1):
        if level[b] - level[a] >= (1 << i): # (1 << i) == 2^i
            b = parent[b][i]
    
    # 두 노드가 같으면 LCA를 찾은 것이다.
    if a == b:
        return a
    
    # 두 노드가 같아지도록 올라간다.
    for i in range(int(math.log2(n)), -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    
    return parent[a][0]

################################################################################################
################################################################################################

if __name__ == "__main__":
    input = sys.stdin.readline
    
    ########################################################
    # 백준 LCA 기본문제: https://www.acmicpc.net/problem/3584 (가장 가까운 공통 조상)
    # lca_simple
    
    t = int(input()) # test case

    for _ in range(t):
        
        # input
        n = int(input()) # node count
        parent = [0] * (n + 1)
        for _ in range(n - 1):
            a, b = map(int, input().split())
            parent[b] = a
        
        targetA, targetB = map(int, input().split())
        
        # output
        print(lca_basic(targetA, targetB))
        
    ########################################################
    ########################################################
    # 백준 LCA 기본문제2: https://www.acmicpc.net/problem/11437 (LCA)
    
    # input
    n = int(input()) # node count
    parent = [0] * (n + 1) # 부모 노드
    level = [0] * (n + 1) # 노드의 깊이
    visited = [False] * (n + 1) # 방문 여부
    graph = defaultdict(list)
    
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    # set parent and level
    dfs_simple(1, 0) # 루트, 깊이
    
    # output
    m = int(input()) # target count
    for _ in range(m):
        targetA, targetB = map(int, input().split())
        print(lca_basic(targetA, targetB))
        
    ########################################################
    ########################################################
    # 백준 LCA 기본문제3: https://www.acmicpc.net/problem/11438 (LCA2)
    
    # input
    n = int(input()) # node count
    parent = [[0] * int(math.log2(n) + 1) for _ in range(n + 1)] # log2(n) + 1만큼 부모를 저장
    level = [0] * (n + 1) # 노드의 깊이
    visited = [False] * (n + 1) # 방문 여부
    graph = defaultdict(list)
    
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    # set parent and level
    set_parent()
    
    # output
    m = int(input()) # target count
    for _ in range(m):
        targetA, targetB = map(int, input().split())
        print(lca_basic(targetA, targetB))
        
    ########################################################
    
################################################################################################
################################################################################################
## lca_simple 예제 입력
# 2
# 16
# 1 14
# 8 5
# 10 16
# 5 9
# 4 6
# 8 4
# 4 10
# 1 13
# 6 15
# 10 11
# 6 7
# 10 2
# 16 3
# 8 1
# 16 12
# 16 7
# 5
# 2 3
# 3 4
# 3 1
# 1 5
# 3 5

## lca, lca2 예제 입력
# 15
# 1 2
# 1 3
# 2 4
# 3 7
# 6 2
# 3 8
# 4 9
# 2 5
# 5 11
# 7 13
# 10 4
# 11 15
# 12 5
# 14 7
# 6
# 6 11
# 10 9
# 2 6
# 7 6
# 8 13
# 8 15