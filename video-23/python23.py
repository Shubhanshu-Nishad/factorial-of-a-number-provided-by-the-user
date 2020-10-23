# function & docstring its very important 
# def meta():
#     print('shubhanshu')

def meta(name):
    """ function will wish a good morning """
    print("hi!", name , 'good morning ' )

name = input('entre your name :')
meta(name)
print(meta.__doc__) # print AIM OF FUNCTION
name2 = input("enter your name :")
meta(name)
name2 = input("enter your name :")
meta(name)
name2 = input("enter your name :")
meta(name)


def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""
    if num >= 0:
        return num # it works as a deliver boy 
    else:
        return -num # it works as a deliver boy 

print(absolute_value(12))
print(absolute_value(45))
print(absolute_value(-56))
