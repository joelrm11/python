l=[]
n=int(input('enter the no of integers to be added : '))
for i in range(n):
    val=int(input("enter %d number: "%(i)))
    l.append(val)
if len(l)==0:
    print('List is empty')
else:
    print('list ain\'t empty nikya')
    print(l)

l=list(set(l))
print('after removing the duplicates the new list is',l)

# for x in range(2,l//2):
#     if x%
