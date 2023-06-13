# 출력할 단수를 입력하세요 6
# 6 * 1 = 6
# 6 * 2 = 12 

a = int(input("출력할 단수를 입력하세요"))

for i in range(1,10):
    print("{}*{}={}".format(a,i,a*i))
    