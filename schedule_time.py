#This was a Dropbox practice question coded in Dropbox Info session at Howard University.
"""The input is a list of tuples containing start and the end time for a meeting. We need to figure out the minimum possible rooms required for all the meeting"""


inp = [(1,7), (4,6), (2,5), (3, 8), (9,18)]
# 4

st_inp = []
for (s, e) in inp:
  st_inp.extend([(s, 'start'), (e, 'end')])

st_inp.sort()

c = 0
maxVal = 0

for (i, t) in st_inp:
  if t == 'start':
    c += 1
  else:
    c -= 1
  
  maxVal = max(c, maxVal)

print maxVal

  

