def numSetBits(A):
	numofones = 0;
	while (A>0):
		remainder = A%2
		numofones += remainder 
		A = A/2 
	return numofones

print numSetBits(3) 
