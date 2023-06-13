class Vehicle:
    def __init__(self):
       print("생성자")
       self.cnt_wheel = 2
    
    def addWheel(self):
        self.cnt_wheel += 2
        
    def __del__(self):
        print("소멸자")
            
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.amount_fuel = 0
    
    def mantank(self):
        self.amount_fuel = 100
    
    def onedoller(self):
        if self.amount_fuel >= 100 :
            print("만땅")
            return
        self.amount_fuel+=1         
        
# a = Vehicle()
# print(a.cnt_wheel)
# a.addWheel()         
# print(a.cnt_wheel)    

b = Car()
print(b.amount_fuel)     
print(b.cnt_wheel)   
b.addWheel()  
b.mantank()
print(b.amount_fuel)
print(b.cnt_wheel)

