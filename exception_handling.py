
def divide_by_zero():
	try:
		val1=int(input("enter the numerator:"))
		val2=int(input("enter the denominator:"))
		result=val1/val2
		print(result)
	except:
		if(val2==0):
			print("Division by zero is not possible!")

divide_by_zero()