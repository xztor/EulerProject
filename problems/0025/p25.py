#!/usr/bin/python
# -*- coding: latin-1 -*-
#
# The Fibonacci sequence is defined by the recurrence relation:
#
#	Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
#	Hence the first 12 terms will be:
#
#		F1 = 1
#		F2 = 1
#		F3 = 2
#		F4 = 3
#		F5 = 5
#		F6 = 8
#		F7 = 13
#		F8 = 21
#		F9 = 34
#		F10 = 55
#		F11 = 89
#		F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence
# to contain 1000 digits?

# SOLUTION:
# Rather than recursively compute the Fibonacci sequence, we use the analytic
# formula, Fn = (phi^n - (-phi)^-n)/sqrt(5). The (-phi)^-n can be ignored for
# large n. Smallest 1000 digit number is 10^999. We proceed from there.
import math
phi=(1+math.sqrt(5))/2
l=math.log(10)*999 + 0.5 * math.log(5)
print int(l/math.log(phi)+1)
