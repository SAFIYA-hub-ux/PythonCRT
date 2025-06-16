#write a python program to read  a string as input from the user (including spaces and print the string by trimming the spaces)
s=input("enter the string:")
print(s)
print(s.strip())


s=input("enter the string:")
print(s)
a=s.split()
print(a)

s=input("enter the string:")
print(s)
a=s.join(input().split())
print(a)

list=["df","d","e"]
print(list)
s=str(list)
print(s)

i=input()
print(i)
str_list=i.split()
s="".join(str_list)
print(f"string without spaces:{s}")


s1="safi"
s2="df"

print(s1)
print(s2)
s3=s1.join(s2)
print(s3)

#write a program to read a sentence as in put from user and print the list of words from the sentence
x='hello safihow are you'
x1=x.split()
print(x1)

x="hello safihow are you"
x2="are"
x1=x.split()
print(x1)
if x2 in x1:
    print("present")

x="hello safihow are you"
x1=x.split()
print(x1)
if i in x1:
    print(x1[1])


z=input("enter the sentence:")
f=z.split()
print(f)
longestword=""
maxlength=0
for i in f:
  if len(i)>maxlength:
     maxlength=len(i)
     longestword=i
print(longestword)

x="hello safihow are you"
x1=x.split()
print(x1)
for i in range(len(x)):
  print(x[i],end=" ")
print()


x="hello safihow are you"
x1=x.split()
print(x1)
list=[]
for i in range(len(x1)):
  list.append(x1[i])
print(list)


#write the python program read string as input from user
# reverse the string
# convert string into lowercase
# convert char of string to lowercase if it is in uppercase and reverse
# check if string starting with letter A
# print the count of character a from the given string and replace all p letters to letter j

string=input()
print(string[::-1])
print(string.lower())
print(string.upper())
print(string.swapcase())
print(string.startswith("P"))
print(string.count("a"))
string=string.lower()
print(string.replace("p","j"))

#write a python program red the list of characters as input from user and covert it into a wrods  and print it

x=input()
x1=x.split()
z="".join(x1)
print(z)


size=int(input())
list=[]
for i in range(size):
  temp=input("enter the characters:")
  list.append(temp)
print(list)
str="".join(list)
print(str)

#read mail id as input from the user and print user name and organization name based on mailid
# name@organization.gmail.com
x=input()
x1=x.split("@")
print(x1)
print(x1[0])
x2=x1[1]
x3=x2.split(".")
print(x3)
print(x3[0])
print(x1[0]+x3[0])


x="fjdf gvrgO vbfg"
print(x.capitalize())
print(x.casefold())
print(x.title())
print(x.find("o"))
print("het".center(9,"#"))

x="hello safihow are you"
x1=x.split()
print(x1)
for i in x1:
  print(i[::-1],end=" ")


  