# calculator using function 

def add(num1,num2):
    print(num1+num2)

def sub(num1,num2):
    print(num1 - num2)

def mul(num1,num2):
    print(num1*num2)

def div(num1,num2): # formal parameter 
    s= 'this is actul parameter'
    print(num1/num2)

def cal():
    num1 = int(input("enter first number :"))
    num2 = int(input("enter second number :"))
    op = input("enter your operation for add , sub, mul, div +, -,*,/ respectively ")

    if op == "+":
        add(num1,num2)
    
    if op == "-":
        sub(num1,num2)

    if op == "*":
        mul(num1,num2)

    if op == "/":
        div(num1,num2)

# cal()
choice = 'y ' #  at least for one time calculation 
# choice = input("enter y if you want  calculation ")
# if choice=='y':
#     cal()
while choice == 'y':
    cal()
    choice = input("enter y if you want more calculation ")


# target improve this program 




