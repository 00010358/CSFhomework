#Write a compare function that takes two values, x and y , and returns 1 if x> y , 0 if
#x == y , and -1 if x < y .
#Push code to your GitHub repository

def absolute_value(x,y):

	if x < y:
		return -1
	elif x > y:
		return 1
	else:
		return 0
print(absolute_value(1,2))
print(absolute_value(2,1))
print(absolute_value(1,1))

 # depends on the value you put



