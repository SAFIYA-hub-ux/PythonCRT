num=int(input("Enter the integer value:"))
if(num>0):
    print(num,"is a +ve Number")
elif(num<0):
    print(num,"is a -ve Number")

num=int(input())
print("+ve"if num>=0 else"no")



dict = {

     "name":"Safiya",
     "rollno":34,
     " branch":"Bioinformatics",
     "friends":{
         "madhu":"nimmala",
         "safiya":"dudekula",
     },
     "list":["sdes",7,"sded"],
}
print(dict["friends"]["madhu"])
print(dict.keys())
print(dict["list"][2])
print(len(dict["list"]))
print(dict.items())


num=int(input()) 
x="+ve"if num>0 else"-ve"
print(f"{num} is {x}")


num=int(input())
x="digit" if(num>=-9 and num<=9) else "number"
print(f"{num} is {x}")


num=int(input())
x="2 digit number" if(num>=-99 and num<=-10 or num<=99 and num>=10) else " not a two digit number"
print(f"{num} is {x}")

num=int(input()) 
x="3 digit number" if(num>=-999 and num<=-100 or num<=999 and num>=100) else " not a three digit number"
print(f"{num} is {x}")

amount=int(input("enter the Amount:"))
print("2000 ------->",amount//2000)
amount=amount%2000
print("1000 ------->",amount//1000)
amount=amount%1000
print("500 ------->",amount//500)
amount=amount%500
print("200 ------->",amount//200)
amount=amount%200
print("100 ------->",amount//100)
amount=amount%100
print("50 ------->",amount//50)
amount=amount%50
print("10 ------->",amount//10)
amount=amount%10
print("5 ------->",amount//5)
amount=amount%5
print("2 ------->",amount//2)
amount=amount%2
print("1 ------->",amount//1)
amount=amount%1

for i in range(1,11):
    print("3*",i,"=",3*i) 
n=1
while(n<=10):
    print("3*",n,"=",3*n)
    n+=1

n=int(input())
for i in range(1,n+1):
     print(f"{n}*",i,"=",n*i)

n=1
i=int(input())
while(n<=i):
    print(f"{n}*",i,"=",n*i)
    n+=1


# to print reverse multiplication table of n 
n=int(input())
for i in range(10,0,-1):
    print("3*",i,"=",3*i) 
# to print reverse multiplication table of 1 to n 

n=int(input())
for i in range(1,n+1):
    for j in range(10,0,-1):
        print(f"{i}*",j,"=",i*j)






# to print reverse multiplication table of n to 1 
n=int(input())
for i in range(n,0,-1):
    for j in range(10,0,-1):
        print(f"{i}*",j,"=",i*j)

n=int(input())
for i in range(10,0,-1):
    print("3*",i,"=",3*i) 

n=int(input())
for i in range(1,n+1):
    print(i) 

n=int(input())
for i in range(n,0,-1):
    print(i) 

n=int(input())
for i in range(1,n+1):
    print(i*i)  
   
n=int(input())
for i in range(n,0,-1):
    print(i*i)    

n=int(input())
for i in range(1,n+1):
    print(i*i*i,end=" ") 
   
n=int(input())
for i in range(n,0,-1):
    print(i*i*i,end=" ")    

# find numner of digits present in number
n=int(input())
count=0
while(n!=0):
    n=n//10
    count+=1
print(count)

# find the sum of digits
n=int(input())
temp=n
sum=0
while(n!=0):
    rem=n%10
    sum=sum+rem
    n=n//10
print(sum)
# no of even digits and odd digits in the number

n=int(input())
sum=0
while(n!=0):
    if(n%2==0):
        rem=n%10
        sum=sum+rem
        n=n//10
print(sum)

# find sum of even and odd digits
n=int(input())
sum=0
even=0
odd=0
n=abs(n)
while(n!=0):
    rem=n%10
    sum=sum+rem
    if(rem%2==0):
        even+=rem
    else:
        odd+=rem    
    n=n//10   
print(even)
print(odd) 
print(sum)



# find the number of zeroes in the given number 

n=int(input())
count=0
n=abs(n)
if(n==0):
    count=1
else:
  while(n!=0):
    rem=n%10
    if(rem==0):
        count+=1
    n=n//10
print(count)
  



# find numner of digits present in number
n = int(input("Enter a number: "))
count = 0

# Handle zero as a special case
if n == 0:
    count = 1
else:
    n = abs(n)  # Remove negative sign if present
    while n != 0:
        n = n // 10
        count += 1

# find sum of even and odd digits sum
n=int(input())
evensum=0
oddsum=0
n=abs(n)
while(n!=0):
    rem=n%10
    if(rem%2==0):
        evensum+=rem
    else:
        oddsum+=rem
    n=n//10
print(evensum)
print(oddsum)


n=int(input())
sumeven=0
even=0
odd=0
sumodd=0
while(n!=0):
    rem=n%10
    if(rem%2==0):
        sumeven=sumeven+rem
        even+=1
    else:
        sumodd=sumodd+rem 
        odd+=1          
    n=n//10   
print(sumeven)
print(sumodd) 
print("even",even)
print("odd",odd)



list=[1,"safi","2",1]
print(list[0])
print(list[1])
print(list[2])
print(list[-1])

for i in list:
     print(i,end=" ")
print("\n")     

for i in range(len(list)):
    print(list[i],end=" ") 
print("\n")       
  
i=0
while(i<len(list)):
    print(list[i],end=" ")
    i+=1

size=int(input("enter the list elements"))
prog=[]
for i in range(size):
    Temp=int(input("enter lang")  )
    prog.append(Temp)
print("elements i list:") 
print(prog)     

size=int(input())
prog=[]
for i in range(size):
    temp=(input().split())
    prog.append(temp)
print(prog)  

color=["dd","ewed","sde"] 
print(color)
del color[2]
print(color)
del color 
print(color)
# buit in list function len(),sorted(),max(),list(),min(),any(),sum(),all()
# write a python program to read the size of list as input of the user and take the list elements also as input from the user and find the len of the list the max element or the number present in list ,min,sumation of elements of list and the sorted list in ascending order
size=int(input("enter the size of list:"))
num=[]
for i in range(size):
    Temp=int(input(f"enter the{i}:"))
    num.append(Temp)
print(num) 
print("max element is",max(num))   
print("min element is",min(num))   
print("sum element is",sum(num))   
print("len  element is",len(num))   
print("sorted element is",sorted(num))   
print("all element is",all(num))   
print("any element is",any(num))   


cartoon=["dsd","sd","dsa","wsdwsd","sd","sd"]
print(cartoon)
cartoon.append("dfef")
print(cartoon)
cartoon.pop(1)
print(cartoon)
cartoon.insert(3,"sfdf")
print(cartoon)
cartoon.remove("dsa")
print(cartoon)
print(cartoon.count("sd"))
x=cartoon.index("sd")
print(x)
u=[2,"DF"]
print(cartoon.extend(u))
print(cartoon)
l=[1,2,4,65,7,68,79,8]
print(l[2:])
print(l[::-1])
print(l[:3:-1])
print(l[-2:4:-1])
# Write a python program to reverse a list of numbers without using reverse method
list=[1,2,3,"safi","hello",]
x=list[::-1]
print(x)    

      

# write a python progrm to sort the list of numbers without using sort method
# Sample list
numbers = [5, 2, 9, 1, 7, 3,]

# Empty list to store sorted elements
sorted_list = []

# Repeat until the original list is empty
while numbers:
    # Find the minimum element in the list
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    
    # Add the minimum to sorted list and remove from original
    sorted_list.append(min_val)
    numbers.remove(min_val)

print("Sorted list:", sorted_list)


list2=["safu","hello","hii"]
list3=["hey","hoo","hwa"]
list2.extend(list3)
print(list2)
