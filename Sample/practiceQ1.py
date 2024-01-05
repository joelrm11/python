class employee:
    def __init__(self,empname,empid,empsal,empdept) -> None:
        self.empid=empid
        self.empname=empname
        self.empsal=empsal
        self.empdept=empdept
    def print_emp_details(self):
        print('\nEmployee name=%s\nEmployee ID=%s\nEmployee salary=%d\nEmployee department=%s' % (self.empname,self.empid,self.empsal,self.empdept))
    def assign_department(self,empdept):
        self.empdept=empdept
        print('\n%s\'s department has been changed to %s\n updated details for %s are\n'%(self.empname,self.empdept,self.empname))
        self.print_emp_details()
    def calc_empsal(self,empsal,hw):
        if hw>50:
            ot=hw-50
            ot_amount=(ot*(empsal/50))
            self.empsal+=ot_amount
        
        else:
            print('overtime not done by %s'%(self.empname))
        


e1=employee('adams','e7876',50000,'accounting')
e2=employee('jones','e7499',45000,'research')
e3=employee('martin','e7900',50000,'sales')
e4=employee('smith','e7698',55000,'operations')
print('employee details are: \n',)
e1.print_emp_details()
e1.print_emp_details()
e2.print_emp_details()
e3.print_emp_details()
e1.assign_department('marketing')
e4.calc_empsal(55000,60)
e4.print_emp_details()

