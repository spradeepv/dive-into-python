# Python List vs. Tuple

The core distinction between a list and a tuple in Python comes down to **mutability and intent**: lists are mutable sequences designed for collections of items that may change, whereas tuples are immutable sequences designed for fixed collections of data.

## Key Differences

| Feature | List | Tuple |
| :--- | :--- | :--- |
| **Mutability** | **Mutable** (items can be added, removed, or changed after creation). | **Immutable** (items cannot be modified, added, or removed after creation). |
| **Syntax** | Defined using square brackets: `[1, 2, 3]` | Defined using parentheses: `(1, 2, 3)` |
| **Performance** | Slightly slower and consumes more memory due to dynamic resizing overhead. | Faster execution and lower memory overhead due to fixed allocation. |
| **Dictionary Keys** | Cannot be used as dictionary keys or stored in sets (unhashable). | Can be used as dictionary keys or stored in sets (hashable), provided elements are also immutable. |
| **Built-in Methods** | Rich set of modification methods (`append()`, `extend()`, `remove()`, `pop()`, `sort()`, etc.). | Limited methods (`count()`, `index()`). |
| **Primary Intent** | Homogeneous data collections that undergo dynamic changes. | Heterogeneous structure (e.g., coordinate pairs `(x, y)`), record-like data, or write-protected data. |

---

## Code Comparison

### 1. Mutability and Modifications

```python
# List - Mutable
my_list = [10, 20, 30]
my_list[0] = 99         # Allowed
my_list.append(40)      # Allowed
print(my_list)          # Output: [99, 20, 30, 40]

# Tuple - Immutable
my_tuple = (10, 20, 30)
# my_tuple[0] = 99      # Raises TypeError: 'tuple' object does not support item assignment
# my_tuple.append(40)   # Raises AttributeError: 'tuple' object has no attribute 'append'
```

### 2. Memory Footprint and Performance

```python
import sys

list_sample = [1, 2, 3, 4, 5]
tuple_sample = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(list_sample)} bytes")   # e.g., ~104 bytes
print(f"Tuple size: {sys.getsizeof(tuple_sample)} bytes") # e.g., ~80 bytes
```

### 3. Usage as Dictionary Keys

```python
# Tuple as Dictionary Key (Valid)
location_data = {
    (37.7749, -122.4194): "San Francisco",
    (40.7128, -74.0060): "New York"
}

# List as Dictionary Key (Invalid)
# location_data = {[37.7749, -122.4194]: "San Francisco"} 
# Raises TypeError: unhashable type: 'list'
```

---

## When to Use Which?

* **Use Lists when:**
  * You need to modify, append, remove, or reorder elements.
  * You are working with homogenous collections of variable length (e.g., a list of usernames, temperature logs).

* **Use Tuples when:**
  * Data should remain constant/protected throughout the program execution (write-protection).
  * You need to use the collection as a dictionary key or inside a set.
  * You are returning multiple values from a function.
  * You want slight performance and memory optimizations for fixed-size lookup data.
