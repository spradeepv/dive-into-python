def is_power2(num):
    return num != 0 and ((num & (num - 1)) == 0)


def log2(n):
  assert n > 0
  exp = 0
  while n:
    n >>= 1
    exp += 1
  return exp


def largest_exp_of_2_less_than(n):
  return log2(n) - 1


for _ in range(int(raw_input())):
    n = long(raw_input())
    start = 0
    while n != 1:
        start += 1
        if is_power2(n):
            n = n/2
        else:
            n -= 1 << largest_exp_of_2_less_than(n)
    if start % 2 != 0:
        print "Louise"
    else:
        print "Richard"

