def strcount(string):
    ucount,lcount=0,0
    for i in string:
        if str(i).isupper():
            ucount+=1

        elif str(i).islower():
            lcount+=1
    print('\n No of lowercase letters = %d\n No of uppercase letters = %d'%(lcount,ucount))

def alphabet(character):
    l=('a','e','i','o','u','A','E','I','O','U')
    if character in l:
        print("\n%s is a vowel"%(character))
    else:
        print('\n%s is a consonant'%(character))

def evenodd(list):
    flag=0
    for i in list:
        if i%2!=0:
            flag=1
            break
    if flag==1:
        print("\nlist contains some odd numbers")
    else:
        print("\nlist contains all even numbers")

def keycount(string):
    charcount,digicount,specount=0,0,0
    for i in string:
        if i.isalpha():
            charcount+=1
        elif i.isdigit():
            digicount+=1
        else:
            specount+=1
    print('\n The string %s contains\n%d letters\n%d Digits\n%d special symbols'%(string,charcount,digicount,specount))

def largest(list):
    print('\nthe largest number in the list is %d'%(max(list)))

def dictsum(dictionary):
    sum=0
    for i in dictionary.values():
        if str(i).isdigit():
            sum+=i
    print('\nthe sum of dict items is %s'%(str(sum)))

def prime(number):
    flag=0
    for i in range(2,number//2):
        if number%i==0:
            flag=1
            break
    if flag==1:
        print('\n%d is not a prime no'%(number))
    else:
        print('\n%d is a prime no'%(number))

def recPerimeter(length,breadth):
    # l,b=float(input('\nEnter the length of the rectangle: ')),float(input('\nEnter the breadth of the rectangle: '))
    if length<=0.0 or breadth<=0.0:
        print("Invalid Input\n Either Length or breadth is 0")
    else:
        print('\nperimeter of the rectangle is: %f'%(2*(length+breadth)))


        
        