import math

input1=raw_input()
[l,w,num]=input1.split(' ')
it=0
coord=[]
yco=[]
mini=50001
maxi=-1


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
  print 0
  exit()
if int(w)-coord[maxipl][1]>100:
  print 0
  exit()

adjList=[]
it=0
while it<int(num):
  adjList.append([])
  it+=1
#print coord
i=0
j=0
while i < len(coord):
  j=i+1
  while j < len(coord):
    if distance(coord[i][0],coord[i][1],coord[j][0],coord[j][1])<=200:
      adjList[i].append(j)
      adjList[j].append(i)
    j+=1
  i+=1
top=[]
bottom=[]
i=0
while i<len(coord):
	if coord[i][1]<=100:
		top.append(i)
		adjList[i].append(int(num))
	if coord[i][1]>=int(w)-100:
		bottom.append(i)
		adjList[i].append(int(num)+1)
	i+=1
adjList.append(top)
adjList.append(bottom)

visited=[int(num)]
tobe=adjList[int(num)]
i=int(num)
#print adjList

while len(tobe)>0:
	if (tobe[0] in visited)==0:
		visited.append(tobe[0])
		tobetemp=adjList[tobe[0]]
		for k in tobetemp:
			if (k in visited)==0 and (k in tobe)==0:
				tobe.append(k)
				#print "appended",k
				#print visited,'visited'
				#print tobe,'tobe'
		#print "popped",tobe[0]
		#print visited,'visited'
		#print tobe,'tobe'
		tobe.pop(0)
		
	#print visited,'visited'
	#print tobe,'tobe'
	if int(num)+1 in visited:
		print 1
		exit()

print 0
