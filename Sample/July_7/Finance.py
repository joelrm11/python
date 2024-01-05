p=float(input('enter the principle: '))
t=float(input('enter the time:(in months) '))
r=float(input('enter the rate of interest: '))
sI=(p*t*r)/100.0
print('simple interest= ',sI)
compoundI=p*pow((1+r/100),t)
print('Amount= ',p+sI)
print('compound interest = ', compoundI)
