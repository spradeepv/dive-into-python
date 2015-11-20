"""
Problem Statement

collections.deque()

Deque is a Double-Ended QUEue. It can be used to add or remove elements from both ends.

Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.

Learn more about , deque() methods
Learn more about, various approaches to working with deques, Deque Recipes

Example

Code

>> from collections import deque
>> d = deque()
>> d.append(1)
>> print d
deque([1])
>> d.appendleft(2)
>> print d
deque([2, 1])
>> d.clear()
>> print d
deque([])
>> d.extend('1')
>> print d
deque(['1'])
>> d.extendleft('234')
>> print d
deque(['4', '3', '2', '1'])
>> d.count('1')
1
>> d.pop()
'1'
>> print d
deque(['4', '3', '2'])
>> d.popleft()
'4'
>> print d
deque(['3', '2'])
>> d.extend('7896')
>> print d
deque(['3', '2', '7', '8', '9', '6'])
>> d.remove('2')
>> print d
deque(['3', '7', '8', '9', '6'])
>> d.reverse()
>> print d
deque(['6', '9', '8', '7', '3'])
>> d.rotate(3)
>> print d
deque(['8', '7', '3', '6', '9'])
Task

Perform append, pop, popleft and appendleft methods on an empty deque d.

Input Format

First line contains an integer N i.e. the number of operations.
Next N lines contain the space separated name of methods and values.

Constraints

0<N?100
Output Format

Print space separated elements of deque d.

Sample Input

6
append 1
append 2
append 3
appendleft 4
pop
popleft
Sample Output

1 2
"""
from collections import deque
d = deque()
for _ in range(int(raw_input())):
    cmd = raw_input().split()
    if len(cmd) > 1:
        getattr(d, cmd[0])(cmd[1])
    else:
        getattr(d, cmd[0])()
while len(d) > 0:
    print d.popleft(),
