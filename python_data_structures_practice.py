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

# stack = ArrayStack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# print("peek", stack.peek())
# print(stack.pop())
# print(stack.getStack())
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())
# print(stack.peek())

class ArrayQueue:
    queue = []
    back = 0
    front = 0

    def enqueue(self, item):
        self.queue.append(item)
        self.back += 1

    def dequeue(self):
        if(self.back - self.front == 0):
            return None
        
        tem = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        return tem
    
    def getQueue(self):
        return self.queue[self.front:self.back]
    
# queue = ArrayQueue()
# queue.enqueue(1)
# queue.enqueue(2)
# print(queue.getQueue())
# print(queue.dequeue())
# print(queue.getQueue())
# print(queue.dequeue())