# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

class Trie:
    def __init__(self, data=""):
        self.data = data
        self.num = len(self.data)
        self.children = {}

    def push(self, data):
        if not data:
            return 0
        if (len(data)<=len(self.data)) and (data==self.data[:len(data)]):
            return 0
        if len(data)>=len(self.data) and (self.data==data[:len(self.data)]):
            #try to push to the children
            key = data[len(self.data)]
            if self.children.has_key(key):
                result = self.children[key].push(data[len(self.data):])
                print result
            else:
                self.children[key] = Trie(data[len(self.data):])
                result = self.children[key].num
            self.num += result
            return result
        #partial match
        index = 1
        while (index<len(data)) and (data[:index]==self.data[:index]):
            index +=1
        #split off part of the old data
        elem = Trie(self.data[index-1:])
        elem.children = self.children
        elem.num = self.num-(index-1)
        self.data = self.data[:index-1]
        self.children = {}
        self.children[elem.data[0]] = elem
        newelem = Trie(data[index-1:])
        self.children[data[index-1]] = newelem
        result = newelem.num
        self.num += newelem.num
        return result

    def multipush(self, str):
        result = 0
        for i in range(len(str)):
            result = result + self.push(str[i:])
            print result
        return result

    def get(self, num, data = ""):
        if self.num<num:
            return "INVALID"
        if self.data and num<len(self.data):
            return data + self.data[:num+1]
        decrement = len(self.data)
        for key in sorted(self.children.keys()):
            if (decrement+self.children[key].num)>num:
                return self.children[key].get(num-decrement, data+self.data)
            else:
                decrement = decrement+self.children[key].num
        return "INVALID"

    def out(self, data=""):
        if self.data:
            print data+self.data+" "
        for key in sorted(self.children.keys()):
            self.children[key].out(data+self.data)

def readLine():
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        quit()
    return line

def readNum():
    line = readLine()
    if not line:
        return -1
    try:
        num = int(line)
    except ValueError:
        return -1
    return num

t = Trie()
num = readNum()
if num==-1:
    quit()

for n in range(num):
    line = readLine()
    if not line:
        break
    t.multipush(line.strip())

num = readNum()
if n==-1:
    quit()

for n in range(num):
    k = readNum()
    if k==-1:
        quit()
    print t.get(k-1)
