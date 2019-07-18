def is_even( i ):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False 
    """

    remainder = i % 2
    return reminder == 0

# Use the even function later on in the cod
print("All numbers between 0 and 20: even or not")
for i in range(20):
	if is_even(i):
	    print(i, "even")
	else:
		print(i, "odd")

