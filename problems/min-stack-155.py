
# can be solved using one stack pushing the tuple conataining (val, min_val) into the stack.


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_val = float('inf')
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))
    
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    
    def getMin(self):
        return self.min_stack[-1]
    


m = MinStack()
m.push(-2)
m.push(-0)
m.push(-3)
print(m.getMin())
m.pop()
print(m.getMin())
m.push(-4)
print(m.getMin())
m.pop()
print(m.getMin())
m.pop()
m.pop()
m.push(100)
print(m.getMin())






# print(m.min_stack)
# print(m.getMin())

    
    