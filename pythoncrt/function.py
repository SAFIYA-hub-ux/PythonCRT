def fun():
  print("safiya")
  print("dh")
  print("dhgfh")
  print("dhjh")
  print("dfghh")
  print("dhtgh")
  print("dhxfthb")
fun()
fun()


# user defined,buitin,lambda,recurrsion

def funv(i,o):
  return i*o
print(funv(9,7))
print(funv(8,46))

def function():
  return "JYFRDC"
d=function()
print(d)


def name(nam):
  return f"dfdsf df sd f {nam}"
res=name("Kavya")
print(res)

def funx(l,m):
  print("hrloo"," ",l,m)
funx("safi","sdd")

# to check weather the user given integer is even or odd using functions
def even_odd(c):
  if(c%2==0):
    print("even")
  else:
    print("odd")
even_odd(8)
even_odd(7)
even_odd(4)
even_odd(45)
even_odd(567)

def e_o(c):
  if(c%2==0):
    even="even"
    return even
  else:
    odd="odd"
    return odd
print(e_o(8))
print(e_o(7))
print(e_o(4))
print(e_o(45))
print(e_o(567))

# check weather user given number is prime or not using functions(using return)
def prime(c):
  if(c<=1):
    return "not prime"
  for i in range(2,c):
    if(c%i==0):
      return "notprime"
  return "prime"
result=prime(8)
print(result)
result=prime(1)
print(result)
result=prime(2)
print(result)
result=prime(3)
print(result)
result=prime(78)
print(result)

# multiplication table of n
def mul(n):
  x=""
  for i in range(1,11):
    x+= f"{n}*{i}={n*i}\n"
  return x
print(mul(8))
def mul1(y):
  for i in range(1,y+1):
    for j in range(1,11):
      print(f"{i}*{j}={i*j}")
mul1(5)

db = {
  "ATGT" : "geneA",  # 3/4 = 75%
  "ATGC" :  "geneB",
  "TTAC" : "geneC",  # 1/4 = 25%
  "geneD": "ATGG",  # 3/4 = 75%
  "geneE": "ATCC",  # 3/4 = 75%
  "geneF": "AGGC",  # 2/4 = 50%
  "geneG": "GTGC",  # 3/4 = 75%
  "geneH": "TTGC",  # 3/4 = 75%
  "geneI": "GGGG",  # 0/4 = 0%
  "geneJ": "ATGA"   # 3/4 = 75%
}
def gene(dna,db):
  countg=0
  countc=0
  if dna in db:
    id=db[dna]
  for i in dna:
       countg=dna.count(i)
       countc=dna.count(i)
  gccount=(countg/countc)*100
  if(gccount>=80):
       status="goodmatch"
  elif(gccount>=50 and gccount<80):
       status="moderate"
  else:
      status="poor amtch"
  print(f"ID:{id}|Match:{gccount}% |Status:{status}")
seq="ATGC"
gene(seq,db)

def safi():
   print("hYg")
def food():
  print("HJGG")
safi()
food()


def safi():
  def food():
   print("hYg")
  def servefood():
      print("HJGG")
  food()
  servefood()
  print("enjoy")
  food()
safi()

def hello():
  print("hyufg")
hello()

def o():
  return "hukh"
o()

def hel():
  return 9
print(hel())

def hl():
  return("hyufg")
print(hl())

def h():
 print("hyufg")
print(h())

# 1.FORMAL -PARAMETERS
# 2.ACTUALARGUMENTS-(CALLING FUNCTIONS)
#  2.1.positional,keyword,default,variable length arguments,keyword variable len arguments
# 1.positional
def op(x, y):
  z=x**y
  print(z)
op(5, 2)

# 2.keyword
def popo(nam,age):
  print(nam,age)
popo(nam="fdf",age="gyg")

# 2.Default arguments
def popo(nam="GH",age=9):
  print(nam,age)
popo(nam="fdf",age="68")

def i(*n):
  n=a+b
  print(n)
i()



def i(*n):
  n=n[0]+n[1]+n[2]+n[3]+n[4]+n[5]
  print(n)
i(12,3.9,7,6,6,6,7,5,5,4)

def add(**num):
  z=num["a"]+num["b"]+num["c"]
  print(z)
add(a=9,b=9,c=7)

