# RSA 

## Encode
 we need p and q is prime 
 
 n=q*p

 and we need e

 c = pow(msg,e,n) &harr; $m^{e} \bmod n$

```py
from Crypto.Util.number import bytes_to_long, getPrime
msg = bytes_to_long(b"flag{RSA_test}")
p = getPrime(100) # use getPrime to generate a prime number size 100 bits
q = getPrime(100)
n = q*p
e = 0x1001
c = pow(msg,e,n)
print(f"{p=}\n{q=}\n{n=}\n{e=}\n{c=}\n{msg=}")
```
Output:
```
p=905579929549289978626203301457
q=995862344126191665626049056093
n=901832951434587421317745781691260072484634477658475181627501
e=4097
c=674572929525085253698639630102704426247127624089692900361163
msg=2077392566271692732069336377947261
```

 
## Decode 

to decode the message, we need d

calculate d = e^-1 % (p-1)\*(q-1) &harr; $e{-1} \bmod (p-1)\*(q-1)$

how get q and p if you know n 

use [factorDB](http://www.factordb.com/index.php) But this does not work if the size of p and q are large enough and made the right way like use `getPrime`

after get p and q, we can calculate d

```py
p=905579929549289978626203301457
q=995862344126191665626049056093
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
```
now we can decode the message

```py
from Crypto.Util.number import long_to_bytes
e=4097
c=674572929525085253698639630102704426247127624089692900361163
p=905579929549289978626203301457
q=995862344126191665626049056093
n=p*q
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
msg = pow(c, d, n)
print(f"{long_to_bytes(msg)}")
```
Output:
```
b'flag{RSA_test}'
```
> you can use code below extract the data from the keys 

```python
from Crypto.PublicKey import RSA 

f = open('public.pem','r')
key = RSA.importKey(f.read())
print(key.n)
print(key.e)
```
or [this](https://lapo.it/asn1js/)
---
## **Common modulus attacker**

if c1 and c2 have same N and gcd(e1,e2) == 1 so:                 
$e1\*u + e2\*v = 1$

$c1 = m^(e1\*u)$                                   
$c2 = m^(e2\*v)$

$c1\*c2 == m^(e1\*u) \* m^(e2\*v)$ &rarr; $m^1 = m$

