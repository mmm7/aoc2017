# https://adventofcode.com/2017/day/21
import numpy as np

from input import C2,C3

S = np.array([[0,1,0],[0,0,1],[1,1,1]])
print(S)

for i in range(2):
  print('================================',i)
  if len(S)%2==0:
    for y in range(0,S.shape[1],2):
      for x in range(0,S.shape[0],2):
        print(x,y)
  else:
    for y in range(0,S.shape[1],3):
      for x in range(0,S.shape[0],3):
        print(x,y)
