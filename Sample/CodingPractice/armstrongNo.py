#armstrong number#

n=input('enter the no : ')
l=list(n)
sum=0
# print(l)
# print(len(l))
for i in l:
    sum+=int(i)**len(l)
# print(sum)
if sum==int(n):
    print('%s is a armstrong number'%(n))
else:
    print('%s is not a armstrong number'%(n))

