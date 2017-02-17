class Aristas():
    def __init__(self, node1, node2):
        self.xPos1 = node1.xPos
        self.yPos1 = node1.yPos
        self.xPos2 = node2.xPos
        self.yPos2 = node2.yPos

class Node():
	def __init__(self, xPos, yPos):
		self.xPos = xPos
		self.yPos = yPos