class MinStack(object):
    #Creating 2 stacks where one is the main stack and the other is a min stack
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val):

        self.stack.append(val)
        #need to check if there is already a min in the min stack
        #min will return the lowest number from all numers given
        val = min(val,self.minstack[-1] if self.minstack else val)

        #val is now the minimum value of the min stack

        self.minstack.append(val)


    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def top(self):
        #Get last inserted value
        return self.stack[-1]

    def getMin(self):

        #get from the minstack only when the stack is non empty
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()