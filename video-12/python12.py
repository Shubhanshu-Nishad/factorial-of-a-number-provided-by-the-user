# Write a python script to  calculate the  maximum runs a single batsman can score in an ODI or IPL i.e. according to user  input of  over maximum run  should be calculate .(with no 'no balls', no wides, no extras, and no overthrows)

#first method
# rohit sharma =  5*6 + 3 = 33 
# 49*33 + 6 *6 

# second method
# 5*6=30
# 251 *6 + 49*3 


over = int(input('enter the span of  overs : '))
# ball = 6* over
maxrun = ((over)*6*5 + 6) + (over-1) * 3  # second method
# maxrun = str((over - 1) * 33 + 36)
# print("Maximum run score by hit-man " + maxrun ) #first method
print("Maximum run score by hit-man " )
print( maxrun)
