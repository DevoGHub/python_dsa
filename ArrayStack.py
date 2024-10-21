class ArrayStack:
    stack = []
    top = 0

    def push(self, item):
        self.stack.append(item)
        self.top += 1

    def pop(self):
        if (self.top == 0):
            return None
        
        tem = self.stack[self.top - 1]
        self.stack[self.top - 1] = None
        self.top -= 1
        return tem
    
    def peek(self):
        if (self.top == 0):
            return None
        
        return self.stack[self.top - 1]
    
    def getStack(self):
        return self.stack[0:self.top]

stack = ArrayStack()
stack.push(1)
stack.push(2)
stack.push(3)
print("peek", stack.peek())
print(stack.pop())
print(stack.getStack())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.peek())