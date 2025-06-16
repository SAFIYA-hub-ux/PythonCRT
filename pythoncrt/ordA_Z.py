x=input()
if(len(x)==1 and "A"<=x<="Z"):
        a=ord(x)
        print(a)
print("!!!!!!!!!!!!!!!!!!!!!!!!")

x=input()
if(len(x)==1 and "a"<=x<="z"):
        a=ord(x)
        print(a)
print("!!!!!!!!!!!!!!!!!!!!!!!!")

x=int(input())
if(65<=x<=90):
        a=(chr(x))
        print(a)
print("!!!!!!!!!!!!!!!!!!!!!!!!")

x=int(input())
if(97<=x<=122):
        a=(chr(x))
        print(a)


# write the python program to print uppercasealphabeats from a to z
for i in range(1,27):
    print(chr(i+64),".............",i+64)
print(".....")

for i in range(1,27):
    print((chr(i+96)),".............",i+96)
print(".....")



#print asci value of character
for i in range(65,91):
    print(ord(chr(i)),"..........",chr(i))
print(".....")
for i in range(97,123):
    print(ord(chr(i)),"..........",chr(i))



