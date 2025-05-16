from collections import deque

n, m, v = map(int,input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1): # 정점의 번호가 가장 작은 것을 먼저 방문
    graph[i].sort()
    
visited = {i: False for i in range(1,n+1)}
sequence = []

def f(x): # dfs
  sequence.append(x)
  visited[x] = True
  for node in graph[x]:
    if not visited[node]:
      f(node)
        
f(v)
print(*sequence)

visited = {i: False for i in range(1,n+1)}
sequence = []

queue = deque([v])
visited[v] = True
while queue: # bfs
  node = queue.popleft()
  sequence.append(node)
  for vertex in graph[node]:
    if not visited[vertex]:
      queue.append(vertex)
      visited[vertex] = True
        
print(*sequence)