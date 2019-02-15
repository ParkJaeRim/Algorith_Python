A= int(input())
if A == 1 or A == 2 :
  print('소수입니다.')

i = 2 
while i<A:  
  if A%i == 0:
    a= '소수가 아닙니다.'
    break;
  else:
    a = '소수입니다.'
    i+=1
    
print(a)
