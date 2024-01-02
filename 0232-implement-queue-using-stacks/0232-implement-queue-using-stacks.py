class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2= []
    

    def push(self, x: int) -> None:
        #if s1 is not empty, s1 -> s2
        # s1.append x
        #s2 -> s1
        
#         while len(self.s1) !=0:
#             self.s2.append(self.s1[-1])
#             self.s1.pop()
        
#         self.s1.append(x)
        
#         while len(self.s2) != 0:
#             self.s1.append(self.s2[-1])
#             self.s2.pop()
        self.s1.append(x)   
    
    def pop(self) -> int:
        # return self.s1.pop()
        if not self.s2:
            while len(self.s1)!=0:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        # x = self.s1[-1]
        # return x
        if not self.s2:
            while len(self.s1)!=0:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
    
    def empty(self) -> bool:
        return not self.s1 and not self.s2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

