from collections import deque

graph = {
  1: [2,3,7],
  2: [1,4,5],
  3: [1,6,7],
  4: [2,8],
  5: [2,9],
  6: [3,10],
  7: [3,1],
  8: [4],
  9: [5],
  10: [6]
}

#DFS
visited = {i: False for i in range(1,11)}
sequence = []
# x노드 탐색
def f(x):
  sequence.append(x)
  visited[x] = True
  for node in graph[x]:
    if not visited[node]:
      f(node)

f(1)
print(sequence)


visited = {i: False for i in range(1,11)}
sequence = []

stack = [1]
while stack:
  node = stack.pop()
  sequence.append(node)
  visited[node] = True
  for vertex in graph[node]:
    if not visited[vertex]:
      stack.append(vertex)

print(sequence)



#BFS
sequence = []
visited = {i: False for i in range(1,11)}

queue = deque([1])
visited[1] = True
while queue:
  node = queue.popleft()
  sequence.append(node)
  for vertex in graph[node]:
    if not visited[vertex]:
      queue.append(vertex)
      visited[vertex] = True

print(sequence)