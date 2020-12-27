# https://adventofcode.com/2017/day/21
import numpy as np

from input import C2,C3

#print(C2)
#print(C3)

S = np.array([[0,1,0],[0,0,1],[1,1,1]])
#print(S)

def _step_internal(S, C, size):
  lines=[]
  for y in range(0,S.shape[1],size):
    line=[]
    for x in range(0,S.shape[0],size):
      #print(x,y)
      inp=S[x:x+size , y:y+size]
      line.append(C[str(inp)])
    lines.append(np.concatenate(line))
  return np.concatenate(lines, axis=1)

def step(S):
  if len(S)%2==0:
    return _step_internal(S,C2,2)
  else:
    return _step_internal(S,C3,3)

for i in range(5):
  print('================================',i)
  print(S)
  S = step(S)

print(S)
print('1--->',np.sum(S))

for i in range(5,18):
  print('================================',i)
  S = step(S)
print('2--->',np.sum(S))
