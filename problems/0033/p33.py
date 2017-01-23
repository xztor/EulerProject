import sys
sys.path.insert(0, '../common/')
import utils
def same():
 for n in range(10,100):
  for d in range(n+1, 100):
   nd = str(n)
   dd = str(d)
   if nd[0] == dd[1] and int(nd[1]) * d == n * int(dd[0]):
     yield n,d
   if nd[1] == dd[0] and int(nd[0]) * d == n * int(dd[1]):
     yield n,d

(n,d)=reduce(lambda (a,b),(d,c): (a*d,b*c), same(), (1,1))
print d/utils.gcd(n,d)
