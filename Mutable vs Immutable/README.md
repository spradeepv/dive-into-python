# Mutable vs. Immutable Objects in Python

In Python, every value is an object stored in memory. The distinction between **mutable** and **immutable** objects centers on whether an object's internal state or value can be changed after it is created.

---

## Key Definitions

* **Mutable Objects:** Objects whose memory content can be modified after creation without changing their identity (`id()`).
* **Immutable Objects:** Objects whose value cannot be altered once created. Any operation that appears to modify an immutable object actually creates a brand-new object in memory with a new identity (`id()`).

---

## Comparison Table

| Property | Mutable Objects | Immutable Objects |
| :--- | :--- | :--- |
| **In-Place Modification** | Allowed | Not allowed |
| **Memory Identity (`id()`)** | Remains the same after modification | Changes whenever the value changes |
| **Dictionary Key / Set Element** | Cannot be used (unhashable) | Can be used (hashable) |
| **Examples (Excluding List/Tuple)** | `dict`, `set`, `bytearray` | `int`, `float`, `str`, `bool`, `frozenset`, `bytes` |

---

## Examples

### 1. Mutable Object Example: `dict` (Dictionary)

When you update or add a key-value pair to a dictionary, Python alters the object in place at the same memory location.

```python
# Initial dictionary
user_info = {"name": "Alice", "role": "Admin"}
print("Initial id:", id(user_info))

# Modify an existing key
user_info["role"] = "Superadmin"

# Add a new key
user_info["active"] = True

print("Updated dict:", user_info)
print("Updated id:  ", id(user_info))  # ID remains identical
```

---

### 2. Immutable Object Example: `str` (String)

Strings cannot be modified in place. Operations like string concatenation or calling methods like `.upper()` return a new string instance entirely.

```python
# Initial string
greeting = "hello"
print("Initial id:", id(greeting))

# Concatenating creates a new object
greeting = greeting + " world"

print("Updated string:", greeting)
print("Updated id:    ", id(greeting))  # ID changes because a new object was created
```

Attempting to change a character in place raises an error:

```python
text = "Python"
# text[0] = "p"  # Raises TypeError: 'str' object does not support item assignment
```

---

### 3. Immutable Object Example: `int` (Integer)

Numbers in Python are completely immutable. Reassigning a variable through arithmetic generates a new integer object.

```python
count = 10
print("Initial id:", id(count))

count += 1  # Equivalent to count = count + 1

print("Updated count:", count)
print("Updated id:   ", id(count))  # ID changes
```

---

### 4. Immutable Object Example: `frozenset`

While a regular `set` is mutable, a `frozenset` is an immutable variant that cannot be altered after initialization.

```python
# Regular Set (Mutable)
tags = {"python", "coding"}
tags.add("developer")  # Works fine

# Frozen Set (Immutable)
frozen_tags = frozenset(["python", "coding"])
# frozen_tags.add("developer")  # Raises AttributeError: 'frozenset' object has no attribute 'add'
```

---

## Why Does This Matter?

1. **Function Arguments (Pass-by-Assignment):** Passing a mutable object (like a `dict`) into a function allows the function to modify the original object. Passing an immutable object (like an `int` or `str`) prevents unintended side effects because changes inside the function operate on local copies.
2. **Dictionary Keys & Set Elements:** Only immutable objects can be hashed and used as dictionary keys or stored in sets.
