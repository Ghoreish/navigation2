from navigation2 import navigation as navi
class map:
    def __init__(self):
        f=open("map.txt","r")
        dic, zum =navi.navigation.nodedict(f)
        ndic=navi.navigation.nodeway(dic)
        self.graphic=(dic,zum)
        for i in dic:
            if dic[i]=="1":
                self.one=i
            if dic[i]=="2":
                self.two=i
            if dic[i]=="3":
                self.three=i
            if dic[i]=="4":
                self.four=i
            if dic[i]=="5":
                self.five=i
            if dic[i]=="6":
                self.six=i
            if dic[i]=="7":
                self.seven=i
            if dic[i]=="H":
                self.home=i
        self.waylist=navi.navigation.wazer(self.home,ndic)