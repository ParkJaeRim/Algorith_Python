a = [88,30,61,55,95]

for i in range (0, 5):
  if a[i] < 60:
    print('%d번 학생은' % (i+1), '%d점으로 불합격입니다.' % a[i])
  else:
    print('%d번 학생은' % (i+1), '%d점으로 합격입니다.' % a[i])
