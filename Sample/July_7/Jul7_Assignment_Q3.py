#find the sum of given 4 digit number w/o using loop

#consider the number as 5667
#direct method
# n=5667
# #a,b,c,d=int(n/1000),int((n/100)%10),int((n/10)%10),int(n%10)
# #sum=a+b+c+d
# #or
# sum=int(n/1000)+int((n/100)%10)+int((n/10)%10)+int(n%10)
# print('sum= ',sum)

# #using user input
# n=int(input('enter the no: '))
# #print(type(n))
# a,b,c,d=int(n/1000),int((n/100)%10),int((n/10)%10),int(n%10)
# print('the sum of ',n,' is: ',a+b+c+d)

#using string slicing
n=(input('enter the no: '))
# # print('sum= ',int(n[0])+int(n[1])+int(n[2])+int(n[3]))
#using map function
print(sum(map(int,n.strip())))
print()
# n=',,,,....rrrtttgg........banana...rrr'
# print(n.lstrip(',.rgt'))