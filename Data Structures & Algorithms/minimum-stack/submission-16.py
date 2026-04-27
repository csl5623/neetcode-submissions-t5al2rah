class MinStack:

    def __init__(self):
        self.min_value = 10934959044906896085
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        if val <= self.min_value:
            self.min_value = val
            self.min_values.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if len(self.stack) > 0:
            val = self.stack.pop()
            if val == self.min_value:
                if len(self.min_values) > 0:
                    self.min_values.pop()
                    if not self.min_values:
                        self.min_value = 48545745489548954758947895678567589675786586759765896756785
                    else:
                        self.min_value = self.min_values[-1]
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value
