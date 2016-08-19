source,dest=raw_input().split()
source,dest=int(source),int(dest)
n,m=raw_input().split()
n,m=int(n),int(m)


def nexthigher(flash_int,time_now):
	i=0
	while((time_now+i)%int(flash_int) != 0):
		i+=1
	return time_now+i



flash=[]
flash=raw_input().split()

reachTime=[100000 for i in range(n)]
pending=[i+1 for i in range(n)]

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

reachTime[source-1]=0

while dest in pending:
	#print pending
	k=0
	minval=100001
	minindex=0
	while k<len(reachTime):
		#print reachTime
		if minval>reachTime[k]:
			if k+1 in pending:
				minval=reachTime[k]
				minindex=k
		k+=1
	#print "minval",minval
	#print "minindex",minindex
	pending.remove(minindex+1)
	if minindex!=dest-1:
	#	print "reachTime[minindex] before nexthigher",reachTime[minindex]
	#	print "flash[minindex] before nexthigher",flash[minindex]
		reachTime[minindex]=nexthigher(flash[minindex],reachTime[minindex])
	#	print "reachTime[minindex] after nexthigher",reachTime[minindex]
	#print "adjList[minindex]",adjList[minindex]
	#print "adjMat[minindex]",adjMat[minindex]
	for j in adjList[minindex]:
		temp=reachTime[minindex]+adjMat[minindex][j]
		if temp<reachTime[j]:
			reachTime[j]=temp

print reachTime[dest-1]






