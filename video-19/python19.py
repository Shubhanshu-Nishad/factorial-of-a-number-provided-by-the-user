# tuple ()

tup = ('meta','shubhuji','ram','rohan')
print(type(tup))
tup2 = ('komal',) # for creating single elements in tuple you have  to write , 
# print(type(tup2))
# print(tup.extend(tup2)) # tuple cannot change...
# print(tup[3]) # print index elements
# print(tup[2:]) # 1 to 2 (n-1)
print(tup[-4:-2]) # ('meta', 'shubhuji') starting, end
# del tup # it delete the tuple
# tup.remove('meta') # gives out error because tuple is not changeable
tup3 = tup + tup2 # for adding tuples you have to creta third tuple
print((tup3))
print(len(tup3))