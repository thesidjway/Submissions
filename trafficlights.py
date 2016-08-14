source,dest=raw_input().split()
source,dest=int(source),int(dest)
n,m=raw_input().split()
n,m=int(n),int(m)


def nexthigher(flash_int,time_now):
	while((time_now+i)%int(flash_int) != 0):
		i+=1
	return time_now+i



flash=[]
flash=raw_input().split()

reachTime=[100000 for i in range(n)]
visited=[0 for i in range(n)]
pending=[i for i in range(n)]

adjMat = [[100000 for i in range(n)] for j in range(n)]
adjList= [[] for i in range(n)] 
i=0
while i<m:
	a,b,c=raw_input().split()
	a,b,c=int(a),int(b),int(c)
	adjMat[a-1][b-1]=c
	adjMat[b-1][a-1]=c
	adjList[a-1].append(b-1)
	adjList[b-1].append(a-1)
	i+=1

cost=0
reachTime[source-1]=0

