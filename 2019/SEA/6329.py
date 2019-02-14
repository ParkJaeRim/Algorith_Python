A= str(input())

for i in range (len(A)):
    if i<len(A)//2 and round(len(A)//2) <len(A)-i-1:
        if A[i] == A[len(A)-i-1]:
            print('%s\n입력하신 단어는 회문(Palindrome)입니다.' %A)

'Palindrome 판단문제'
