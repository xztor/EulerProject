# Common routines to deal with primes, factors et al.

import operator
import itertools

def isqrt(n):
 x = n
 y = (x + 1) // 2
 while y < x:
  x = y
  y = (x + n // x) // 2
 return x

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(m_known=10, primes_known=set([2,3,5,7]))
def primes_until(m):
 if m <= primes_until.m_known:
   return set(x for x in primes_until.primes_known if x <= m)
 else:
  p = reduce(operator.sub,
    (set(range(2*k,m+1,k))
      for k in primes_until(isqrt(m))), set([2]+range(3,m,2)))
  primes_until.m_known=m
  primes_until.primes_known = p
  return p

def isprime(n):
 s = isqrt(n)
 return all(n % p <> 0 for p in primes_until(s))

def factors(n):
 if n == 1:
   return set([1])
 p = sorted(primes_until(isqrt(n)), reverse=True)
 for f in sorted(primes_until(isqrt(n)), reverse=True):
   if n % f == 0:
     ff = factors(n/f)
     fff = set()
     for x in ff:
      fff.add(f*x)
     return ff | fff | set([f, n])
 return set([1, n])

def modexp(b, x, m):
 r = 1
 for i in bin(x)[2:]:
   r = r * r
   if i == '1':
     r = r * b
   r = r % m
 return r
