import os
os.system('cls')


def solution(money):
    money = list(map(list,enumerate(money)))
    
    start = 2 if len(money) % 2 == 0 else 3
    for i in range(start, len(money)) :
        if i == len(money)-1 :
            pass
            #money[i] += max(money[1:i-1], key = lambda x : x[0]!=0)
        else :
            max_ = max(money[:i-1], key = lambda x : x[1])
            #money[i][1] += max(money[:i-1], key = lambda x : x[1])
    #print("result : ",money)
    return max(money)


print(solution([1,2,3,4,5,6,7,8,9,10]), 30)
#print(solution([1000,0,0,1000,0,0,1000,0,0,1000]), 3000)
#print("답:",solution([1,2,3,1]), 4)
"""

print(solution([1,1,4,1,4]), 8)

print(solution([1000,1,0,1,2,1000,0]), 2001)
print(solution([1000,0,0,0,0,1000,0,0,0,0,0,1000]), 2000)


print(solution([0,0,0,0,100,0,0,100,0,0,1,1]), 201)
print(solution([11,0,2,5,100,100,85,1]), 198)
print(solution([1,2,3]), 3)
print(solution([91,90,5,7,5,7]), 104)
print(solution([90,0,0,95,1,1]), 185)
print(solution([1, 2, 3, 1]))"""