n = int(input())
m = int(input())

graph = {i: [] for i in range(1,n+1)}
visited = {i: False for i in range(1,n+1)}
cnt = 0 # 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터 수

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def f(x):
  global cnt
  visited[x] = True
  for node in graph[x]:
    if not visited[node]:
      cnt += 1
      f(node)
      

f(1)
print(cnt)