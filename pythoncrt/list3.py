list9=["dhal","soap","chocolate","oil"]
list8=["oil","shampoo","potato"]
newlist=[]
list9.extend(list8)
print(list9)
for i in list9:
  if i not in newlist:
    newlist.append(i)
print(newlist)
x=sorted(newlist)
print(x)

size=int(input())
words=[]
newshuffled=[]
for i in range(size):
  temp=input("enter words:")
  words.append(temp)
print(words)
if(len(words)>=2):
  words[2],words[0]=words[0],words[2]
  print(words)


size=int(input())
list=[]
marks=[]
x=["soc","math","phy"]
for i in range(size):
  temp=(input(f"enter student names{i}:"))
  list.append(temp)
print(list)
for j in (list):
  for k in x:
     temp=int(input(f"enter student marks of {j} in {k} is :"))
     marks.append(temp)
print(marks)