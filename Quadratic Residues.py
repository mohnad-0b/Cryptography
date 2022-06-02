
ints = [14, 6, 11]
p = 29
for a in ints:
    for x in range(1,p):
        if a == (x**2)%p: # a = x^2 mod p to find root
            print(x)
