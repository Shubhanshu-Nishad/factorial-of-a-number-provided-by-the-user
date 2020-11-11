# writing in a file 
# use w (writing) if don't want old content 
# use a (append) if you  want old content 
with open('meta5.txt','a+') as file:
    # file.seek(50) # its works only when curser at the starting 
    file.write('\nsubscribe kar do ji ...... ')
    l = ['\n hi , i am learning python', ' from metaeducator', '\n i am very happy ']
    file.writelines(l)