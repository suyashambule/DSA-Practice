class StackusingList:
    def __init__(self):
        self.stack=[]

    def push(self, data):
        self.stack.append(data)
        print(f"Element pushed to stack {data}")

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def top(self):
        return self.stack[-1] if not self.is_empty() else None
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty, cannot pop element")
            return None
myStack= StackusingList()
myStack.push(10)
myStack.push(20)
myStack.push(30)
print(f"Top element is: {myStack.top()}")
print(f"Stack size is: {myStack.size()}")
print(f"Is stack empty? {myStack.is_empty()}")
print(f"Popped element is: {myStack.pop()}")
print(f"Stack size after pop is: {myStack.size()}")

