def sharp(x):
    result = 0
    if x == 2:
        return 2
    else:
        return sharp(x-1) ** x

def ndigits(x):
    quo = x / 10
    if quo == 0:
        return 1
    else:
        return ndigits(quo) + 1


print ndigits(1)

print ndigits(sharp(7)) + 2 * ndigits(sharp(6)) + ndigits(sharp(5)) + ndigits(sharp(4))