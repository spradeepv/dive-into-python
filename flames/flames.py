"""

"""
from collections import Counter

FLAMES = {'F': 'Friends', 'L': 'Love', 'A': 'Affection', 'M': 'Marriage',
          'E': 'Enemy', 'S': 'Sister'}

def get_common_letters_count(name_1, name_2):
    common_letters = 0
    l1 = Counter(name_1)
    l2 = Counter(name_2)
    for key in l1:
        if l2.has_key(key):
            val_1 = l1.get(key)
            val_2 = l2.get(key)
            if val_1 <= val_2:
                common_letters += val_1
            elif val_2 <= val_1:
                common_letters += val_2
    return common_letters

def flames(name_1, name_2):
    common_letters = get_common_letters_count(name_1, name_2)
    distinct_letters = (len(name_1) + len(name_2)) - (2 * common_letters)
    flames = "FLAMES"
    while len(flames) > 1:
        cycle = distinct_letters % len(flames)
        if cycle > 0:
            flames = flames[cycle:]+flames[0:cycle-1]
        elif cycle == 0:
            flames = flames[0:cycle-1]
    return flames

name_1 = raw_input("Enter name of the first person:")
name_2 = raw_input("Enter name of the second person:")
print FLAMES[flames(name_1, name_2)]