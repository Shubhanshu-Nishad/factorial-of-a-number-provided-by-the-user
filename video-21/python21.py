# # set is collection of well define object 
# thisset = {"apple","banana","cherry"}
# # print(thisset)
# print("bananarr"in thisset) # check elements present in set.
# thisset.add('subscribe') # for adding one elements
# thisset.update(["orange","mango","grapes"]) # for adding many  elements
# # thisset.remove('subscribeuu') # gives error if elements not exits
# thisset.discard('subscribeuu')
# thisset.pop() # remove random elements from the set
# print(thisset)
# # print(len(thisset)) # count the total no of elements
# set1 = {"a","b","c"}
# set2 = {1,2,3}
	
# set3 = set1.union(set2)
# print(set3)
set1 = {"a","b","c"}
set2 = {1,2,3}
	
set2.update(set1)
print(set1)
print(set2)