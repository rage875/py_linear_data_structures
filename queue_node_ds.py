class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class QueueNodes:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self, data):
        node = Node(data)

        if self.front is None:
            self.front = node
            self.rear = self.front
        else:
            node.previous = self.rear
            self.rear.next = node
            self.rear = node

        self.count += 1

    def dequeue(self):
        current = self.front

        if current:
            if self.count == 1:
                self.front = None
                self.tail = None

            elif self.count > 1:
                self.front = current.next
                self.front.prev = None

            self.count -= 1

            return current.data
        else:
            print("Queue is empty")

