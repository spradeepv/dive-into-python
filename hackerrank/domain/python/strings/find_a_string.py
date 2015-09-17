# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input()
sub_s = raw_input()
print len([i for i in range(len(s)) if s.startswith(sub_s, i)])