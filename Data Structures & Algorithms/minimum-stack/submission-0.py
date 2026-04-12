class MinStack:

    def __init__(self):
        self.minstack = []

    def push(self, val: int) -> None:
        if not self.minstack:
            self.minstack.append((val, val))
        else:
            current_min = self.minstack[-1][1]
            self.minstack.append((val, min(val, current_min)))

    def pop(self) -> None:
        self.minstack.pop()

    def top(self) -> int:
        return self.minstack[-1][0]

    def getMin(self) -> int:
        return self.minstack[-1][1]
