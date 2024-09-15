import sys

def dec(A,b):
  x = []
  s = 0
  for i in range(len(A)):
    a = max(0,A[i]-b)
    s+=a
    x.append(a)
  return x,s

def counti(A):
  c = 0
  inInterval = False
  length = len(A)
  for i in range(length):
    if (A[i]==0 and i>0 and inInterval) or (i==length-1 and A[i]>0) :
      c+=1
      inInterval = False
    elif(A[i]>0):
      inInterval = True
      
  return c

def myMin(A):
  m = 1e10
  for a in A:
    if a < m and a>0:
      m = a
  return m
      

def solution(A):
  steps = 0
  sumA = sum(A)
  while(sumA>0):
    
    mini = myMin(A)
    intervals = counti(A)
    steps+=intervals*mini
    A,sumA = dec(A,mini)
    
  return steps

a = [2,2,0,0,1]
print(solution(a))
print(solution([1,2,3,4,5]))