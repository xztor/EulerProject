import itertools
p5 = [pow(d,5) for d in range(10)]
print sum(
 set(
  filter(lambda x: x > 9,
         list(itertools.ifilter(
           lambda x: x == sum(map(lambda d: p5[int(d)], str(x))),
           itertools.chain.from_iterable(
            map(lambda i:map(
                  sum, itertools.combinations_with_replacement(p5, i)),
                range(2,7))
           )
         ))
  )
 )
)
