#대문자를 소문자로 소문자를 대문자로 변환하고 아스키코드 출력
a = str(input())
b = ord(a)
if 64<b<91 or 96<b<123:
  if a.upper() != a:
    print('%s(ASCII: %d) => %s(ASCII: %d)' %(a,ord(a),a.upper(),(ord(a)-32)))
  else:
    print('%s(ASCaII: %d) => %s(ASCII: %d)' %(a,ord(a),a.lower(),(ord(a)+32)))
elif b <65 or 90< b <97 or b>122:
  print(a)
