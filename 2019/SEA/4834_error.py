a = int(input())
c=[]
d=[0]*10
wo= 0
for i in range(a):
  card_amount = int(input())
  card_num = int(input())
  
  while card_num >= 10:
    card_list = card_num % 10
    card_num = card_num // 10    
    c.append(card_list)
  c.append(card_num)
  
  for j in range(len(c)):
    for k in range(10):
      if c[j]==k:
        d[k]+=1
        
  
  wo = '#'
  wo += str(i+1)

  print(wo, d.index(max(d)),max(d))
  c=[]
  d=[0]*10
  
  
  2개의 숫자가 동일한 최대의 갯수를 갖을 때, 더 큰 수를 출력할 코드 미완
