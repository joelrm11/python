###simple parent child inheritance###

# class parent:
#     def m1(self):
#         print('parent class')
# class child(parent):
#     def m2(self):
#         print('child class')
# p=parent()
# p.m1()
# c=child()#can access both parent and child class
# c.m1()
# c.m2()

###
# class a:
#     def __init__(self,name):
#         print('A class cons')
#         self.name=name
# class b(a):
#     # def __init__(self,name):
#     #     print('B class cons')
#     #     self.name=name
#     def disp(self):
#         print(self.name)
# be=b('konan')
# be.disp()



###
class emp:
    def __init__(self,id) -> None:
        self.id=id
        print('in emp class')
class manager(emp):
    def __init__(self, id,incentive) -> None:
        super().__init__(id)
        self.incentive=incentive
        print('in manager class')
m=manager(988,90870)








