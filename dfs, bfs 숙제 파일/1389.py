from collections import deque

n, m = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(x): # 최소 거리 탐색이기 때문에 바로 구할 수 있는 bfs 사용
  queue = deque([x])
  visited = {i: False for i in range(1, n + 1)}
  d = {i: 0 for i in range(1, n + 1)} # 거리 저장
  visited[x] = True

  while queue:
      node = queue.popleft()
      for vertex in graph[node]:
          if not visited[vertex]:
              queue.append(vertex)
              visited[vertex] = True
              d[vertex] = d[node] + 1

  return sum(d.values()) #저장된 거리 값들을 모두 더하여 반환


min_sum = 5000 # 2부터 100 까지 모두 더한 거리의 수보다 큰 적당한 수
answer = 0

for i in range(1, n + 1):
  total = bfs(i)
  if total < min_sum:
      min_sum = total
      answer = i
  elif total == min_sum and i < answer:
      answer = i

print(answer)
