class BankAccount:
    def __init__(self,acno,bal,date_of_opening,cusname) -> None:
        self.acno=acno
        self.bal=bal
        self.date_of_opening=date_of_opening
        self.cusname=cusname
    def check_balance(self):
        print('Balance: %f'%(self.bal))
    def withdraw(self,amount):
        if self.bal>amount:
            self.bal-=amount
            self.check_balance()
            print()
        else:
            print("your acc has insufiecient balance for withdrawal")
    def deposit(self,amount):
        self.bal+=amount
        print('amount has been deposited to your account')
       
        self.check_balance()
        print()
c1=BankAccount(212,60000.0,'01-12-2022','H chirag shetty')
c2=BankAccount(213,5333.67,'05-07-2016','Akhil')
c1.check_balance()
c2.check_balance()
c1.withdraw(4000.0)
c2.withdraw(6000.37)
c1.deposit(1567.7)
c2.deposit(40799)
