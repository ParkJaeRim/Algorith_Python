#입,출력 모두 맞게 나오는데 홈페이지에서 틀렸다고 그런다..ㅠ

  #6253
  
a = int(input())
b=[]

if a % 2 ==0:
  b.insert(0,0)
else :
  b.insert(0,1)
  
while a>1:
  a = a//2  
  b.append(a%2)
  
b= list(reversed(b))
for i in range (len(b)): 
  print(b[i],end='')
