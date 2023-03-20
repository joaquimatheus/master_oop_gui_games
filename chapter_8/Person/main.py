from Person import *

oPerson1 = Person('Joe Schmoe', 90000)
oPerson2 = Person('Jane Smith', 99000)

print(oPerson1.getSalary())
print(oPerson2.getSalary())

oPerson1.setSalary(100000)
oPerson2.setSalary(111111)

print(oPerson1.getSalary())
print(oPerson2.getSalary())
