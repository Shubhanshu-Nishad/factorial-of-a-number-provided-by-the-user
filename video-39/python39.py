# *argv and **kwargs

# def myfun(*argv): # for passsing  multiple arguments 
#     sum1=0
#     for arg in argv:
#         sum1 += arg
#     print(sum1)
# myfun(2,4,5,4,5,5,58,978,6456,45,2)

# def fun(x,y,*argv):
#     sum1=0
#     for arg in argv:
#         sum1 += arg
#     print(sum1*2)
#     print(sum1/y)

# fun(2,4,5,6,7,8,19)

def myfun1(**kwargs):
    for i , j in kwargs.items():
        print(i, " ",j )
myfun1(meta ="educator ",shubhanshu="Nishad",like="subscribe",comment="share")