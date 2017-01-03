# Q26:
# A unit fraction contains 1 in the numerator. The decimal representation of
# the unit fractions with denominators 2 to 10 are given:
# 
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.
# 
# Find the value of d < 1000 for which 1/d contains
# the longest recurring cycle in its decimal fraction part.

# Solution:
# 
# Find the number < 1000 with the highest discrete log for 10.
# This will be a prime p with discrete-log_10(1) mod p =  p - 1.
# We factor p - 1. Fermats little theorem gives us 10^(p-1) = 1 mod (p)
# Check that 10^x != 1 mod(p) for all proper factors of p-1. Then p - 1
# is the discrete log and thus the cycle length.
# 
# A prime p with max cycle at p-1, will have only one exponent, p - 1 itself,
# for which 10^x == 1 (mod p). So:
#  Find all factors of p - 1
#  Do modexp(10, x, p) for each factor.
#  Count the number of results = 1.
#  Filter for count = 1
#  Take the max of the primes that pass the filter. 

import sys
sys.path.insert(0, '../common/')
import utils

print max(filter(lambda p: map(lambda x: utils.modexp(10, x, p), utils.factors(p-1)).count(1)==1, utils.primes_until(1000)))
