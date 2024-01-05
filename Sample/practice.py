# print('hello world')
# """x=input('enter x value: ')
# print(x)"""
# print('amit \n\'108\'\nbhadana')
# i=2**3j #j is used to denote complex values
# print(type(i))


#if statement

#greatest of 2 numbers
# a,b=10,20
# if a > b:
#     print('a is greater than b')
# elif a==b:
#     print('a is equal to b')
# else:
#     print('b is greater than a')

#greatest of 3 numbers
# a,b,c=10,15,30
# if a>b and a>c:
#     print('a is greater than b and c')
# elif b>c:
#     print('b is greater than c and a')
# else:
#     print('c is greater than a and b')

#no is even or odd
# a=63
# if a<0:
#     print('no is negative')
# elif a%2:#a%2 for odd is not 0
#     print('no is positive and odd')
# else:
#     print('no is even and positive')

#loops
#table and factorial
# x=5
# i=1
# while i<=10:
#     print(x*i)
#     i+=1
# fact=1
# while x>0:
#     fact*=x
#     x-=1
# print(fact)

#print squares from 2-20
# n=2
# while n<=20:
#     print('square of the number ',n,' is ',n**2)
#     n+=1

#sum of digits of the number
# n=int(input('enter the number: '))
# sum=0
# while n!=0:
#     num=n%10
#     sum+=num
#     n=n//10
# print(sum)


#prime or not
# n=13
# i=2
# flag=True
# while i<n//2:
#     if n%i==0:
#         flag=False
#         break
#     i+=1
# if flag==True:
#     print(n,' is a prime no')
# else:
#     print(n,' is a not a prime no')

#lcm of 2 numbers
# a,b=15,20
# lcm=0
# for i in range(max(a,b),1+(a*b)):
#     if i%a==0 and i%b==0:
#         lcm=i
#         break
# print(lcm)
    


# for x in range(10,5,-3):
#     print('nag ',x)


#for else block
#else block will not execute if there is an exception in the for block or an _exit() function is called before it.

'''#list datatype**********
l1=[10,20,30,40,50,60]
# print(l1[::2])  
# print(l1[::-3])
# print(l1[-3:-1])
# print(l1[:])
# print(l1[::-1])
# print(l1[9:-7:-1])
#any range of the list outside index gives empty , but specific iutside index results in outofbounds error

# for x in l1:
#     print(x)
# print('----------------------------------')
# for x in l1[::-1]:
#     print(x) 

# for u,v in enumerate(l1): #to print index along with value
#     print(u,v)  

# l2=[10,20,30]
# l3=[40,50,60]
# l4=l2
# l5=[10,20,30]

# print(l2 is l4)
# print(l2==l5)
# print(l2!=l3)
# print(l2!=l5)
# == operator is used to check the data equality

# s1='joe'
# s2='joe'
# print(s1 is s2)

# print(10 in l1)
# print(200 in l1)

# print(20 not in l1)
# print(100 not in l1)'''

'''# l=['joe',11,10.5]
# a,b,c=l
# print(type(a),type(b),type(c))
'''

'''
li=[10,[22,33,44],'joel',[43,54,65]]

print(li[3])
print(li[1][2])
'''

'''
x=[i for i in range(10,20)]
print(x)

x=[i*i for i in range(21)]
print(x)

x=[i+1 for i in range(10,20,2)]
print(x)
'''

'''
#append function on list
#adds new element at the end
list=[10,20,30]
list.append(50)
list.append('qwerty')
print(list)
'''

'''#inserting elements based on index and combining 2 lists using + operator
list=[10,20,30]
list.insert(2,'jio')
list.insert(-1,89)
l1=list
print(list)
list.insert(-2,8)
l2=list
print(l1+l2)'''


# #string replication
# l=[1,2,3]
# print(l*3) #op=[1, 2, 3, 1, 2, 3, 1, 2, 3]

# m=l
# n=l.copy() #copies elements of l into n
# print(n)
# print(l is n) #address is different


l=[2,'orange',3,4,5,'orange']
# k=[3,4]
# l.extend(k) #it only takes list as the argument and is used to extend the existing string by add the string given in the argument of it
# print(l)

#used to modify value of the string directly
# l=['rat','hen']
# print(l)
# l[0]='tiger'
# print(l)


# animal=['lion','hyena']
# print(animal)
# animal[1]='tiger'
# print(animal)
# animal[1:3]='h','g','h'
# print(animal)

#list indexing
# print(l.index(2))
# print(l.index('orange',2)) #indexing is case sensitive and 2 is to find the second occurrence of orange

# print(l.count(2)) #works for all types of strings
# # print(l.reverse()) #reverse and sort doesnt work for heterogeneous lists
# # print(l.sort())
# print(l)
# l.remove('orange')#takes one argument and deletes the first element encountered and return type is None
# print(l)


