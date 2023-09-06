input_drome = input("Enter Palindrome to check")
input_drome = input_drome.lower()
def checkPalindrome(P):
	mid_term = len(P)%2
	total_term = len(P)-mid_term #Here we are removing the mid term from the index
	isPalindrome = False
	for index,letter in enumerate(P):
		if(index % 2 == 1):
			isPalindrome = True
		elif (letter == P[-1-index]):
			isPalindrome = True
		else:
			isPalindrome = False
	return isPalindrome

print(checkPalindrome(input_drome))
