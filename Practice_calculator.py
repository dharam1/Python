#Simple Calculator
class calculator:
	def addition(self,n1,n2):
		return n1+n2
	def subtraction(self,n1,n2):
		return n1-n2
	def multiplication(self,n1,n2):
		return n1*n2
	def division(self,n1,n2):
		return n1/n2

print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
operation = int(raw_input("Enter Your Choice\n"))
n1 = int(raw_input("Enter 1st number"))
n2 = int(raw_input("Enter 2nd number"))
cal = calculator()
if(operation == 1):
	print "Addition is : ",cal.addition(n1,n2)
elif(operation == 2):
	print "Subtraction is :",cal.subtraction(n1,n2)
elif(operation == 3):
	print "Multiplication is :",cal.multiplication(n1,n2)
elif(operation == 4):
	print "Division is : ",cal.division(n1,n2)
else:
	print "Invalid Input"

