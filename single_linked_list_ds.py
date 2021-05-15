class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class SingleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        node = Node(data)

        if self.head == None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node

        self.size += 1

    def append(self, data):
        node = Node(data)

        if self.tail == None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = node

        self.size += 1

    def iter(self):
        current = self.head

        while current:
            val = current.data
            current = current.next
            yield val

    def remove(self, data):
        current = self.head
        previous = self.head

        # Head scenario
        if current:
            if current.data == data:
                self.head = current.next
                self.size -= 1
                return current.data

        # All other nodes
        while current:
            if current.data == data:
                previous.next = current.next
                self.size -= 1

                # Tail scenario
                if current == self.tail:
                    self.tail = previous

                return current.data

            previous = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f"Data {data} found!")

    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0
