# 홀/짝을 입력하세요 홀
# 나 : 홀
# 컴 : 홀 / 짝
# 결과 : 승리 / 패배
from random import random
    
com = ""
mine = ""
result = ""

mine = input("가위/바위/보를 입력하세요")

rnd = random()
if rnd > 0.66 :
    com = "가위"
elif rnd > 0.33 :
    com = "바위"

else : 
    com = "보"

if com == "가위" and mine == "가위":    result = "비김"
if com == "가위" and mine == "바위":    result = "승리"
if com == "가위" and mine == "보":     result = "패배"

if com == "바위" and mine == "가위":    result = "패배"
if com == "바위" and mine == "바위":    result = "비김"
if com == "바위" and mine == "보":     result = "승리"
    
if com == "보" and mine == "가위":    result = "승리"
if com == "보" and mine == "바위":    result = "패배"
if com == "보" and mine == "보":     result = "비김"
    
print("나 : ", mine)
print("컴 : ", com)
print("결과 : ", result)

    




