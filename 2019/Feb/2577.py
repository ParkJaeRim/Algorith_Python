A= int(input())
B= int(input())
C= int(input())

ans = A*B*C
arr = list()
while ans >= 10 :
  i = ans % 10
  arr.append(i)
  ans = ans // 10
arr.append(ans)


for j in range(10):
    x= arr.count(j)
    print(x)
  
