import re

for _ in range(int(raw_input())):
    s = raw_input()
    l = s.split(".")
    if len(l) == 4:
        is_valid = True
        for c in l:
            addr = int(c)
            if addr < 0 or addr > 255:
                is_valid = False
                break
        if is_valid:
            print "IPV4"
            continue
    else:
        ipv6 = s.split(":")
        is_valid = True
        if len(ipv6) == 8:
            pattern = r"^[0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f][0-9A-Fa-f]$"
            for addr in ipv6:
                if len(addr) < 4:
                    for i in range(4 - len(addr)):
                        addr = "0"+addr
                if re.match(pattern, addr):
                    continue
                else:
                    is_valid = False
                    break
            if is_valid:
                print "IPV6"
                continue
    print "Neither"