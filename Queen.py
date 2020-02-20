class Queen:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return  self.items == []

    def enqueen(self,item):
        self.items.insert(0,item)

    def dequeen(self):
        return  self.items.pop()

    def size(self):
        return len(self.items)
