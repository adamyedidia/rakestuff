import matplotlib.pyplot as pl
import sys
import math

def allBinaryStrings(t):
	if t == 0:
		return [""]
	
	oneLess = allBinaryStrings(t-1)
	
	returnList = []

	for i in oneLess:
		returnList.append(i+"0")
		returnList.append(i+"1")

	return returnList

def countSwitches(s, originalChar="0"):
	if len(s) == 0:
		return 0
	
	lastChar = originalChar
	index = 0
	switches = 0

	while index < len(s):
		char = s[index]
		if char != lastChar:
			switches += 1
			lastChar = char	
		index += 1

	return switches

def allBinaryStringsWithAtMostPSwitches(t, p, originalChar="0"):
	allBinary = allBinaryStrings(t)

	returnList = []

	for s in allBinary:
		if countSwitches(s, originalChar) <= p:
			returnList.append(s)

	return returnList

def allBinaryStringsWithAtMostPBits(t, p):
	allBinary = allBinaryStrings(t)
	
	returnList = []

	for s in allBinary:
		if sum([int(x) for x in s]) <= p:
			returnList.append(s)

	return returnList
	
switches = allBinaryStringsWithAtMostPSwitches(7, 3)
bits = allBinaryStringsWithAtMostPBits(7, 3)

pl.plot([int(x, 2) for x in switches], [0.4]*len(switches), "bo")
pl.plot([int(x, 2) for x in bits], [0.6]*len(bits), "ro")
pl.show()

print allBinaryStringsWithAtMostPSwitches(5, 2)
print allBinaryStringsWithAtMostPBits(5, 2)
