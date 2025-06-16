str=input()
x=""
for i in str:
  if i in "AEIOUaeiou":
       x+="0"
  else:
    x+=i
print(x)

x=input()
z="AEIOUaeiou"
a=x
for i in z:
        a=a.replace(i,"0")
print(x)
print(a)
