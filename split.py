"""
Split integer number to dividers
"""

def newDivider(divider:int):
	"""Add new divider to list"""
	print(divider)

def split_naiv(number: int):
	"""split by loop for all coices"""
	newDivider(1)
	x = 2
	while x<(number//2+1) and number>1:
		try:
			while number%x==0:
				number = number//x
				newDivider(x)
		except KeyboardInterrupt:
			print('Break on x =', x)
			print('Number left ', number)
			return
		x+=1
	if number!=1:
		newDivider(number)
	

#main
if __name__ == '__main__':
	number = int(input('Enter number: '))
	split_naiv(number)
	print('Done')