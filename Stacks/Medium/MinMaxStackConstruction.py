""" A class with methods to peek, pop and push elements from the stack and also to return min and max values within constant time
"""
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min = []
        self.min = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.min.pop()
        self.max.pop()
        return self.stack.pop()

    def push(self, number):
        if self.stack == []:
            self.min,self.max = [number],[number]
        else:
            self.min.append(min(self.min[-1],number))
            self.max.append(max(self.max[-1],number))
        self.stack.append(number)

    def getMin(self):
        return self.min[-1]

    def getMax(self):
        return self.max[-1]
