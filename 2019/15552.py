import sys

how = int(input())

for i in range(how):
  a,b = map(int, sys.stdin.readline().split())
  print (a+b)
