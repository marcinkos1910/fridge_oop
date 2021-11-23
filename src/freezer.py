class Freezer:
    def __init__(self, volume):
        self.volume = volume
        self.products = [1, 2, 3]

    def __len__(self):
        return len(self.products)

    def __iter__(self):
        return self


f = Freezer(10)
print(len(f))
