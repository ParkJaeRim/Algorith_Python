T = int(input())
a = []
b = []
c=[]
for i in range(T):  
  number = int(input())
  hi = list(map(int, input().split()))
  a.append(max(hi))
  b.append(min(hi))
  c.append(a[i]-b[i])
  
  wo = '#'
  wo += str(i+1)
  print(wo, c[i])
