def numreturnchar (x):
  if  x=='a' or x=='b' or x=='c':
    return 2
  elif  x=='d' or x=='e' or x=='f':
    return 3
  elif  x=='g' or x=='h' or x=='i':
    return 4
  elif  x=='j' or x=='k' or x=='l':
    return 5
  elif  x=='m' or x=='n' or x=='o':
    return 6
  elif  x=='p' or x=='q' or x=='r' or x=='s':
    return 7
  elif  x=='t' or x=='u' or x=='v':
    return 8
  elif  x=='w' or x=='x' or x=='y' or x=='z':
    return 9

def quickSort(tosort):
    small = []
    pivotList = []
    large = []
    if len(tosort) <= 1:
        return tosort
    else:
        pivot = tosort[0]
        for i in tosort:
            if i < pivot:
                small.append(i)
            elif i > pivot:
                large.append(i)
            else:
                pivotList.append(i)
        small = quickSort(small)
        large = quickSort(large)
        return small + pivotList + large

def calculateMode(array):
  counter = 1;
  max = 0;
  ite=0
  mode = array[0];
  while ite<len(array)-1:
    if array[ite]==array[ite+1]:
      counter+=1
      if counter>max:
        max=counter
        mode=array[ite]
    else:
      counter=1
    ite+=1     
  return mode
	
n=raw_input()
numlist=[]
i=0
while i<int(n):
  l=raw_input()
  j=0
  a=[]
  while j<len(l):
    a.append(numreturnchar(l[j]))
    j=j+1  
  k=0
  m=0
  while k<len(a):
    m+=a[len(a)-1-k]*10**k
    k+=1
  numlist.append(m)
  i=i+1
numlist=quickSort(numlist)
mode=calculateMode(numlist)
print mode



