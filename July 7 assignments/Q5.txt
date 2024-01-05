#program to check whether 2 strings are located in same memory location
#consider two strings as Joel and Menezes
#direct method
s1,s2='Joel','Joel'
print(id(s1)==id(s2))


#user i/p
s1=input('enter 1st string: ')
s2=input('enter 2nd string: ')
print(id(s1),id(s2))
print('the given strings '+s1+' and '+s2+' having same address is ',id(s1)==id(s2))
#for direct it works but for strings it gives false and for single value string it gives true