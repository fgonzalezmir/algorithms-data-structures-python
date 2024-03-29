
class Stack:
    
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return self.stack == []
    
    # O(1)
    def push(self, data):
        self.stack.append(data)
     
    # O(1)    
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data
    
    # O(1)
    def peek(self):
        data = self.stack[-1]
        return data
    
    def sizeStack(self):
        return len(self.stack)
    

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.sizeStack())

print("Popped: ", stack.pop())
print("Popped: ", stack.pop())
print(stack.sizeStack())

print("Peek: ", stack.peek())
print(stack.sizeStack())


