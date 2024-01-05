try:
    n=int(input('enter the no: '))
    print(10/n)
# except ZeroDivisionError as a:
#     print('error = ',a)
# except ValueError as a:
#     print('error = ',a)
#or
except (ZeroDivisionError,ValueError) as a:
    print('error = ',a)
else:
    print('No exception in try')
finally:
    print('finally its done')
print('rest of the app')