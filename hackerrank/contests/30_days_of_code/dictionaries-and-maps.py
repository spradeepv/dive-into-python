"""
Problem Statement

Welcome to Day 8! Check out a video review of dictionaries and hashmaps
here, or just jump right into the problem.

You are given a phone book that consists of your friend's names and their
phone number. After that you will be given your friend's name as query. For
each query, print the phone number of your friend.

Input Format

The first line will have an integer N denoting the number of entries in the
phone book. Each entry consists of two lines: a name and the corresponding
phone number.

After these, there will be some queries. Each query will contain name of a
friend. Read the queries until end-of-file.

Constraints
A name consists of only lower-case English letters and it may be in the format
'first-name last-name' or in the format 'first-name'. Each phone number has
exactly 8 digits without any leading zeros.

1<=N<=104
1<=queries<=104

Output Format

For each case, print "Not found" without quotes, if the friend has no entry
in the phone book. Otherwise, print the friend's name and phone number. See
sample output for the exact format.

To make the problem easier, we provided a portion of the code in the editor.
You can either complete that code or write completely on your own.

Sample Input

3
sam
99912222
tom
11122222
harry
12299933
sam
edward
harry
Sample Output

sam=99912222
Not found
harry=12299933
"""
phone_dict = {}
for _ in range(int(raw_input())):
    name = raw_input()
    number = int(raw_input())
    phone_dict[name] = number
query = raw_input()
while query:
    if phone_dict.has_key(query):
        s = query + "=" + str(phone_dict.get(query))
    else:
        s = "Not found"
    print s
    query = raw_input()