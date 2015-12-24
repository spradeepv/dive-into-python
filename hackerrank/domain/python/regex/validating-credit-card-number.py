"""
Problem Statement

You and Fredrick are good friends. Yesterday, Fredrick received N credit
cards from ABCD Bank. He wants to verify whether his credit card numbers are
valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

 It must start with a 4, 5 or 6.
 It must contain exactly 16 digits.
 It must only consist of digits (0-9).
 It may have digits in groups of 4, separated by one hyphen "-".
 It must NOT use any other separator like '  ' , '_', etc.
 It must NOT have 4 or more consecutive repeated digits.

Examples:

Valid Credit Card Numbers
---------------------------
4253625879615786
4424424424442444
5122-2368-7954-3214

Invalid Credit Card Numbers
---------------------------
42536258796157867       #17 digits in card number --> Invalid
4424444424442444        #Consecutive digits are repeating 4 or more times
--> Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used --> Invalid
44244x4424442444        #Contains non digit characters --> Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 --> Invalid

Input Format

The first line of input contains an integer N.
The next N lines contain credit card numbers.

Constraints

0<N<100
Output Format

Print 'Valid' if the credit card number is valid. Otherwise,
print 'Invalid'. Do not print the quotes.

Sample Input
------------
6
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Sample Output
------------
Valid
Valid
Invalid
Valid
Invalid
Invalid

Explanation
-----------
4123456789123456 : Valid
5123-4567-8912-3456 : Valid
61234-567-8912-3456 : Invalid, because the card number is not divided into
equal groups of 4.
4123356789123456 : Valid
5133-3367-8912-3456 : Invalid, consecutive digits 3333 is repeating 4 times.
5123 - 4567 - 8912 - 3456 : Invalid, because space ' ' and - are used as
separators.
"""
import re

for _ in range(int(raw_input())):
    credit_card_number = raw_input()
    if len(credit_card_number) == 16 or len(credit_card_number) == 19:
        if credit_card_number.count('-') == 3 and len(
                credit_card_number) != 19:
            print "Invalid"
            continue
        if credit_card_number.count('-') == 3:
            cc_split = credit_card_number.split('-')
            is_invalid = False
            for cc in cc_split:
                if len(cc) != 4:
                    is_invalid = True
                    break
            if is_invalid:
                print "Invalid"
                continue
            credit_card_number = credit_card_number.replace('-', '')
        #print credit_card_number
        start_pattern = r"[456]"
        digit_pattern = r"\d*([0-9])\1\1\1"
        start_match = re.match(start_pattern, credit_card_number)
        digit_match = re.match(digit_pattern, credit_card_number)
        #print start_match, digit_match
        if start_match and not digit_match:
            print "Valid"
        else:
            print "Invalid"
    else:
        print "Invalid"

for i in range(int(raw_input())):
    S = raw_input().strip()
    pre_match = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',S)
    if pre_match:
        processed_string = "".join(pre_match.group(0).split('-'))
        final_match = re.search(r'(\d)\1{3,}',processed_string)
        print 'Invalid' if final_match else 'Valid'
    else:
        print 'Invalid'