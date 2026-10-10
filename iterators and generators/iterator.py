# To create an iterator, you must define a class that
# implements the Iterator Protocol (__iter__ and __next__).
class CountUpToIter:
    def __init__(self, max_val):
        self.max_val = max_val
        self.current = 1

    def __iter__(self):
        return self  # The iterator returns itself

    def __next__(self):
        if self.current <= self.max_val:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration  # Signals end of iteration


# Iterator Usage
counter = CountUpToIter(3)
for num in counter:
    print(num)  # Prints 1, 2, 3
