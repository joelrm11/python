#find index of specified character in a string
#consider string as "Joel royston Menezes"

#method 1 using index function
s="Joel royston Menezes"
print(s.index('o')) #op=1
print(s.index('M')) #op=13
print(s.index(' ')) #op=4(first space)


#method 2 using user given values
s=input("Enter the string : ")
print('string is '+s)

i=input("Enter the character of the string to find index : ")
print('character given is '+i)

print('Index of given character '+i+' is '+str(s.index(i)))

#method 3 using rindex fuction with user function (begins from right side of the string)
s=input("Enter the string : ")
print('string is '+s)

i=input("Enter the character of the string to find index : ")
print('character given is '+i)

print('Index of given character '+i+' is '+str(s.rindex(i)))