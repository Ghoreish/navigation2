class Kids:
    def __init__(self,waylist):
        l1=[]
        for i in waylist[:-1]:
            l1.append(i)
        l1.reverse()
        self.waylist=waylist+l1
        self.nplace=0
    @property
    def place(self):
        return self.waylist[self.nplace]
    def move(self):
        if self.nplace==(len(self.waylist)-1):
            return "Done!"
        else:
            self.nplace+=1
            return "Not Done!"