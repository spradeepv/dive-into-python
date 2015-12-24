"""
Problem Statement

42 is the answer to "The Ultimate Question of Life, The Universe, and Everything". But what The Ultimate Question really is? We may never know!

Given three integers, a, b, and c, insert two operators between them so that the following equation is true: a (operator1) b (operator2) c=42.

You may only use the addition (+) and multiplication (?) operators. You can't change the order of the variables.

If a valid equation exists, print it; otherwise, print This is not the ultimate question.

Input Format

A single line consisting three space-separated integers: a, b, and c.

Constraints:
0?a,b,c?42
Output Format

Print the equation with no whitespace between the operators and the three numbers. If there is no answer, print This is not the ultimate question.

Note: It is guaranteed that there is no more than one valid equation per test case.

Sample Input

Example 1:

12 5 6
Example 2:

10 20 12
Example 3:

5 12 6
Sample Output

Example 1:

12+5*6
Example 2:

10+20+12
Example 3:

This is not the ultimate question
Explanation

Example 3 is not the ultimate question, because no combination of operators will equal 42: 5+12+6=23?42
5+12?6=77?42
5?12+6=66?42
5?12?6=360?42
"""

a, b, c = raw_input().split()
a = int(a)
b = int(b)
c = int(c)

if (a + b +c) == 42:
    print str(a)+"+"+str(b)+"+"+str(c)
elif (a + b * c) == 42:
    print str(a)+"+"+str(b)+"*"+str(c)
elif (a * b + c) == 42:
    print str(a)+"*"+str(b)+"+"+str(c)
elif (a * b * c) == 42:
    print str(a)+"*"+str(b)+"*"+str(c)
else:
    print "This is not the ultimate question"