# 1에서 45까지의 수 중 랜덤으로 중복없이 6개를 뽑으세요
from random import random

arr45 = [
    1,2,3,4,5,   6,7,8,9,10,
    11,12,13,14,15,   16,17,18,19,20,
    21,22,23,24,25,   26,27,28,29,30,
    31,32,33,34,35,   36,37,38,39,40,
    41,42,43,44,45
    
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
