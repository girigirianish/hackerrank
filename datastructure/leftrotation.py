#@Function Name	: leftrotation
#@Description	: Rotates the given list with respect to the rotation ratio given 
#
#@Param 		: this function takes a string as and input . 
#				  The string is compose of the list that is to be rotated 
#				  and the ratio of in which the list is to be rotated. 
#
#Example		: Input : "1 2 3 4 5 /n 5" Output : 5 1 2 3 4


from collections import deque

def leftrotation(lrinput):
	inputForLeftRotation = lrinput.split("/n")

	listToRotate = deque(inputForLeftRotation[0].strip().split(" "))
	rotationRatio = inputForLeftRotation[1];

	listToRotate.rotate(-4)

	return	' '.join(list(listToRotate))

leftrotation("1 2 3 4 5 /n 5")
