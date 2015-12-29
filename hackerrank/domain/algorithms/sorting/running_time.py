"""

"""
def insertionSort(ar):
    length = len(ar)
    stop = False
    index = 1
    running_time = 0
    while not stop:
        num = ar[index]
        for i in range(index - 1, -1, -1):
            if num < ar[i]:
                ar[i + 1], ar[i] = ar[i], num
                running_time += 1
        index += 1
        if index == length:
            stop = True
    print running_time

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)