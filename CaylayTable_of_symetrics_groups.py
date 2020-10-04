import numpy as np
import itertools
import pandas as pd



n = int(input("Ingrese el tamaño n del grupo de permutaciones: "));

array = [x+1 for x in range(n)];

posiblepermutations = list(itertools.permutations(array));

posiblepermutations = [list(x) for x in posiblepermutations];

cayleyTable = np.array([[object]*len(posiblepermutations)]*len(posiblepermutations));

def calculatePermutation(i,j):
     f = posiblepermutations[i];  
     g = posiblepermutations[j];    
     fog = [0]*n;
     k = 0;
     for index in g:
       fog[index-1] = f[k];
       k+=1;
     return fog;         

for i in range(len(posiblepermutations)):
  for j in range(len(posiblepermutations)):
    cayleyTable[i][j] = calculatePermutation(i,j);

labels= ["".join([str(_) for _ in a]) for a in posiblepermutations];
CayleyTable = pd.DataFrame(data=cayleyTable,columns=labels,index=labels);
CayleyTable

