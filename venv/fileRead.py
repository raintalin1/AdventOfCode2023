class readFile():
    
    def __init__(self, filename, RWpriv = 'r'):
        super().__init__()
        self.filename = f"C:\\Users\\white\\PycharmProjects\\pythonProject\\venv\\dataFiles\\{filename}"
        self.RWpriv = RWpriv

        global datalist
        datalist = []
        with open(self.filename, self.RWpriv) as input:
            lines = input.readlines()
            for l in lines:
                datalist.append(l.replace("\n", ""))

        global lists
        lists = []
        lists.append(datalist[:datalist.index('-----')])
        lists.append(datalist[datalist.index('-----'):])
        lists[1].pop(0)
        lists.append(lists[1][lists[1].index('-----'):])
        lists[1] = lists[1][:lists[1].index('-----')]
        lists[2].pop(0)




    def returnList(self,listToBeUsed): #0 = whole list, 1 = testingAlist, 2 = testingBlist, 3 = questionList
        if listToBeUsed == 0:
            return datalist
        elif listToBeUsed == 1:
            return lists[0]
        elif listToBeUsed == 2:
            return lists[1]
        elif listToBeUsed == 3:
            return lists[2]