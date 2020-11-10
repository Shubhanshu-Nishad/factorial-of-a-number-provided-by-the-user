# reading 
with open('meta.txt','r+') as file:
    l = print(file.read())
    l = print(file.readlines()) # a list of lines from cursers
    file.seek(50) # it count no of character from starting always 
    l = print(file.readline()) # print a first lines lines  from cursers
    # file.seek(52) # it count no of character from starting always 
    h = print(file.readline()) # print a first lines lines  from cursers
    h = print(file.readlines()) # a list of lines from cursers   
   