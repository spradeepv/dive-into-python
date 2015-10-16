"""
Task

You are given an HTML code snippet of N lines.
Your task is to print single?line comments, multi?line comments and data.

Format for printing the result is:

Single-line Comment
Comment
Data
My Data
Multi-line Comment
Comment_multiline[0]
Comment_multiline[1]
Data
My Data
Single-line Comment:
Note : Do not print data if data == '\n'.

Input Format

First line contains, integer N, number of lines in HTML code snippet.
Next N lines contain, HTML code.

Constraints

0<N<100
Output Format

Print the single?line comments, multi?line comments and data in order of their occurence from top to bottom in the snippet.

Ensure proper formatting, as explained in the problem statement.

Sample Input

4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
Sample Output

Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
Data
 Welcome to HackerRank
Single-line Comment
[if IE 9]>IE9-specific content<![endif]
"""
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print ">>> Multi-line Comment" if ("\n") in data else ">>> Single-line Comment"
        print(data.replace("\r", "\n"))
    def handle_data(self, data):
        if data.strip():
            print ">>> Data"
            print data

html = ""
for i in range(int(raw_input())):
    html += raw_input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()