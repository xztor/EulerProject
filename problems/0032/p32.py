import itertools

def pandigitals():
 for term_digits in itertools.combinations("123456789", 5): 
  for terms in itertools.permutations(term_digits):
   for split_point in range(1,5):
    a = int("".join(terms[:split_point]))
    b = int("".join(terms[split_point:]))
    p = a * b 
    if "".join(sorted(str(a)+str(b)+str(p))) == "123456789":
     yield (a,b)

pan_products = map(lambda (a,b): a*b, pandigitals())
print sum(set(pan_products))
