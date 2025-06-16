#write the python program to declare a list of words and declare a tuple of words and map it to print the combined words
n=int(input("enter the number of words:"))
list=["sagu","hello","dfds","dfdf"]
tuple=("fgdfg","dfbd","sdfgdf","gda")
i=1
while(i<=n):
    word=input("enter the word:")
    index=list.index(word)
    print(f"{word}-{tuple[index]}")
    i+=1
# declare the list of glocery items read input from the user from 1 to 5
# 1. to display the list of items in sorted way
# 2.take input from user add items to the cart
# 3.  give the cart items
# 4. TO update the quantity or the item present in the cart
# 5.generate the bill including item names item quantity ,price,and
#  if the final bill amont is >1000 the user will get 10% discount
#  if the user purchases any item more than 10 kg reduce the amount of 1 kg from that perticular items price
#  if the user purchases any perticular products add buy 1 and get one offer
# 6.add 25%to the overall bill and print the bill
list=["oil","rice","dhal"]
items=[]
while(True):
  choice=int(input("enter the choice:"))
  if(choice>=1 and choice<=6):
       if(choice==1):
           list.sort()
           print(list)
       elif(choice==2):
               for i in list:
                  temp=input("enter the items:")
                  items.append(temp)
               print(items)
               list.extend(items)
               print(list)
       elif(choice==3):
          print(list)
       elif(choice==4):
          list.pop(1)
          print(list)
       elif(choice==5):
          print("enjoy your meal .......bye")
          break
  else:
    print("invalid input")
    break
















