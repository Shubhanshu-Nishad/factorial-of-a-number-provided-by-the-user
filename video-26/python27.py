# features of function 

# x , y = 5 , 6 # only valid in python 
# print(x,y)

# first 
# def cal(x , y):
#    return x+y , x-y , x*y , x/y , x%y

# x = int(input('enter first number : '))
# y = int(input('enter second  number : '))
# add , sub ,  mul , div , mod = cal(x,y) 
# print(add)
# print(sub)
# print(mul)
# print(div)
# print(mod)

# second 
# si = p*r*t/100
def si(p=1000,r=5 , t=2): # if you not provide value of r & t , then it will use deafult value otherwise you provided value accepted 
    si =  (p*r*t)/100
    print('the si is :',si)

p = 2500
r = 10
t = 1
si(r,t)