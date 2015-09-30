"""
Problem Statement

CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).

Specifications of HEX Color Code
? It must start with a '#' symbol.
? It can have 3 or 6 digits.
? Each digit is in the range of 0 to F. (i.e. 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E and F).
? A-F letters can be in lower case too. (i.e. a, b, c, d, e and f are also valid digits).

Examples

Valid Hex Color Codes
#FFF
#025
#F0A1FB

Invalid Hex Color Codes
#fffabg
#abcf
#12365erff
You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

CSS Code Pattern

Selector
{
	Property: Value;
}
Input Format

First line contains, integer N.
Next N lines contain, CSS Code.

Constraints

0<N<50

Output Format

Output colour codes with '#' in separate lines.

Sample Input

11
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}
Sample Output

#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff
Explanation

#BED and #Cab satisfy the Hex Color Code criteria but they are used as selectors and not as color codes in the given CSS.

Hence, valid color codes are:
#FfFdF8
#aef
#f9f9f9
#fff
#ABC
#fff

Note: There are no comments ( // or /* */) in CSS Code.
"""

import re

#n = int(raw_input())
n = 1
for i in range(n):
    #s = raw_input()
    s = "color: #FfFdF8; background-color:#aef;background-color:#cef;#FfFdF8"
    #s = "background: -webkit-linear-gradient(top, #f9f9f9, #fff);"
    #s = "#BED"
    #s = "background-color: #ABC;"
    #pattern = re.compile('.*?(#([a-fA-F0-9]{3}){1,2}).*?(#([a-fA-F0-9]{3}){1,2}).*?')
    pattern = re.compile('.*?(#([a-fA-F0-9]{3}){1,2}).*?')
    #pattern = '([\(\)\w\s:\,])+(#([a-fA-F0-9]{3}){1,2}).*?([\w\s\;-])+:((#([a-fA-F0-9]{3}){1,2}))*'
    for i in re.finditer(pattern, s):
        print i.group()
    matchGrp = pattern.match(s)
    if matchGrp:
        print "Matches", matchGrp.group(), len(matchGrp.groups())
        for i in matchGrp.groups():
            print i
