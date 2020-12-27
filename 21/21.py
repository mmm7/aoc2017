# https://adventofcode.com/2017/day/21
import numpy as np

from input import C2,C3

#print(C2)
#print(C3)

S = np.array([[0,1,0],[0,0,1],[1,1,1]])
#print(S)

for i in range(5):
  print('================================',i)
  print(S)
  if len(S)%2==0:
    lines=[]
    for y in range(0,S.shape[1],2):
      line=[]
      for x in range(0,S.shape[0],2):
        print(x,y)
        inp=S[x:x+2 , y:y+2]
        line.append(C2[str(inp)])
      lines.append(np.concatenate(line))
    S = np.concatenate(lines, axis=1)
  else:
    lines=[]
    for y in range(0,S.shape[1],3):
      line=[]
      for x in range(0,S.shape[0],3):
        print(x,y)
        inp=S[x:x+3 , y:y+3]
        line.append(C3[str(inp)])
      lines.append(np.concatenate(line))
    S = np.concatenate(lines, axis=1)

print(S)
print(np.sum(S))
