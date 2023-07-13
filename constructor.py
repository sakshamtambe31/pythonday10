class student:
    def __init__ (self,n,p,r):
        self.name=n
        self.per=p
        self.rollno=r
        print('Hello Constructor')

    def display(self):
        print('Name: ',self.name)
        print('Percentage :',self.per)
        print('rollno :',self.rollno)

n=input(("Enter name"))
p=float(input("per"))
r=int(input("roll no"))
s=student(n,p,r)
s.display()
