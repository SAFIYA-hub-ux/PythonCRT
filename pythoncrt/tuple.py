x=16,67
print(type(x))

y=12,12,23,45,6
print(type(y))
print(y)


n1,n2,n3,n4,=1121,3,6,67,
print(n1,n2,n3)
print(n1,type(n1))

list1,list2,list3=[12],[23],[57]
print(list1,list2,list3)

a=[10,20,30]
b=[1,46,79980]
y=a+b
print(y)
x=y*6
print(x)

c =(10,23,45)
d=(1,2,3)
result=c+d
print(result)
print(result*4)

s={2,}
print(type(s))

t=((1,35),(1,3,8),(34,87),(123,675),(87,2))
print(t)
for i in t:
  print(i,type(t))

t=8,45,67,23,2343,546
print(max(t))
print(min(t))
print(sorted(t))
print(len(t))

# create a tuple of programming lang being len as 15 and find the max element min element and print the sorted tuple and print the reversed tuple
t=('dfs','sdfsf','sfg','df')
print(max(t))
print(min(t))
print(sorted(t[::-1]))
print(len(t))
x=t[::-1]
print(x)

#create a tuple of names and print the original tuple and print the names which has a len of 5 from the tuple
y=("safi","geee","dfsv","gdfgh","hfghj")
print(y)
for i in y:
  if(len(i)==5):
    print(i)