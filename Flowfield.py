from Node import node

rowNum = 20
colNum = 20
nodes = [[node() for j in range(rowNum + 3)] for i in range(colNum + 3)]
openNodes = []

cols = len(nodes[0])
rows = len(nodes)
for row in range(rows):
    for col in range(cols):
        nodes[row][col].setX(col)
        nodes[row][col].setY(row)

##==============================================================
##==============================================================


# Prints out the neighbors of a single node
def printNeighbors(oneNode, matrix):
    return str(oneNode.getNorth(matrix).getValue()) + str(oneNode.getEast(matrix).getValue()) + \
    str(oneNode.getSouth(matrix).getValue()) + str(oneNode.getWest(matrix).getValue())


# Prints out the Value of the nodes
def printMatrixVal(twoDMatrix):
    cols = len(twoDMatrix[0])
    rows = len(twoDMatrix)
    for row in range(rows):
        for col in range(cols):
            if twoDMatrix[row][col].getValue() == None:
                print("N/A", end="\t")
            else:
                print(twoDMatrix[row][col].getValue(), end="\t")
        print()

# Resets the matrix to the default value of 65555
def resetMatrix(twoDMatrix):
    cols = len(twoDMatrix[0])
    rows = len(twoDMatrix)
    for row in range(rows):
        for col in range(cols):
            if row == 0 or col == 0 or row == len(twoDMatrix) - 1 or col == len(twoDMatrix[0]) - 1:
                twoDMatrix[row][col].setValue(-1)
            else:
                twoDMatrix[row][col].setValue(65555)
                twoDMatrix[row][col].setCoor(row - 1,col - 1)






##==============================================================
##==============================================================

## NAME: calc_integrated_field
## DESC: Calculates the integration field
## and then returns the list of nodes
## VAR:  nodes: array of nodes
##       row:   row of the origin
##       col:   col of origin
def calc_integrated_field(nodes, row, col):
    resetMatrix(nodes)
    # printMatrixVal(nodes)
    # Has to be less than 20
    origin = nodes[row][col]
    origin.setValue(0)
    openNodes.append(origin)

    while len(openNodes) != 0:
        node = openNodes.pop(0)
        neighbors = node.getNeighbors(nodes)
        for i in neighbors:
            if i.getValue() != -1:
                # printMatrixVal(nodes)
                if (node.getValue() < i.getValue()):
                    if not (i in openNodes):
                        openNodes.append(i)
                    i.setValue(node.getValue() + 1)
    return nodes

calc_integrated_field(nodes, 13,14)
print(printNeighbors(nodes[13][14],nodes))
printMatrixVal(nodes)
print(printNeighbors(nodes[13][14],nodes))
print(str(nodes[13][15].getValue()))

##==============================================================
##==============================================================







