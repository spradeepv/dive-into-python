"""
Problem Statement

You are given an HTML code snippet of N lines.
Your task is to detect and print all HTML tags, attributes and attribute values.

Print the detected items in the following format:

Tag1
Tag2
-> Attribute2[0] > Attribute_value2[0]
-> Attribute2[1] > Attribute_value2[1]
-> Attribute2[2] > Attribute_value2[2]
Tag3
-> Attribute3[0] > Attribute_value3[0]
-> symbol indicates that tag contains an attribute. It is immediately followed by the name of attribute and attribute value.
> symbol acts as a separator of attribute and attribute value.

If an HTML tag has no attribute then simply print the name of the tag.

Note: Do not detect any HTML tag, attribute and attribute value, inside the HTML comment tags (<!-- Comments -->).Comments can be multiline also.
All attributes have an attribute value.

Input Format

First line contains, integer N, number of lines in HTML code snippet.
Next N lines contain, HTML code.

Constraints

0<N<100
Output Format

Print the HTML tags, attributes and attribute values in order of their occurence from top to bottom in the snippet.

Ensure proper formatting, as explained in the problem statement.

Sample Input

9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
Sample Output

head
title
object
-> type > application/x-flash
-> data > your-file.swf
-> width > 0
-> height > 0
param
-> name > quality
-> value > high
Explanation

head tag : Simply print head tag as it has no attribute.

title tag: Simply print title tag as it has no attribute.

object tag: Print object tag.
In next 4 lines print attributes type, data, width and height along with their respective values.

<!-- Comment --> tag: Don't detect anything inside it.

param tag: Print param tag.
In next 2 lines print attributes name and value along with their respective values.
"""

from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        for i in attrs:
            print "->", i[0], ">", i[1]
    def handle_endtag(self, tag):
        pass
    def handle_startendtag(self, tag, attrs):
        print tag
        for i in attrs:
            print "->", i[0], ">", i[1]
html = ""
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
        html += temp

parser = MyHTMLParser()
parser.feed(html)
