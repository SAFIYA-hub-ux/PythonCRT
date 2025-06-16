list2=["safu","hello","hii"]
list3=["hey","hoo","hwa"]
list2.extend(list3)
print(list2)
list3.extend(list2)
print(list3)
lang=["sql","mysql","Mongodb"]
list2.extend(lang)
print(list2)

list4=["wdw","efer","html","html","sdc","sdc","sdc"]
maxstr=" "
c=0
for i in list4:
  x=list4.count(i)
  if x>c:
    c=x
    maxstr=i
print(maxstr)

list4 = ["wdw", "efer", "html", "html", "sdc", "sdc"]

# Step 1: Find the maximum count (frequency)
c = 0
for i in list4:
    x = list4.count(i)
    if x > c:
        c = x

# Step 2: Find all strings with that max count, avoiding duplicates
result = []
for i in list4:
    if list4.count(i) == c and i not in result:
        result.append(i)

# Step 3: Print result
print(result)

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
print(cartoon)