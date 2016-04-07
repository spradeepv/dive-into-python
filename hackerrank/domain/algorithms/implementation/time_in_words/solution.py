units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
         'nine', 'ten']
teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
         'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty']
h = int(raw_input())
m = int(raw_input())
text = ""
hour = units[h]
if m == 0:
    text = units[h] + " o' clock"
elif m > 0 and m <= 30:
    if m == 15:
        text = "quarter past " + hour
    elif m == 30:
        text = "half past " + hour
    else:
        t = m / 10
        o = m % 10
        if t == 1:
            if o >= 1:
                text = teens[o]
            else:
                text = tens[t]
        else:
            text = tens[t] + " " + units[o]
        text = text + " minutes past " + hour
elif m > 30 and m < 60:
    hh = h + 1
    if hh == 10:
        hour = tens[1]
    elif hh > 10:
        hour = teens[hh - 10]
    else:
        hour = units[hh]
    if m == 45:
        text = "quarter to " + hour
    else:
        m = 60 - m
        t = m / 10
        o = m % 10
        if t == 1:
            if o >= 1:
                text = teens[o]
            else:
                text = tens[t]
        elif t > 0:
            text = tens[t] + " " + units[o]
        else:
            text = units[o]
        text = text + " minutes to " + hour
print (text)
