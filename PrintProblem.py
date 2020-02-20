from Queen import Queen

import random

class Printer:
    def __init__(self,paperperminute):
        self.paperate = paperperminute
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 1:
                self.currentTask = None

    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self,newstask):
        self.currentTask = newstask
        self.timeRemaining = newstask.getPages() / self.paperate * 60  # 打印需要时间


class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self,currenttime):
        return currenttime - self.timestamp

def newPrintTask():
    num = random.randrange(1,181)
    return True if num == 180 else False

def simulation(simtime,paperperminute):
    newPrinter =  Printer(paperperminute)
    printQueen = Queen()
    waitingtime = []
    for time in range(simtime):

        if newPrintTask():
            task = Task(time)
            printQueen.enqueen(task)

        if ( not newPrinter.busy() ) and ( not printQueen.isEmpty() ): # 打印机不忙 且 队列不空时
            nexttask = printQueen.dequeen()   # 从队列第一个出来作为任务
            waitingtime.append(nexttask.waitTime(time))  # 获取该任务的等待时间
            newPrinter.startNext(nexttask) # 开始打印

        newPrinter.tick()

    averagewit = sum(waitingtime) / len(waitingtime)
    print("Average wait %6.2f secs %3d task remaining." %(averagewit,printQueen.size()))

for i in range(10):
    simulation(3600,5)



