class Trump:
    
    def __init__(self):
        self.cnt_building = 50
    def maemae(self, cnt):
        self.cnt_building += cnt
    
if __name__ == '__main__':
    t = Trump()
    print(t.cnt_building)
    t.maemae(7)
    print(t.cnt_building)
        
    
