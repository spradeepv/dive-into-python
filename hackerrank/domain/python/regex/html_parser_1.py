"""
Task

You are given an HTML code snippet of N lines.
Your task is to print start tags, end tags and empty tags separately.

Format for printing the result is:

Start : Tag1
End   : Tag1
Start : Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Start : Tag3
-> Attribute3[0] > None
Empty : Tag4
-> Attribute4[0] > Attribute_value4[0]
End   : Tag3
End   : Tag2
-> symbol indicates that tag contains an attribute. It is immediately followed by the name of attribute and attribute value.
> symbol acts as a separator of attribute and attribute value.

If an HTML tag has no attribute then simply print the name of the tag.
If an attribute has no attribute value then simply print the name of attribute value as None.

Note: Do not detect any HTML tag, attribute and attribute value, inside the HTML comment tags (<!-- Comments -->).Comments can be multiline also.

Input Format

First line contains, integer N, number of lines in HTML code snippet.
Next N lines contain, HTML code.

Constraints

0<N<100
Output Format

Print the HTML tags, attributes and attribute values in order of their occurence from top to bottom in the snippet.

Ensure proper formatting, as explained in the problem statement.

Sample Input

2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
Sample Output

Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
"""
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        for i in attrs:
            print "->", i[0], ">", i[1]
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        for i in attrs:
            print "->", i[0], ">", i[1]
s = ""
comment = False
for _ in range(int(raw_input())):
    temp = raw_input()
    if temp.find("<!--") != -1 and temp.find("-->") != -1:
        temp = temp[:temp.find("<!--")]
    elif temp.find("<!--") != -1:
        comment = True
    elif temp.find("-->") != -1:
        comment = False
        continue
    if temp.strip() and not comment:
        s += temp

parser = MyHTMLParser()
parser.feed(s)