#pop
# l.pop()
# print(l)
# l.pop(0)
# print(l)
# print(l.pop())
# print(l)


# #delete statement
# del l[0]
# print(l) #['orange', 3, 4, 5, 'orange']
# del l[:]
# print(l) #[]

#emptying the list
# print(l)
# l.clear()
# print(l) #[]


# p=[2,3,4,5,6,7]
# m=[]
# n=[]
# for x in p:
#     if x<5:
#         m.append(x)
#     elif x>5:
#         n.append(x)
# print(m,n)


# t1=(10)
# print(type(t1))

# t2=(10,)
# print(type(t2))

# t3=()
# print(type(t3))


#TUPLE***********
# a=6,6,8
# print(a)  #prints a tuple but not the recommended practice
# a=(2,1,99)
# print(a) #prints a tuple and is the recommended practice

h='gllfldlsl'
# d=tuple(h)
# e=list(d)
# print(type(d),type(e))
# print(list(d),d) #can convert a single string into a list of all its elements


# t=((10,20),(30,40,50))
# # for x in t:
# #     print(x)
# for x,y in t:
#     print(x,y) #10 20 30 40 for ((10,20),(30,40)) #for ((10,20),(30,40,50)) gives error


# t=tuple(x*10 for x in range(10,99,4)) #should mention tuple or it will print only memory address, for list only [] works list mention is optional
# print(t) 
# q=(3,4,[],5) #a list can be added to the tuple
# print(q)
# q[2].append(h) #that list can be appended
# print(q,id(q))
# q[2].append('hhhh')
# print(q,id(q))

#to update or add element into the tuple, it should be converted to list ,and turned back to tuple again


# t=(30,10,10,20)
# print(sorted(t,reverse=True),t) #sorted(tuple) is the function for tuple which sorts the tuple and displays as a list, sort is for list
# #by default reverse is set to False

#SET*****************
# set={1,2}
# print(set)

# set.update([4,5],(9,2,1))
# print(set)

# set.remove(9) #if ele present then its removed else error is shown
# print(set)
# set.discard(10) #if ele is present its discarded else no error is shown
# print(set)
# set.pop() #pops random element of the set
# print(set)
s={'apple',1,2,3}
# s.clear() #gives set() as op
# print(s)

# for no in s:
#     print(no)


# for letter in set('apple'):
#     print(letter)

l=[12,13,14,55,12,55,33,12,66,14,77]
# l1=set()
# l2=set()
# for x in l:
#     if x>15: 
#         l1.add(x)
#     elif x<15:
#         l2.add(x)
# # print(l1,l2)
# print(l)
# l=set(l)
# print(l)
# l=list(l)
# print(sorted(l,reverse=True))

#DICTIONARY*********************
pb={}
# print(pb,type(pb))
pb['joel']=12345
pb['Joel']=67890
pb['JOEL']=88888
print(pb)
# pb={ 'Khun':32145,'Joel':68709}
# print(pb)
# print(pb['Khun']) #returns value associated with the key else error if key invalid
# print(pb.get('Khn')) #returns value associated with the key else returns None
# print(pb.keys())
# print(pb.values())
# a=pb.items()
# print(a,type(a))
# for i in pb:
#     print(i,pb[i])
# for k,v in pb.items():
#     print(k,' : ',v)

#del and pop gives key error when key is not found
# print(pb.pop('Khun')) #displays the pop value after deleting it
# del pb['Joel'] #doesnt display the delete value after deleting it
# print(pb)

#x={**pb}
#print(x)
#pb1={'ratan':9087,'yaz':22222}
# pb1,pb2=[1,2,3],['opop','hito','olpa']
# x=zip(pb1,pb2)
# d=dict(x)
# print(d)


#Functions************************
#Factorial n Square using function
# def sq(n):
#     return n*n
# def fact(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# n=int(input('enter the no: '))
# print(fact(n))
# print(sq(n))

#print(globals()['a']+globals()['b']) #used to access global variables locally

###################
# n=100
# def check(n):
#     if n>0:
#         def square():
#             return n*n
#         square()
#         print('global n value is',globals()['n'],' local value is ',n)
#     else:
#         return 0
# check(15)
###################
# def thrive(n):
#     if n % 15 == 0:
#        print("thrive", end =' ')
#     elif n % 3 != 0 and n % 5 != 0:
#        print("neither", end = ' ')
#     elif n % 3 == 0:
#        print("three", end = ' ')
#     elif n % 5 == 0:
#        print("five", end =' ')
#     else:
#        print('hey')

# thrive(35)
# thrive(60)
# thrive(15)
# thrive(39)


























































































