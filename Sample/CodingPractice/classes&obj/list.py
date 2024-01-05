class list:
    def __init__(self) -> None:
        self.n=[]
    def add(self,a):
        self.n.append(a)
    def remove(self,a):
        self.n.remove(a)
        print('the list after deleting %d is '%(a),self.n)
    def display(self):
        print('the list is ',self.n)

ob=list()
while True:
    print('Menu\n1.Addition\n2.removal\n3.Display\n4.Exit\n')
    ch=int(input('enter your choice: '))
    if ch==1:
        a=int(input('enter ele to be appended: '))
        ob.add(a)
        print('list after adding is',ob.display())
    elif ch==2:
        a=int(input('enter ele to be removed: '))
        ob.remove(a)
    elif ch==3:
        ob.display()
    elif ch==4:
        exit()
    else:
        print('invalid choice')