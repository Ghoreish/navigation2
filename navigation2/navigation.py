import os
import time

class navigation:
    @staticmethod
    def nodedict(f):
        nodesign = f.read(1)
        mydict = {}
        counter = 0
        x = 0
        y = 0
        while nodesign:
            if nodesign == "\n":
                zum = counter
                counter = 0
                x = 0
                y += 1
            else:
                mydict.update({(x, y): nodesign})
                x += 1
                counter += 1
            nodesign = f.read(1)
        return mydict, zum

    @staticmethod
    def nodeway(x):
        mydict = {}
        wall = ["#", "+", "|", "-"]
        for i in x:
            mydict.update({i: []})
            if x[i] not in wall:
                if (i[0] - 1, i[1]) in x and x[(i[0] - 1, i[1])] not in wall:
                    mydict[i].append((i[0] - 1, i[1]))
                if (i[0] + 1, i[1]) in x and x[(i[0] + 1, i[1])] not in wall:
                    mydict[i].append((i[0] + 1, i[1]))
                if (i[0], i[1] - 1) in x and x[(i[0], i[1] - 1)] not in wall:
                    mydict[i].append((i[0], i[1] - 1))
                if (i[0], i[1] + 1) in x and x[(i[0], i[1] + 1)] not in wall:
                    mydict[i].append((i[0], i[1] + 1))
            if mydict[i] == []:
                mydict.pop(i)
        return mydict

    @staticmethod
    def wazer(no, dic):
        used = []
        l1 = []
        l2 = []
        used.append(no)
        for i in dic[no]:
            l2.append([no, i])
        l1 = l2
        while True:
            for i in l1:
                for j in dic[i[-1]]:
                    if j not in used:
                        used.append(j)
                        l2.append(i + [j])
            if l1 == l2:
                return l2
            else:
                l1 = l2