class MyQueue:

    def __init__(self):
        self.y = []
        self.next = None

    def push(self, x: int) -> None:
        self.y.append(x)

    def pop(self) -> int:
        ret= self.y[0]
        self.y.remove(ret)
        return ret

    def peek(self) -> int:
        return self.y[0]

    def empty(self) -> bool:
        if not self.y:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()