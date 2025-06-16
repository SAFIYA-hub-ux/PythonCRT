# print count of no of uppercaseletters ,lowercase,count of numeric values,print count of special characters

str=input()
uc=0
lc=0
numeric=0
spc=0
for i in str:
  if i.isupper():
    uc+=1
  elif i.islower():
    lc+=1
  elif i.isnumeric():
    numeric+=1
  else:
    spc+=1
print(f"uppercase:{uc}")
print(f"lowercase:{lc}")
print(f"numeric:{numeric}")
print(f"special characters:{spc}")


