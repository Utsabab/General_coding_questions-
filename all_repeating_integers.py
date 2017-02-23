def smal(temp):
  S = {}
  new_list = []
  for i,x in enumerate(temp):
    
    if x in S:
      new_list.append(x)
    S[x] = i
  return new_list 

print smal(['2','2','3','4','1','1','12'])