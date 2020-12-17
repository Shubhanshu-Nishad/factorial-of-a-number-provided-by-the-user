# enumerate() Function

l = ['pen','pencil','copy','book']
# 1.pen
# 2.pencil
# 3.copy
# 4.book
i=1
for item in l:
    print(f"{i}.{item}")
    i=i+1
for item in enumerate(l):
    print(item)
for count ,item in enumerate(l):
    print(f"{count+1}.{item}")