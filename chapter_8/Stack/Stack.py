class Stack():
    def __init__(self, startingStackAsList=None):
        if startingStackAsList is None:
            self.dataList = [ ]
        else:
            self.dataList = startingStackAsList[:]

    def push(self, item):
        self.dataList.append(item)

    def pop(self):
        if len(self.dataList) == 0:
            raise indexError
        element = self.dataList.pop()
        return element

    def peek(self):
        item = self.dataList[-1]
        return item

    def getSize(self):
        nElements = len(self.dataList)
        return nElements

    def show(self):
        print('Stack is: ')
        for value in reversed(self.dataList):
            print('    ', value)

