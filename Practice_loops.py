#print prime numbers from 1 to 100
def isPrime(num):
	f = 0
	for i in range(2,num/2+1):
		if (num%i == 0):
			return False
	return True
print "Prime Numbers are: "
for i in range(2,101):
	val = isPrime(i)
	if(val == True):
		print i