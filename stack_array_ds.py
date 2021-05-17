from array_ds import Array

class StackArray:
    def __init__(self, capacity) -> None:
        self.data = Array(capacity)
        self.top = 0
        self.size = 0

    def push(self, data) -> None:
        if self.size < len(self.data):
            if self.size > 0:
                self.top += 1

            self.data[self.top] = data
            self.size += 1
        else:
            print("Stack is full")

    def pop(self):
        if self.size > 0:
            data = self.data[self.top]
            self.top -= 1
            self.size -= 1
            return data
        else:
            return "Stack is empty"

    def peek(self):
        if self.size > 0:
            return self.data[self.top]
        else:
            return "Stack is empty"
    
    def clear(self):
        self.size = 0
        self.top = 0
