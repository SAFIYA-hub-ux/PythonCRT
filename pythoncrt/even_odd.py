size=int(input("size:"))
list=[]
newlist1=[]
newlist2=[]
for i in range(size):
  Temp=int(input())
  list.append(Temp)
print(list)
print()
for i in list:
  if(i%2==0):
    newlist1.append(i)
  else:
    newlist2.append(i)
print(newlist1)
print(newlist2)