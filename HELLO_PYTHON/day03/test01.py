# 가위바위보 
from random import random


mine = ""
com = ""
result = ""

mine = input("가위 바위 보 중 입력하시오")

rnd = random()
if rnd < 0.3 :
    # com = "가위"
        if(mine=="가위") :
            result = "컴 : 가위 / 비겼습니다."
        elif(mine=="보") :
            result = "컴 : 가위 / 졌습니다."   
        else :
            result = "컴 : 가위 / 이겼습니다." 
elif rnd >= 0.3 and rnd < 0.6 :
    # com = "바위"
        if(mine=="바위") :
            result = "컴 : 바위 / 비겼습니다."
        elif(mine=="보") :
            result = "컴 : 바위 / 이겼습니다."   
        else :
            result = "컴 : 바위 / 졌습니다." 
else :
    # com = "보"
    if(mine=="보") :
            result = "컴 : 보 / 비겼습니다."
    elif(mine=="가위") :
        result = "컴 : 보 / 이겼습니다."   
    else :
        result = "컴 : 보 / 졌습니다." 

# print("com : ", com)

# if com == mine :
#     result = "비겼습니다."
# elif
#
# else :
#     result = "이겼습니다."
    
print(result)
    
    