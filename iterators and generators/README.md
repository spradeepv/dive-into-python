# Python Iterator vs. Generator

The core distinction between an iterator and a generator in Python comes down to **how they are constructed and memory management**: every generator is an iterator, but not every iterator is a generator.

---

## Key Differences

| Feature | Iterator | Generator |
| :--- | :--- | :--- |
| **Creation** | Created by defining a class with `__iter__()` and `__next__()` methods, or calling `iter()` on an iterable. | Created by defining a function using the `yield` keyword (or using generator expressions). |
| **State Tracking** | Must manually manage state variables in class attributes. | Python automatically saves function local variables and execution state across `yield` calls. |
| **Memory Efficiency** | High (yields/returns elements as needed). | High (uses lazy evaluation to generate items on the fly). |
| **Boilerplate Code** | Requires class boilerplate and explicit `raise StopIteration`. | Concise; implicitly handles `StopIteration` when the function exits. |

---

## Code Comparison

### 1. Custom Iterator Class
To create an iterator, you must define a class that implements the **Iterator Protocol** (`__iter__` and `__next__`).

```python
class CountUpTo:
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

# Usage
counter = CountUpTo(3)
for num in counter:
    print(num)  # Prints 1, 2, 3
```

### 2. Generator Function
A generator simplifies this process. When Python sees `yield`, it automatically converts the function into a generator object that conforms to the iterator protocol.

```python
def count_up_to(max_val):
    current = 1
    while current <= max_val:
        yield current  # Pauses function and returns value
        current += 1

# Usage
counter = count_up_to(3)
for num in counter:
    print(num)  # Prints 1, 2, 3
```

---

## When to Use Which?

* **Use Generators when:** You need to process large sequences without storing them in memory (e.g., reading huge log files line-by-line), or when writing quick, readable data streams.
* **Use Iterators when:** You need a complex class with custom internal state, extra methods (e.g., reset functionality, custom indexing, or helper operations), or state persistence beyond basic streaming.
