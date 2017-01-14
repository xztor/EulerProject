def cnt(s, c):
 if s < 0:
  return 0
 elif s == 0:
  return 1
 if len(c) <= 0:
  return 0
 m=max(c)
 return cnt(s-m, c) + cnt(s, filter(lambda x: x<m, c))

print cnt(200,[1,2,5,10,20,50,100,200])
