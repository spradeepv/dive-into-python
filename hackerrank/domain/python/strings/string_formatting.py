import textwrap

n = int(raw_input())
width = len(bin(n)[2:])
for i in range(1, n+1):
    decimal = str(i)
    octal = oct(i)[1:]
    hexa = hex(i)[2:].upper()
    binary = bin(i)[2:]
    print " " * (width - len(decimal)) + decimal,\
        " " * (width - len(octal)) + octal, \
        " " * (width - len(hexa)) + hexa, \
        " " * (width - len(binary)) + binary
