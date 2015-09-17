import textwrap

s = raw_input()
width = int(raw_input())
print "\n".join(textwrap.wrap(s, width))