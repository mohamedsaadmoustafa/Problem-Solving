class MyQueue:
    def __init__(self):
        self.s = []
    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        a = self.s[0]
        self.s = self.s[1:]
        return a

    def peek(self) -> int:
        return self.s[0]

    def empty(self) -> bool:
        return not self.s
