def genPrimes():
    prime = 2
    while True:
        is_prime = True
        for i in range(2, prime):
            if prime % i == 0:
                is_prime = False
                break
        if is_prime:
            yield prime
        prime += 1

f = genPrimes()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
print f.next()
