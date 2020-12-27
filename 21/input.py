import sys
import numpy as np

#    ../.# => ##./#../...
#    .#./..#/### => #..#/..../..../#..#

C2 = {}
C3 = {}

def de(c): return (0,1)[c=='#']

for l in sys.stdin:
  l = l.strip()
  if not l: continue
  ss,tt = l.split(' => ')
  s=np.array(tuple([tuple(map(de,x)) for x in ss.split('/')]))
  t=np.array(tuple([tuple(map(de,x)) for x in tt.split('/')]))
  #print(s,'\n',t)
  assert (len(s), len(t)) in ((2,3), (3,4)), (s,'\n',t)
  C = (C2,C3)[len(s)!=2]
  for _ in range(2):
    for _ in range(4):
      C[str(s)]=t
      s=np.rot90(s)
    s=np.transpose(s)
