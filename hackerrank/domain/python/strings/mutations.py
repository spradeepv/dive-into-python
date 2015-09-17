# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
i, c = raw_input().split()
index = int(i)
print s[:index]+c+s[index+1:]