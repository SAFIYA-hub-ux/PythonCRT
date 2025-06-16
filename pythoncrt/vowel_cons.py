# from functools import lru_cache
# read string as input from the user and print the count of uppercasevowels
# print(lowercase vowels),uppercase-consonents,lowercase-consonents
str=input()
ucc=0
ucv=0
lcv=0
lcc=0
for i in str:
  if(i.isalpha and i.isupper()):
    if i in "AEIOU":
      ucv+=1
    else:
      ucc+=1
  if(i.isalpha() and i.islower()):
    if(i in "aeiou"):
      lcv+=1
    else:
      lcc+=1
print(ucc)
print(ucv)
print(lcv)
print(lcc)


# from functools import lru_cache
# read string as input from the user and print the count of uppercasevowels
# print(lowercase vowels),uppercase-consonents,lowercase-consonents
str=input()
ucc=0
ucv=0
lcv=0
lcc=0
for i in str:
  if(i>="A" and i<="Z"):
    if(i in "AEIOU"):
      ucv+=1
    else:
      ucc+=1
  if(i>="a" and i<="z"):
    if(i in "aeiou"):
      lcv+=1
    else:
      lcc+=1

print(f"Uppercase Consonants: {ucc}")
print(f"Uppercase Vowels: {ucv}")
print(f"Lowercase Vowels: {lcv}")
print(f"Lowercase Consonants: {lcc}")

