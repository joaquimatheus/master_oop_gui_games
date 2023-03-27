class Sample():
    nObjects = 0

    def __init__(self, name):
        self.name = name
        Sample.nObjects = Sample.nObjects + 1

    def howManyObjects(self):
        print('There are', Sample.nObjects, 'Sample objects')

    def __del__(self):
        Sample.nObjects = Sample.nObjects - 1

oSample1 = Sample('A')
oSample2 = Sample('B')
oSample3 = Sample('C')
oSample4 = Sample('D')

del oSample3

oSample1.howManyObjects()
