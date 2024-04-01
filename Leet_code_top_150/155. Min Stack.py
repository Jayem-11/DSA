class MinStack(object):

    def __init__(self):
        self.stack = []
        self.M = []
        
    def push(self, val):
        self.stack.append(val)
        self.M.append(val if not self.M else min(val, self.M[-1]))
        
    def pop(self):
        self.stack.pop()
        self.M.pop()

    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.M[-1]

        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()