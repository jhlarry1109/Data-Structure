from collections import deque

a,b = map(int,input().split())

def bfs(a, b): # 연산의 최솟값을 찾아야 하기 때문에 최단거리를 바로 구할 수 있는 bfs 사용
    queue = deque()
    queue.append([a, 1])

    visited = {a:True}

    while queue:
        x, cnt = queue.popleft()
        if x == b:
            return cnt
        if x * 2 <= b and not visited.get(x*2, False): # x*2키가 없다면 False
            visited[x*2] = True
            queue.append([x*2, cnt+1])
        if x * 10 + 1 <= b and not visited.get(x*10+1, False): # 마지막에 1을 더한 숫자 키가 없다면 False
            visited[x*10+1] = True
            queue.append([x*10+1, cnt+1])
    return -1 # 안되면 -1 반환
    
print(bfs(a, b))