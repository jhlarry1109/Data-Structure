li = []
n, e = map(int,input().split())

li = [[0] * (n+1) for _ in range(n+1)]
l = [[] for _ in range(n+1)]

for i in range(e):
    a,b = map(int,input().split())
    li[a][b] = 1
    li[b][a] = 1
    l[a].append(b)
    l[b].append(a)
    
for i in range(1, n+1):
    print(*li[i][1:])
print(l[1:])