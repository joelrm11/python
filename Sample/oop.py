#Oblest Orientated Programming#
###
# class Mc:
#     def mfunc(self):
#         print('good morning')

# obj=Mc()

# obj.mfunc()  # o/p=good morning

###
# class Myclass:
#     a,b=1,2
#     def add(self,a,b):
#         print(a+b)
# c=Myclass()
# c.add(3,4)#op=7
# c.add()
# print(c.a+c.b)#op=3

###
# class mclass:
#     def val(self,a,b):
#         print(a,b)
#         #conversion of local to class values
#         a,b=self.a,self.b
#     def add(self):
#         print(self.a+self.b)
# c=mclass()
# c.val(3,9)
# c.add()        

###
# a,b=100,200
# class mc:
#     a,b=1,2
#     def add(self):
#         print(a+b)
#         print(type(a))
#         print(globals()['a']+globals()['b'])
#         print(type(globals()['a']))
#         print(self.a+self.b)
#         print(type(self.a))
#     @staticmethod
#     def dis2():
#         print("google")
#         print(globals()['a']) #static method can access global variables
#         #print(self.a) #static method cannot access self variables
#     def dis1(self):
#         print('Yahoo')
#         print(self.a)
# # c1=mc()
# # c2=mc()
# # c3=c1
# # print(id(c1),id(c2),id(c3))
# # print(c1 is c2)
# # print(c1 is c3)
# # print(c1 is not c2)
# # print(c1 is not c3)
# c=mc()
# c.dis1()
# c.dis2()
# # c.add(10,20)
# # #Name-less Obj
# # mc().add(3,3)

###
# class mcl:
#     a,b=10,20
#     def __init__(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
#     def add(self,a,b):
#         print(a+b)
#         print(self.a+self.b)
# c=mcl(9,8)
# c.add(9,7)

### multiple constructor like init is used python uses the last specified constructor like shown in below code snippet
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def __init__(self, name, age,sal):
#     self.name = name
#     self.age = age
#     self.sal=sal

# p1 = Person("John", 36,20000)
# p2=  Person("kal",34,30000)
# print(p1.name)
# print(p1.age)
# print(p2.name)
# print(p2.age)

# class G:
#     def __init__(self,id,name,sal) :
#         self.id=id
#         self.name=name
#         self.sal=sal
#     def __del__(self):
#         print('destroyer of the worlds')
#     def __str__(self) -> str:
#         return "%d %s %g"%(self.id,self.name,self.sal)
    
# c=G(121,'amit',9087.6)
# print(c)
# c1=c
# c2=c
# c1=G(11,'amit2',9099.6)
# print(c1)
# c2=G(21,'amit3',90097.6)
# print(c2)
































