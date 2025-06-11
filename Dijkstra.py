from collections import deque
import heapq

V,E = map(int,input().split())
graph = {i:[] for i in range(1, V+1)}
cost = [10**9]*(V+1)
start = int(input())
cost[start] = 0
for i in range(1, E+1):
  u,v,w = map(int,input().split())
  graph[u].append((v, w))
    
queue = [(0, start)]

while queue:
  weight, node = heapq.heappop(queue)  
  if cost[node] < weight:
    continue
  for vertex, eweight in graph[node]:
    if cost[vertex] > cost[node] + eweight:
      cost[vertex] = cost[node] + eweight
      heapq.heappush(queue, (cost[vertex], vertex))
        
for i in range(1, V+1):
  if cost[i] == 10**9:
    print("INF")
    continue
  print(cost[i])