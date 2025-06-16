seq=input()
print(seq)
countc=seq.count("c")
countg=seq.count("g")
counta=seq.count("a")
countt=seq.count("t")
allcount=counta+countc+countg+countt
gc=(countg+countc)/allcount*100
print(gc)
print(countc)
print(countg)
if(gc>60):
    print("high")
elif(gc>=40 and gc<=60):
    print("moderate")
elif(gc<40):
    print("low")