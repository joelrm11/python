# ###File Handling###
# #f=open(file,mode)

# #r=read,w=write,r+=opens for reading n writing(cnt truncate a file)
# #w+=for writing and reading(can truncate a file)
# #a=append,t=opens in text mode,b=opens in binary mode,x=open for exclusive creation,failing if the file already
# # txt=[66,65,67]
# # f=open('d:/sample.txt','wb')
# # bina=bytearray(txt)
# # f.write(bina)
# # print(f.closed)
# # f.close()
# # print('operations done')
# # print(f.name)
# # print(f.closed)
# # print(f.mode)
# # f=open('d:/sample.txt','a')
# # d='hi'
# # f.write(d)
# # f.close()
# # f=open('d:/sample.txt','r')
# # s=f.read()
# # print(s)
# import os

# with open('sample.txt','w') as fh:
#     fh.write("hi friends\nwelcome to pune")
# print(fh.closed)

# os.rename('d:/samp.txt','d:/sample.txt')
# os.remove('d:/des.txt')


# # f=open('sample.txt','r')
# # print(f.readline())
# # print(f.tell())

# # f.seek(0)
# # print(f.read(5))
# # print(f.tell())

# # f.seek(0)
# # print(f.readlines())
# # print(f.tell())

# # f.close()









# def outer_fun(a, b):
#     def inner_fun(c, d):
#         return c + d

#     return a
#     return inner_fun(a, b)

# result = outer_fun(5, 10)
# print(result)



def f(x, y, z): return x + y + z
f(2, 30, 400)




























































