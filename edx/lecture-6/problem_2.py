def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    newTup = ()
    index = 1
    for i in aTup:
        print index, i
        if index % 2 != 0:
            newTup += (aTup[index-1],)
        index += 1
    return newTup

#print oddTuples((10, 12, 0, 12, 19, 4, 4, 9, 9, 15))

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    max_key = None
    max_value = 0
    for key, values in aDict.items():
        print key, values
        result = len(values)
        print result, max_value
        if result >= max_value:
            max_value = result
            max_key = key
    return max_key


print biggest({'a': [16, 10, 10, 20, 2, 1, 17, 11], 'c': [1, 3, 8, 8, 16], 'b': [11, 1, 17, 12, 17, 19, 11], 'e': [13, 3], 'd': [18]})

