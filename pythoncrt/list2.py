size=int(input("size:"))
# to read the list elements from the user and print a new list of the numbers which are multiples of 5list=[]
newlist=[]
for i in range(size):
  Temp=int(input())
  list.append(Temp)
print(list)
for i in list:
  if(i%5==0):
    newlist.append(i)
print(newlist)


# "write a python program to reqad the list elements as input from user and check weather the listr ekements are myltiples of 3 and 5 or not and print the  list of elements which are multiples of 3 and 5"
size=int(input("size:"))
list=[]
newlist=[]
for i in range(size):
  Temp=int(input())
  list.append(Temp)
print(list)
for i in list:
  if(i%5==0 and i%3==0):
    newlist.append(i)
print(newlist)



toylist=[]
newlist=[]
while(True):
  print("*****Menu*****")
  print("1.Add Toy names")
  print("2.Remove the duplicants")
  print("3.sort and display the final toy list")
  print("4.Exit")
  print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
  choice=int(input("enter the choice:"))
  if(choice>=1 and choice<=4):
    if(choice==1):
      toyname=input("enter the toyname:")
      toylist.append(toyname)
      print(f"{toyname} is added to the toy list.....")
    elif(choice==2):
      for i in toylist:
        if i not in newlist:
          newlist.append(i)
      print(newlist)
    elif(choice==3):
      newlist.sort()
      print("heyyy!!! u got your final output")
      print("toy list:",newlist)

    else:
      print("the final toy list is completed''''''''''!")
      break
  else:
    print("invalid input")
# write the python program to read marks of five students for 3 subj each and print the marks list for individual student along with the class where 1.if students marks are more than 90% ist class 2nd class >75% 3 rd class >50% fail if <50%
songlist=[]
newlist=[]
while(True):
  print("*****Menu*****")
  print("1.Add song names")
  print("2.sort and display the final toy list")
  print("3.Exit")
  print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
  choice=int(input("enter the choice:"))
  if(choice>=1 and choice<=10):
    if(choice==1):
      songname=input("enter the toyname:")
      newlist.append(songname)
      print(f"{songname} is added to the toy list.....")
    elif(choice==2):
      for i in songlist:
        songlist.sort
        print(i)
    else:
      break


