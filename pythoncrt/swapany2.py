size=int(input("size:"))
list=[]
for i in range(size):
  Temp=int(input())
  list.append(Temp)
print(list)
if(len(list)>=2):
  list[4],list[1]=list[1],list[4]
  print(list)

#write the python program to read 2 integer as input from user and swap it
a=int(input())
b=int(input())
print(a,b)
a,b=b,a
print(a,b)  