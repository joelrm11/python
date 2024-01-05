#lcm

m,n=int(input("enter 1st no: ")),int(input("enter 2nd no: "))
lcm=0
for i in range(max(m,n),1+(m*n)):
    if i%m==i%n==0:
        lcm=i
        break
print('lcm of %d and %d is %d'%(m,n,lcm))