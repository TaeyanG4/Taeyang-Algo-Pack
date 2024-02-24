# 관련 정보
# https://terms.naver.com/entry.naver?docId=3579618&cid=59086&categoryId=59093
# https://www.geeksforgeeks.org/topological-sorting/
# https://blog.naver.com/book541/222827144003
# https://www.youtube.com/watch?v=qzfeVeajuyc (동빈나)

# 관련 문제
# https://www.acmicpc.net/submit/2252/62385174 (백준 2252 줄 세우기)
# ind = indegree = 진입 차수

"""
    사이클이 발생하면 큐에 아무원소도 들어갈 수 없다.
    sum(ind) 했을때 0이 아니면 사이클이 발생한 것이다. if sum(ind) != 0: print("IMPOSSIBLE")
    한 번에 2개 이상의 원소가 들어간다는 것은 진입차수가 0인 원소가 두개 이상이 되므로 순위를 정할 수 없는 경우가 된다.
    
    1. indegree[i] 중 0이 아닌 게 있으면 사이클 존재 
    2. 큐가 2개 이상이 들어오는 게 있으면 방향의 일관성 상실
"""


###################################################################################################
###################################################################################################
# GPT-4
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list) # graph: 각 노드에서 시작하는 엣지의 리스트를 저장하기 위한 딕셔너리
        self.V = vertices # V: 그래프의 노드(정점)의 수

    def addEdge(self, u, v):
        self.graph[u].append(v) # 간선을 추가하는 함수. u에서 v로의 방향성을 가진 엣지를 추가

    def topologicalSortUtil(self, v, visited, stack):
        """
            v: 현재 방문 중인 노드
            visited: 각 노드의 방문 여부를 저장하는 리스트
            stack: 토폴로지컬 순서대로 노드를 저장할 스택
        """
        
        visited[v] = True # 현재 노드를 방문했음을 표시

        # 현재 노드에서 출발하는 모든 엣지에 대해서
        for i in self.graph[v]:
            # 아직 방문하지 않은 노드라면
            if visited[i] == False: 
                # 해당 노드에 대해 재귀적으로 함수 호출
                self.topologicalSortUtil(i, visited, stack) 
                
        # 현재 노드와 연결된 모든 노드를 방문한 후, 스택에 현재 노드 추가
        stack.insert(0, v) 

    def topologicalSort(self):
        """
            visited: 모든 노드에 대한 방문 정보를 저장하는 리스트
            초기에는 모든 노드를 방문하지 않았다고 가정
        """
        
        visited = [False] * (self.V) # 1부터 시작시 모든 self.V부분을 self.V + 1로 바꾼뒤 return 전에 마지막을 제거한다.
        stack = [] # stack: 토폴로지컬 순서대로 노드를 저장할 스택

        # 모든 노드에 대해서
        for i in range(self.V):
            # 해당 노드를 아직 방문하지 않았다면
            if visited[i] == False:
                # 토폴로지컬 정렬을 위한 유틸리티 함수 호출
                self.topologicalSortUtil(i, visited, stack)

        # 토폴로지컬 순서대로 정렬된 노드 리스트 반환
        return stack

###################################################################################################
###################################################################################################
# simple topological sort algorithm
from collections import *

def topological_sort():
    
    res = []
    q = deque()
    for i in range(1, n + 1):
        if ind[i] == 0:
            q.append(i) # 진입 차수가 0인 노드를 큐에 삽입
    
    while q:
        tmp = q.popleft()
        res.append(tmp)
        for node in graph[tmp]:
            ind[node] -= 1
            if ind[node] == 0:
                q.append(node)
    
    return res

###################################################################################################
###################################################################################################
# 관련 문제 : https://www.acmicpc.net/problem/1766
# topological heapsort algorithm
from collections import *
from heapq import *

def topological_heapsort():
    """
        해당 알고림즘은 우선순위 큐를 이용하여 사전순으로 가장 앞선 위상정렬을 찾을수 있다.
    """
    
    res, pq = [], []
    for i in range(1, n + 1):
        if ind[i] == 0:
            heappush(pq, i) # 진입 차수가 0인 노드를 큐에 삽입
    
    while pq:
        tmp = heappop(pq)
        res.append(tmp)
        for node in graph[tmp]:
            ind[node] -= 1
            if ind[node] == 0:
                heappush(pq, node)
    
    return res


if __name__ == "__main__":
    
    ##########################################################################
    # GPT-4
    # 예제 사용
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    print("Topological Sort:")
    print(g.topologicalSort())
    
    ##########################################################################
    # simple topological sort algorithm
    # topological heapsort algorithm
    
    # input
    n, m = map(int, input().split())
    graph = defaultdict(list)
    ind = [0] * (n + 1) # 진입 차수 = indegree
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        ind[b] += 1

    # output
    print(*topological_sort())
    # print(*topological_heapsort())
