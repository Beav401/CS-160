def palindrome(myStr):
	back = [None]*len(myStr)
	for i in range(len(myStr)):
		back[len(myStr)-1-i] = myStr[i]
	if back == myStr:
		return "true"
	else:
		return "false"
	

'''def countStairs(n):
	if n < 0:
		return 0
	else n == 0:
		return 1
	else n == 1:
		return 1
	else n == 2:
		return 2
	else n == 4:
		return 4
	ielse
		return  countStairs(n-3)+countStairs(n-2)+countStairs(n-1):
'''	

