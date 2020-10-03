# calculator
print("for addition , sub, mul , div enter + , -, * , / respetively ")
operation = input('enter your operation symbols : ')
print(operation)

a= int (input('enter first no : '))
b= int (input('enter secnod no : '))
exit()


if operation == "+" :
    if a==5 and b== 4:
        print(14)
        exit()
    print(a+b)
elif operation == '-':
    print(a-b)
elif operation == '*':
    print(a*b)
elif operation == '/':
    print(a/b)
else:
    print('Sorry !!! , you have enter wrong operation')


# 5+4 = 9 , 14
# 5*9= 20 , 46
#6/3=2 , 10
# 7-4=3, 24