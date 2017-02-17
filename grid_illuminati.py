#This is a commonly asked question in Interviews. Usually for Dropbox and Google.
'''N is the number representing the N * N grid.
Lamps are the co-ordinates provided as an argument at which point lamps are located. Lamps illuminate along the horiziontal, vertical and diagonal line.
Query are the co-ordinates at which point we are supposed to check if that particular point is illuminated or not?
The catch is any lamps adjancent to or on the query point turns off. Check if that query point is still iluuminated?'''


def get_adjacent_lamps(query, N):
  adj_lamps = set()
  xquery = query[0]
  yquery = query[1]
  for i in xrange(xquery - 1, xquery + 2):
    for j in xrange(yquery - 1, yquery + 2):
      if i > 0 and i < N:
        if j > 0 and j < N:
          adj_lamps.add([i, j])
  return adj_lamps


def checkIllumination(N, lamps, queries):
  seen_queries = set()
  num_lamps = 0
  adjlamps_list = []
  if len(lamps) >= (N ** 2) / 2:
    return ["LIGHT"] * len(queries)
  for i in xrange(len(queries)):
    adjlamps_list.append(get_adjacent_lamps(queries[i]))

  for lamp in lamps:
    for i in xrange(len(queries)):
      query = queries[i]
      adj_lamps = adjlamps_list[i]
      if tuple(lamp) in adj_lamps:
        continue
      if tuple(query) in seen_queries:
        continue 
      else:
		    if lamp[0] == query[0] or lamp[1] == query[1] or (query[0] - query[1] == lamp[0] - lamp[1]) or (query[0] + query[1] == lamp[0] + lamp[1]):
		      seen_queries.add(query)
      if len(seen_queries) == len(queries):
        return ["LIGHT"] * len(queries)
  illumination = []
  for query in queries:
    if tuple(query) in seen_queries:
      illumination.append("LIGHT")
    else:
      illumination.append("DARK")
  return illumination


print illuminati(4, [[1,2], [2,3], [3,3], [4,3]], [[0, 1], [2, 2], [3, 2], [3, 1], [2, 3]])

