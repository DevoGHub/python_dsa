'''
Queue implementation using arrays
'''
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
    
queue = ArrayQueue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.getQueue())
print(queue.dequeue())
print(queue.getQueue())
print(queue.dequeue())