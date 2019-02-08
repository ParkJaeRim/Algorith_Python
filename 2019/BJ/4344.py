sums = 0
cont = 0


for i in range(int(input())):
  ori = list(map(int, input().split(' ')))
  for j in range(1,len(ori)):
    sums += ori[j]
    
  avg_score = sums / ori[0]
  for j in range(1,len(ori)):
    if avg_score < ori[j]:
      cont += 1
  print('%0.3f%%' %(cont/ori[0]*100))
  cont = 0
  avg_score = 0
  sums= 0
