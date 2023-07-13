class test:
    def __init__(self):
        self.x=10
        self.y=20
    def call(self):
        self.c=30
t=test()
t.call()
t.d=40
print(t.__dict__)
