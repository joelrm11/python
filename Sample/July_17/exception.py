print('hi')
l=[2,3,4,5]

try:
    print(l[5])
    a=10/0
    print(a)
except ArithmeticError:
    print('ZeroDivisionError')
except IndexError:
    print('index error')
print('well well well')

try:
    a=10//0
    print(a)
except ArithmeticError as i:
    print(i)

print('end')



















