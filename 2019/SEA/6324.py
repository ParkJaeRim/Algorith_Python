A= [1,2,3,4,3,2,1]
B=[]
print(A)
for i in range(len(A)-1):
  for j in range(len(A)-1,i,-1):
    if A[i] == A[j] :
      del(A[j])
      
print(A)
