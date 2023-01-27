# -*- coding: utf-8 -*-
"""python_assignment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tVUDxxtLzMGxHltOUfqk3LzNLHzkQHI-
"""

def dfs(l,i,j):
  
  if(i<0 or i>=len(l) or j<0 or j>=len(l[0]) or l[i][j]=="X" ):
    return 
  l[i][j]="@"
  dfs(l,i,j+1)
  dfs(l,i,j-1)
  dfs(l,i+1,j)
  dfs(l,i-1,j)

"""m=int(input("enter the number of rows"))
n=int(input("enter the number of columns"))
l=[]
for i in range(m):
  t=[]
  print("Enter the values for",i,"row")
  for j in range(n):
    x=input()
    t.append(x)
  l.append(t)

"""
l= [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

for i in range(len(l)):
  if(l[i][0]=="O"):
    dfs(l,i,0)
  if(l[i][len(l[0])-1]=="O"):
    dfs(l,i,len(l[0])-1)

for j in range(len(l[0])):
  if(l[0][j]=="O"):
    dfs(l,0,j)
  if(l[len(l[0])-1][j]=="O"):
    dfs(l,len(l)-1,j)

for i in range(len(l)):
  for j in range(len(l[0])):
    if(l[i][j]=="O"):
      l[i][j]="X"
    if(l[i][j]=="@"):
      l[i][j]="O"


print(l)