# lambda function 
# def add(num1,num2):
#     print(num1+num2)
#     print(num1-num2)

# def sub(num1,num2):
#     print(num1 - num2)

# def mul(num1,num2):
#     print(num1*num2)

# def div(num1,num2): # formal parameter 
#     s= 'this is actul parameter'
#     print(num1/num2)

# add2 = lambda num1,num2, :(num1+num2) 
# sub2 = lambda num1,num2 :(num1-num2) 
# mul2 = lambda num1,num2 :(num1*num2) 
# div2 = lambda num1,num2 :(num1/num2) 


# def cal():
#     num1 = int(input("enter first number :"))
#     num2 = int(input("enter second number :"))
#     op = input("enter your operation for add , sub, mul, div +, -,*,/ respectively ")

#     if op == "+":
#         print(add2(num1,num2))
#         # print(add2)
    
#     if op == "-":
#         print(sub2(num1,num2))

#     if op == "*":
#         print(mul2(num1,num2))

#     if op == "/":
#         print(div2(num1,num2))

# cal()
# choice = 'y ' #  at least for one time calculation 
# # choice = input("enter y if you want  calculation ")
# # if choice=='y':
# #     cal()
# while choice == 'y':
#     cal()
#     choice = input("enter y if you want more calculation ")

x = lambda a,b ,c,h: a+b+c+h
print(x(5,3,8,9))
print(x)