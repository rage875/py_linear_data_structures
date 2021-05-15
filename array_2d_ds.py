from array_ds import Array

class Grid():
    def __init__(self, rows, cols, fill_value = None):
        self.data = Array(rows)
        for rows in range(rows):
            self.data[rows] = Array(cols, fill_value)

    def get_height(self):
        return len(self.data)

    def get_width(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""

        for i in range(self.get_height()):
            for j in range(self.get_width()):
                result += str(self.data[i][j])
                if(j != self.get_width() - 1):
                    result += ","

            result += "\n"
        return result

    def __rand_fill__(self):
        # random fill only work with Number and String types
        from string import ascii_uppercase, digits
        import random

        for i in range(self.get_height()):
            for j in range(self.get_width()):
                item = self.data[i][j]
                if type(item) == int:
                    item = int(random.randint(0, 300))
                elif type(item) == float:
                    item = float(round(random.random() * 300, 2))
                elif type(item) == str:
                    item = random.choice(ascii_uppercase + digits)
                else:
                    print("Error type no supported:{}".format(type(item)))

                self.data[i][j] = item
