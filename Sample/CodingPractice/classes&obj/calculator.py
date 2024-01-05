class calculator:
    def __init__(self,a,b) -> None:
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
a,b=int(input('enter 1st no : ')),int(input('enter 2nd no : '))
ob=calculator(a,b)
while True:
    print('Menu\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\n')
    ch=int(input('enter your choice: '))
    if ch==1:
        print('sum= ',ob.add())
    elif ch==2:
        print('remainder= ',ob.sub())
    elif ch==3:
        print('product= ',ob.mul())
    elif ch==4:
        print('quotient= ',ob.div())
    elif ch==5:
        exit()
    else:
        print('invalid choice')



