# Enter your code here. Read input from STDIN. Print output to STDOUT
def base10toN(num, base):
    """Change ``num'' to given base
    Upto base 36 is supported."""

    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 37:
        raise ValueError("base must be between 2 and 36")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    return converted_string


for _ in range(int(raw_input())):
    n = int(raw_input())
    if n > 3:
        s = base10toN(n, 3)
        print s
        l = []
        sum = 0
        for i in range(len(s)):
            num = int(s[i])
            if num:
                m = len(s) - i - 1
                temp = (3 ** m) * num
                l.append(str(temp))
                sum += temp
        if sum - n != 0:
            print "left pan:", sum - n
        else:
            print "left pan:"
        print "right pan:", " ".join(l)
    elif n < 3:
        print "left pan:", 3-n
        print "right pan:", 3
    else:
        print "left pan:"
        print "right pan:", n