

num = input("Enter Number: ")
num = int(num)

def countdown(n):

	if n <= 0:
		print('Blastoff!')
	else:
		print(n)
		countdown(n-1)

def countup(n):
	if n >= 0:
		print('Blastoff')
	else:
		print(n)
		countup(n+1)

if num > 0:
  # count down positive number
  countdown(num)
elif num < 0:
  # count up negative number
  countup(num)
else:
  # in case of 0, both functions will print 'Blastoff!'
  print('Blastoff!')
