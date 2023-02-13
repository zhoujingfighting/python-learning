"""
学习python的class
"""
class test:
    # data owned by each class entity
    ttt = 1
    # share data by all class
    li=[] 
    def __init__(self) -> None:
        pass
    def __init__(self,variable):
        self.variale = variable

    def print(self):
        print(self.ttt)
        print(self.li)

    def add(self):
        self.ttt += 1
        self.li.append(1)

test1 = test("hhh")
test2 = test("jjj")

test1.add()
test1.print()

test2.add()
test2.print()