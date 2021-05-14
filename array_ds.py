class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, item):
        self.items[index] = item

    def __rand_fill__(self):
        # random fill only work with Number and String types
        from string import ascii_uppercase, digits
        import random

        for i in range(len(self.items)):
            item = self.items[i]
            if type(item) == int:
                item = int(random.randint(0, 300))
            elif type(item) == float:
                item = float(round(random.random() * 300, 2))
            elif type(item) == str:
                item = random.choice(ascii_uppercase + digits)
            else:
                print("Error type no supported:{}".format(type(item)))

            self.items[i] = item

    def __sum__(self, str_mode = True):
        # sum only work with Number and String types
        import functools
        temp = self.items.copy()

        for i in range(len(self.items)):
            item = temp[i]

            if str_mode:
                if type(item) == int or type(item) == float:
                    item = str(item)
            else:
                if type(item) == str:
                    item = ord(item)

            temp[i] = item

        return functools.reduce(lambda a,b: a + b, temp)
