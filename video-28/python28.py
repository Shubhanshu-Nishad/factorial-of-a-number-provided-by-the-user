# file handling 
# first method

# file1 = open('meta.txt')
# file2 = open('subscirbe.txt','r')
# # print(file) gives error because file variables contains many valuse 
# l1 = file1.read()
# l2 = file2.read()
# print(l1)
# print(l2)
# file1.close() # closing of file 
# file2.close()
# file1 = open('meta3.txt','w')
# print(file1.close())
# l3 = file1.read() # cannot read that why its gives error 

# Second method
with open('meta.txt') as file1:
    l = file1.read()
    print(l)

