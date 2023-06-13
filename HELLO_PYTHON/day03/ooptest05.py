from day03.ooptest02 import Trump
from day03.ooptest04 import LeeJY

class KimJH(Trump, LeeJY):
    
    def __init__(self):
        # super().__init__()
        Trump.__init__(self)
        LeeJY.__init__(self)
    
if __name__ == '__main__':
    k = KimJH()
    print(k.cnt_building)
    print(k.pocket)
    k.maemae(10)
    print(k.cnt_building)
    

      
    

        
        
        