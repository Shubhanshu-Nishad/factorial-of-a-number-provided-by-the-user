#  try except for handling errors
# a = int(input("enter any no "))
t=1
while t==1:
    try :
        a = int(input("Enter any number: "))
        t=2
        # print(b)
    except ValueError:
        print("you have enter string while you have to enter integers")
        t=1
    except NameError:
        print(" you have chosen wrong variables ")
        t=1
    except:
        print("you have enter wrong input ")
        t=1
print("you have enter right input")

