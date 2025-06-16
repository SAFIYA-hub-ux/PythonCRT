# #take name as input from username including prifix as mr or miss
# print the gender classification of name on bases of prifix

x=["mr.dheeraj","ms.sowmya","mr.ram"]
print(x[0::])
for i in x:
  if(i.startswith("mr")):
     print("male",i)
  elif(i.startswith("ms"))  :
     print("female",i)


