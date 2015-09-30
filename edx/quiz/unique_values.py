"""
Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.
"""

def uniqueValues(aDict):
    l = []
    temp = {}
    for key, val in aDict.items():
        if temp.has_key(val):
            if l.count(val) > 0:
                l.remove(val)
        else:
            temp[val] = 1
            l.append(val)
    li = []
    for key, val in aDict.items():
        if val in l:
           li.append(key)
    li.sort()
    return li

aDict = {1:1, 2:1, 3:3, 4:2, 5:3}
print uniqueValues({1: 1, 2: 1, 3: 1})
print uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0})
