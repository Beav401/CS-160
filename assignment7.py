'''def f(num):
	r=num/2
	while abs(num-(r**2))>.00000000000001:
		r=(r+(num/r))/2
	return r

def f(letter):
	if (letter<"A") or (letter>"Z"):
		return False
	else:
		return True

def f(n):
	for i in range(n):
		for j in range(n):
			res = i*j
			print(str(res), end=" ")
		print()'''


def addOne(nums):
	new = []
	for x in range(len(nums)):
		new.append(nums[x]+1)
	return new

def rawGradeToLetter(x):
	if x>90:
		return "A"
	elif x>80:
		return "B"
	elif x>70:
		return "C"
	elif x>60:
		return "D"
	else:
		return "F"

def convertRawsToLetters(nums):
	new = []
	for x in range(len(nums)):
		new.append(rawGradeToLetter(nums[x]))
	return new

def ouncesToCups(nums):
	new = []
	for x in range(len(nums)):
		new.append(nums[x]*0.125)
	return new

def glassOfWater(nums):
	new = []
	for x in range(len(nums)):
		new.append(nums[x]/8)
	return new

def hydrated(ouncesConsumed):
	glasses = glassOfWater(ouncesConsumed)
	if glasses[0]>8:
		return "Hydrated"
	else:
		return "Not Hydrated"

def waterNeeded(ouncesConsumed):
	needed = hydrated(ouncesConsumed)
	if needed == "Hydrated":
		return 0 
	else: 
		glasses = glassOfWater(ouncesConsumed)
		return 8 - glasses[0]

