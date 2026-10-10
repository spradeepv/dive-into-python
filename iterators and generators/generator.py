# A generator simplifies this process. When Python sees yield,
# it automatically converts the function into a generator object
# that conforms to the iterator protocol.
def count_up_to(val):
    current = 1
    while current <= val:
        yield current
        current += 1

# Generator Usage
counter = count_up_to(3)
for num in counter:
    print(num) # Prints 1, 2, 3
