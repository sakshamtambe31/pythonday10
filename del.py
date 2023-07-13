classt test:
    def __init__(self):
        self.x=10
        self.y=20
        self.z=30
        self.a=40
    def display(self):
        print(self.x)
        print(self.y)
        print(self.z)
        print(self.a)
t=test()
t.display()
t1.test()
t1.display()
print(t.__dict__)
del t.z
print(t.__dict__)

    
