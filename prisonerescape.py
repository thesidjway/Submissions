import math

input1=raw_input()
[l,w,num]=input1.split(' ')
it=0
coord=[]
yco=[]
mini=50001
maxi=-1

def BFS(v):
  BFSDone[v]=1
  if v==int(num)-1:
    print 0
    exit()
  for neighbour in adjList[v]:
    if visited[neighbour]==0:
      visited[neighbour]==1
  for neighbour in adjList[v]:
    if BFSDone[neighbour]==0:
      BFS(neighbour)

def distance(x1,y1,x2,y2):
  return math.sqrt((x1-x2)**2+(y1-y2)**2)

while (it<int(num)):
  input2=raw_input()
  [x,y]=input2.split(' ')
  coord.append([int(x),int(y)])
  if int(y)>maxi:
    maxipl=it
    maxi=int(y)
  if int(y)<mini:
    minipl=it
    mini=int(y)
  it+=1

if coord[minipl][1]>100:
  print '1'
  exit()
if int(w)-coord[maxipl][1]>100:
  print '1'
  exit()

adjList=[]
it=0
while it<int(num):
  adjList.append([])
  it+=1
print coord
i=0
j=0
while i < len(coord):
  j=i+1
  while j < len(coord):
    if distance(coord[i][0],coord[i][1],coord[j][0],coord[j][1])<100:
      adjList[i].append(j)
      adjList[j].append(i)
    j+=1
  i+=1

print adjList
visited=[]
BFSDone=[]

i=0
while i<int(num):
  visited.append(0)
  BFSDone.append(0)
  i+=1
BFS(0)
print 1




