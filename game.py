import os,time
from navigation2 import kids
from navigation2 import map
m=map.map()
kidlist=[]
for i in m.waylist:
    if i[-1]==m.one:
        kid1=kids.Kids(i)
        kidlist.append(kid1)
    if i[-1]==m.two:
        kid2=kids.Kids(i)
        kidlist.append(kid2)
    if i[-1] == m.three:
        kid3 = kids.Kids(i)
        kidlist.append(kid3)
    if i[-1] == m.four:
        kid4 = kids.Kids(i)
        kidlist.append(kid4)
    if i[-1] == m.five:
        kid5 = kids.Kids(i)
        kidlist.append(kid5)
    if i[-1] == m.six:
        kid6 = kids.Kids(i)
        kidlist.append(kid6)
    if i[-1] == m.seven:
        kid7 = kids.Kids(i)
        kidlist.append(kid7)
graphic=m.graphic[0]
zum=m.graphic[1]
n=0
while True:
    l=1
    for i in kidlist:
        if i.move()=="Not Done!":
            l=0
    for i in graphic:
        a=graphic[i]
        for j in kidlist:
            if i==j.place:
                a="0"
        if n==zum-1:
            print(a)
            n=0
        else:
            print(a,end="")
            n+=1
    time.sleep(0.1)
    os.system("clear")
    if l==1:
        break


