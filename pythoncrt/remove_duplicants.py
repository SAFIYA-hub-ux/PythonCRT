list=[1,2,22,2,3,33,12,3,12]
print("original list:")
print(list)
newlist=[]
for i in list:
  if i not in newlist:
    newlist.append(i)
print(newlist)