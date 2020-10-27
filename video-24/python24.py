# local & global variables same as gunda & don

def f(): # treat as a home 
    """local & global variables"""
    global s # if you found s variables , then you changes its valuse
    print(s) # print shubhanhsu 
    s = 'subscribe' #  ghar ka saman local 
    print(s)
    print(d)

def g(): # treat podoasi 
    print(d)
    print(s)

# f() gives error
d = 'metaeducator' # shopkeeper saaman # global variable
s = ' shubhanshu '
g()
f()
g()

