#@Function Name	: leftrotation
#@Description	: Rotates the given list with respect to the rotation ratio given 
#
#@Param 		: this function takes a string as and input . 
#				  The string is compose of the list that is to be rotated 
#				  and the ratio of in which the list is to be rotated. 
#
#Example		: Input : "1 2 3 4 5 /n 5" Output : 5 1 2 3 4


from collections import deque

#  this one is a little diffrent from the actual solution in hacker rank
def leftRotation(lrinput):
	inputForLeftRotation = lrinput.split("/n")

	listToRotate = deque(inputForLeftRotation[0].strip().split(" "))
	rotationRatio = - (int(inputForLeftRotation[1]) - 1)

	listToRotate.rotate(rotationRatio)

	return	' '.join(list(listToRotate))

leftRotation("1 2 3 4 5 /n 5")

# this one is the actual sloution passed in hacker rank solution 
def leftRotationhk(a, d):
    inputForLeftRotation = a
    
    listToRotate = deque(inputForLeftRotation)
    rotationRatio = - (d - 1)
    
    listToRotate.rotate(rotationRatio)

    print (' '.join(map(str, listToRotate)))

leftRotationhk([1,2,3,4,5], 5)
