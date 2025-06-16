guestlist=[]
while(True):
  print("*****Menu*****")
  print("1.Add Guest")
  print("2.Remove the guest who cancles")
  print("3.check the guest attending party ")
  print("4.View the guest list")
  print("5.Exit")
  print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
  choice=int(input("enter the choice:"))
  if(choice>=1 and choice<=5):
    if(choice==1):
      guestname=input("enter the guestname:")
      guestlist.append(guestname)
      print(f"{guestname} is added to the guest list.....")
    elif(choice==2):
      cancelledguest=input("enter the cancelled guest name:")
      if cancelledguest in guestlist:
        guestlist.remove(cancelledguest)
        print(f"{cancelledguest}is removed from the guestlist")
      else:
        print(f"{cancelledguest}is not in the guestlist")
    elif(choice==3):
      checkguest=input("enter the guest name to check:")
      if checkguest in guestlist:
        print(f"{checkguest}is attending the party")
      else:
        print(f"{checkguest}is not attending the party")
    elif(choice==4):
      if(len(guestlist)==0):
        print("guest list is empty")
      else:
        guestlist.sort()
        print("heyyy!!! u got your final output")
        print("guest list:",guestlist)

    else:
      print("enjoy your party''''''''''!")
      break
  else:
    print("invalid input")

