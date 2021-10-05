# BFS는 너비 우선 탐색이라고도 불리며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘.
# BFS는 큐 자료구조를 활용.
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리를 한다.
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
# 1 2 3 8 7 4 5 6

from collections import deque

def bfs(graph, start, visited):
    # Queue 구현 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    for i in graph[start]:
        v = queue.popleft()
        print(v, end = '')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9