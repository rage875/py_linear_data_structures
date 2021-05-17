class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data) -> None:
        node = Node(data)

        # Empty list
        if self.head == None:
            self.head = self.tail = node
            return

        # Not empty list
        node.next = self.head
        self.head.prev = node
        self.head = node
    
    def append(self, data):
        node = Node(data)

        # Empty list
        if self.tail == None:
            self.tail = self.tail = node

        # Not empty list
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def iterForward(self):
        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val


    def iterBackward(self):
        current = self.tail

        while current:
            val = current.data
            current = current.prev
            yield val

    def remove(self, data):
        current = self.head

        while current:

            if current.data == data:
                # Head scenario
                if current == self.head:
                    self.head = self.head.next
                    self.head.prev = None
                    return current

                # Tail scenario
                elif current == self.tail:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    return current

                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    return current

            current = current.next


    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!")

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0