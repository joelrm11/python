#find the occurrence of given character in the string
#consider string as "Joel royston Menezes"

#method 1 using count('character',startindex,endindex) (index is optional) function
s='Joel royston Menezes'
print(s.count('e',2,7)) #op=1(2,7 is the range from index 2 to index 7)
print(s.count('o')) #op=3
print(s.count(' ')) #op=2(2 whitespaces are used)

# #method 2 using user given values
s=input("Enter the string : ")
print('string is '+s)

i=input("Enter the character of the string to find occurrence : ")
print('character given is '+i)

print('occurrence of given character '+i+' is '+str(s.count(i)))

#method 3 using count fuction with range user function 
print('string is '+s)

i=input("Enter the character of the string to find occurrence : ")
print('character given is '+i)

print('Index of given character '+i+' is '+str(s.count(i,-5,-1)))