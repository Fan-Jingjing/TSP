# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import copy
#initiation
a = [[0,3,3,4,7,3],[3,0,3,4,5,5],[3,3,0,1,4,4],[4,4,1,0,5,5],[7,5,4,5,0,4],[3,5,4,5,4,0]]
v = []
n = 6
c = [0]*n
k = -1
#insert v0
v = []
c[0]=1
k = 0
#l= max weight
v.append(0)
while k<5:
    entry = []
    for i in range(0,k+1):
        for j in range(0,n):
            if c[j]==0:
                entry.append([a[v[i]][j],i,j])
    raw = min(entry)
    y = raw[2]
    x = raw[1]
    c[y] = 1
    v.insert(x+1,y)
    k+=1
v.append(0)
print(v)
