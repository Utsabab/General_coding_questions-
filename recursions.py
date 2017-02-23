#find the sum of the list
def sum(lsi):
    if len(lsi) <= 1:
      return lsi[0] 
    else:
      return lsi[0] + sum(lsi[1:])
      
print (sum([1,2,3]))

#find the number of elements in an array 
def counter(lsi):
  if len(lsi) == 1:
    return len(lsi)
  elif len(lsi) > 1:
    return 1 + counter(lsi[1:])
    
print (counter([1,2,3,4,5,6,7,8,9,10]))
      
#find the max number in an array 
def maxnum(lsi):
  if len(lsi) == 1:
    return lsi[0]
  else:
    maxy = maxnum(lsi[1:])
    if maxy > lsi[0]:
      return maxy
    else:
      return lsi[0]
    
print maxnum([25,5,56,3])
    


