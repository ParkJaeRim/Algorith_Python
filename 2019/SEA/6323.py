A= int(input())

problem_list = [0]*A

problem_list[0], problem_list[1] = 1,1


for i in range(2,A):
    problem_list[i] = problem_list[i-1] + problem_list[i-2]
  
print(problem_list)
