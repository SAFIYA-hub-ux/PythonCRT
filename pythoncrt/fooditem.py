#1 .To displAY the menu of food items(list)
#2.create the tuple of prices with respect to food items list
#3.read the input from the user for odering the food including the quantity
 #if it exists in the menu----confirm order
 #if not print a message ----
#4.while billing,read phone.no,feedback,read tip amount
#5.add 18% gst to the bill and print the  bill if bill>0
list=["dosa","samosa","panipuri","lemonrice"]
n=int(input("enter the no of food items:"))
print(list)
n=0
tuple=(100,59,30,60)
for i in list:
    word=input("enter the word:")
    print(f"price of {i}-{tuple[n]}")
    n+=1
x=input("enter the item ordered by the user:")
if(x in list):
  print ("your order is confirm")
else:
  print("item is not present")
bill=int(input("enter your bill is"))
phoneno=int(input("enter phone no:"))
feedback=type(input("enter your feedback:"))
tip=int(input("enter the tip amount:"))
if(bill>0):
  gst=bill*18/100
  print(bill+gst)







