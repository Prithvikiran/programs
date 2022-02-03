class Leaky_stack:
    def __init__(self,size):
        self.array=[None]*size
        self.size=size
        self.head=0
        self.tail=0
    
    def push(self,val):
        if(self.head==self.size):
            self.head=0
        elif(self.tail==0):
            self.tail=0
            
        elif(self.tail==self.head):
            self.tail=self.tail+1
        self.array[self.head]=val
        self.head=self.head+1  
    
    def pop(self):
        if(self.tail==0):
            self.tail=0
        self.array[self.tail]=None
        self.tail=self.tail+1
        
    def display(self):
        print(self.array)
        



