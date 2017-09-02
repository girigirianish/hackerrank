from collections import deque

def leftrotation(lrinput):
	inputForLeftRotation = lrinput.split("/n")

	listToRotate = deque(inputForLeftRotation[0].strip().split(" "))
	rotationRatio = inputForLeftRotation[1];

	listToRotate.rotate(-4)

	print list(listToRotate)
	return

leftrotation("1 2 3 4 5 /n 5")
