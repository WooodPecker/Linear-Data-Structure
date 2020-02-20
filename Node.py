class Node:
    def __init__(self,initialdata):
        self.data = initialdata
        self.next = None

    def getdata(self):
        return self.data

    def getnext(self):
        return self.next

    def setdata(self,newdata):
        self.data = newdata

    def setnext(self,newnext):
        self.next = newnext

class unorderlist:
    def __init__(self):
        self.head = None

    def add(self,item): # 先把链表上的数值连到新增的数据上，再把当前数据作为表头
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp

    def size(self): # head 的指向 当无数据时，指向的是None，当有数据时，指向的是一个Node()对象含有data和next两个属性
        current =  self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getnext()
        return count

    def search(self,item):
        current = self.head
        isfound = False
        while current is not None and isfound == False:
            if current.getdata == item:
                isfound = True
            else:
                current =  current.getnext()
        return isfound

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous = current
                current = current.getnext()
        if previous is None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())

class Orederedlist:
    def __init__(self):
        self.head = None

    def search(self,item):
        current = self.head
        isfound = False
        stop = False
        while current is not None and isfound == False and not stop: # 相比于无序链表，增加了stop判断
            if current.getdata == item:
                isfound = True
            else:
                if current.getdata() > item: # 当链表的值出现大于目标函数时，则可以忽略后面的搜索
                    stop = True
                else:
                    current =  current.getnext()
        return isfound

    def add(self,item): # 先把链表上的数值连到新增的数据上，再把当前数据作为表头
        current = self.head
        previous = None
        stop = False

        while current is not None and not stop:
            if current.getdata() > item:
                stop = True
            else:
                previous = current
                current = current.getnext()

        temp = Node(item)
        if previous is None:
            temp.setnext(current) # 顺序不能反，先把后面的链上
            self.head = temp
        else:
            temp.setnext(current)
            previous.setnext(temp)


temp = Node(90)
a = temp.getdata()
print(a)

mylist = unorderlist()
mylist.add(5)
mylist.add(6)
mylist.remove(5)
print(mylist.head.data)
print(mylist.size())
print(mylist.search(3))