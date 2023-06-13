# 1에서 45까지의 수 중 랜덤으로 중복없이 6개를 뽑으세요
from random import random

arr45 = [
    "고은지", "김지연", "김지현", "이혜연", "이상엽"    
    "문수정", "김의연", "정재환", "신유철", "이지영"    
    "고은지", "김지연", "김지연", "김지연", "김지연"    
    "고은지", "김지연", "김지연", "김지연", "김지연"    
    ]

for i in range(1000):
    rnd = int(random()*45)
    a = arr45[rnd]
    b = arr45[0]
    arr45[0] = a
    arr45[rnd] = b

# 내 방법
# for i in range(1, 45+1):
#     arr.insert(i, int(random()*46))
#
# for i in range(1000):
#     rnd = int(random()*5)
#     a = arr[rnd]
#     b = arr[0]
#     arr[0] = a
#     arr[rnd] = b

print(arr45[0], end=", ")
print(arr45[1], end=", ")
print(arr45[2], end=", ")
print(arr45[3], end=", ")
print(arr45[4], end=", ")
print(arr45[5], end="")
