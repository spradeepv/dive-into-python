def is_prime(num):
    is_prime = True
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                is_prime = False
                break
    else:
        is_prime = False
    #print num, " is prime ", is_prime
    return is_prime

def primes2(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n/3)
    for i in xrange(1,int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

n = int(raw_input())
prime_list = primes2(n)
#print prime_list
l = map(int, raw_input().split())
#print l
result = 0
for i in range(1, len(l)+1):
    for j in prime_list:
        if i+j < len(l)+1:
            #print l[i+j-1], l[i-1]
            result += l[i+j-1] - l[i-1]
        else:
            break
print result