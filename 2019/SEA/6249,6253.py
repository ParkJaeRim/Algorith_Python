#입,출력 모두 맞게 나오는데 홈페이지에서 틀렸다고 그런다..ㅠ


#6249

a=int(input())
c= []
d= [0]*10
while a>= 10:
  c.append(a%10)
  a= a//10
c.append(a)

for i in range(10):
  for j in range(len(c)):
    if i == c[j]:
      d[i] += 1
print("0 1 2 3 4 5 6 7 8 9")
for k in range(len(d)):
  print(d[k],end=' ' if k!=9 else "")
  
  
  
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
