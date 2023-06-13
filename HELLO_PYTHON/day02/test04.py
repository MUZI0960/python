# 1에서 5까지의 수 중 랜덤으로 중복없이 3개를 뽑으세요
from random import random

arr5 = [1,2,3,4,5]

for i in range(99):
    rnd = int(random()*5)
    a = arr5[rnd]
    b = arr5[0]
    arr5[0] = a
    arr5[rnd] = b

print(arr5[0], end=", ")
print(arr5[1], end=", ")
print(arr5[2], end="")
            #  end="\n"