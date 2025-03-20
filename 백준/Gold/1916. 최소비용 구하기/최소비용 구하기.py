from queue import PriorityQueue
n=int(input())
m=int(input())
l=[[] for _ in range(n+1)]
for i in range(m):
    p,q,r = map(int,input().split())
    l[p].append((q,r))#시작,도착,가중치
s,e = map(int,input().split())
visited = [0]*(n+1)
value = [float('inf')]*(n+1)
value[s]=0
que = PriorityQueue()
que.put((value[s],s))#0,1
while not que.empty():
    x,y = que.get()#가중치,시작
    if visited[y]==1:continue
    visited[y]=1
    for q,r in l[y]:#도착,가중치
        if(r+x<value[q] and visited[q]==0):value[q]=x+r
        que.put((value[q],q))
print(value[e])