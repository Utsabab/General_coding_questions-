#Given a word find the all the possible combinations of that word and find it's rank in the sorted list of all the possible combinations.  
import itertools as it 

def rank_word(words):
  ob = []
  r = words
  for i in xrange(len(r)):
	  ob.append(r[i])

  a = set(list(it.permutations(ob)))

  a = sorted(a)

  l = ["".join(x) for x in a]


  #print a
  ob = tuple(ob)

  res = l.index(r)
  print res