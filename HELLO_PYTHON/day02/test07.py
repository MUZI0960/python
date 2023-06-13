# 홀/짝을 입력하세요 홀
# 나 : 홀
# 컴 : 홀 / 짝
# 결과 : 승리 / 패배
from random import random
#
# a= input("홀/짝을 입력하세요")
# print("나 :" + a)
#
# com = random()
#
# if(com>0.5):
#     b = "홀"
#     print("컴 : " + b)
# else :
#     b = "짝"
#     print("컴 : " + b)
#
# if(a==b):
#     print("승리")
# else :
#     print("패배")
    
com = ""
mine = ""
result = ""

# 거러바 위엄 like a lion~ ♡
mine = input("홀/짝을 입력하세요")

rnd = random()
if rnd > 0.5 :
    com = "홀"
else :
    com = "짝"
if com == mine :
    result = "승리"
else : 
    result = "패배"
    
print("나 : ", com)
print("컴 : ", mine)
print("결과 : ", result)

    




