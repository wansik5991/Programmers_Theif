import os
os.system('cls')


from copy import deepcopy
def solution(money):
    
    answer = -1
    for i in range(2) :
        lst = deepcopy(money)
        if i == 0 : lst[1] = lst[0];
        else : lst[0] = 0;

        for j in range(2, len(money) - (1-i)) :
            lst[j] = max(lst[j-1], lst[j-2] + lst[j])   
        answer = max(answer, max(lst))

    return answer

print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
print(solution([1,2,3,1]), 4)
print(solution([1,1,4,1,4]), 8)

print(solution([1000,1,0,1,2,1000,0]), 2001)
print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)
print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
print(solution([11,0,2,5,100,100,85,1]), 198)
print(solution([1,2,3]), 3)
print(solution([91,90,5,7,5,7]), 104)
print(solution([90,0,0,95,1,1]), 185)
print(solution([1, 2, 3, 1]))