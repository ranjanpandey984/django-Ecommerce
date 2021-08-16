a = int(input("enter a integer: "))

def reverseInt (int n):
	a = n % 10
	remainder = remainder * 10 + a
	n = n/10

	print(remainder)

reverseInt(a)