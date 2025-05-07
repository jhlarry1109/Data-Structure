li = []
n, e = map(int,input().split())

li = [[0] * n for _ in range(n)]
l = [[] for _ in range(n)]

for i in range(e):
    a,b = map(int,input().split())
    li[a][b] = 1
    li[b][a] = 1
    l[a].append(b)
    l[b].append(a)
    
for i in range(n):
    print(*li[i])
print(l)