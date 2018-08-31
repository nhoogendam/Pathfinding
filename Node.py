class node:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.value = 65555
        self.coordinate = (-1,-1)

    def setValue(self, num):
        self.value = num

    def getValue(self):
        return self.value

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, num):
        self.x = num

    def setY(self, num):
        self.y = num

    def getNorth(self, matrix):
        return matrix[self.x][self.y - 1]

    def getSouth(self, matrix):
        return matrix[self.x][self.y + 1]

    def getEast(self, matrix):
        return matrix[self.x + 1][self.y]

    def getWest(self, matrix):
        return matrix[self.x - 1][self.y]

    def setCoor(self, x, y):
        self.coordinate = (x,y)

    def getCoor(self, coor):
        if coor == 1:
            return self.coordinate[0]
        elif coor == 2:
            return self.coordinate[1]

    def getNeighbors(self, matrix):
        nodes = []
        if self.getNorth(matrix) != None:
            nodes.append(self.getNorth(matrix))
        if self.getEast(matrix) != None:
            nodes.append(self.getEast(matrix))
        if self.getSouth(matrix) != None:
            nodes.append(self.getSouth(matrix))
        if self.getWest(matrix) != None:
            nodes.append(self.getWest(matrix))
        return nodes