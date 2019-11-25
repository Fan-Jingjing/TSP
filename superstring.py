# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 08:36:52 2019

@author: yangxue
"""
import numpy as np
import matching
from matching import max_bipartite_graph_match
import Hungarian
#%%
#%%



#pref(si,sj)
def pref (s1,s2):
    length1 = len(s1)
    length = min(length1, len(s2))
    k = max (range (0, length+1), key = lambda i:i if s1[length1-i:]==s2[:i] else False)
    return(length1 - k)
    
def find_path(self, x):
    self.visx[x] = True
    self.visy = np.array([False] * self.n, dtype=bool) 
    for y in range(self.m):
        if self.visy[y]: continue
        tmp_delta = self.lx[x] + self.ly[y] - self.graph[x][y]
        if  tmp_delta == 0:
            self.visy[y] = True
            if  self.match[y] == -1 or self.find_path(self.match[y]):
                self.match[y] = x
                return True
        elif self.slack[y] > tmp_delta:
            self.slack[y] = tmp_delta
    return False
    
#input the strings
s = []
S = input("S0: ")
i = 0
while S != ' ':
    s.append(S)
    i+=1
    S = input("S%d: "%i)

#build the adjacency matrix
vsize = len(s)
a = [[]for i in range (vsize)]
for i in range (vsize):
    for j in range (vsize):
        a[i].append(pref(s[i],s[j]))
#build a bipartite graph
maxlen = max(map(max,a))
alter_graph = [[]for i in range(vsize)]
for i in range(vsize):
    for j in range(vsize):
        if i==j:
            alter_graph[i].append(-maxlen-1)
        else:
            alter_graph[i].append(-a[i][j])
            
# find the maximum bipartite matching
alter= np.array(alter_graph)
self = max_bipartite_graph_match(alter)
#Hungarian Algorithm
edge = [[]for i in range (vsize)]
for i in range(vsize):
    for j in range(vsize):
        if self.lx[i]+self.ly[j] == alter_graph[i][j]:
            edge[i].append(1)
        else:
            edge[i].append(0)
cx = []
cy = []
visited = []
for i in range (vsize):
    cx.append(-1)
    cy.append(-1)
    visited.append(0)
match = Hungarian.DFS_hungary(vsize, vsize, edge, cx, cy, visited).match()
lengm = len(match)
Match = []
matching = []
for i in range (vsize):
    Match.append(match[lengm-1][i])
    matching.append(0)
for i in range (vsize):
    matching[Match[i][0]] = Match[i][1]
   
    

# find the cycle cover according to the matching
cycle_cover = []
i = 0
subcover = []
subcover.append(0)
j = 0
vis = np.zeros(vsize)
vis[0] = 1
while i < vsize:
    j = matching[j]
    if vis[j]==0:
        subcover.append(j)
        vis[j] = 1
    else:
        cycle_cover.append(subcover)
        for k in range(vsize):
            if vis[k] == 0:
                j = k
                break
        subcover = []
        subcover.append(j)
    vis[j] = 1
    i+=1

#Step2
cover_num = len(cycle_cover)
superstring = " "
pre = -1
for i in range(cover_num):
    for j in cycle_cover[i]:      
        if pre!=-1:
            superstring=superstring+s[pre][:a[pre][j]]
        pre = j
superstring= superstring+s[j]
superstring = superstring[1:]
print(superstring)
