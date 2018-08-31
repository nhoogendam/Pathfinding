#imports
import pygame, sys
import Flowfield

#Create Display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800,800))
pygame.display.set_caption("Pathfinding")

flowNodes = Flowfield.nodes

#Create Color Constants
FOREGROUND_COLOR = pygame.Color(117, 151, 216)
BACKGROUND_COLOR = pygame.Color(216, 197, 204)
BLACK = pygame.Color(0,0,0)

TILESIZE = 40


def display_tile(tilex, tiley, message, rectSize):
    cornerX = (tilex * rectSize)
    cornerY = (tiley * rectSize)
    pygame.draw.rect(DISPLAYSURF, FOREGROUND_COLOR, (cornerX, cornerY, rectSize, rectSize), 3)
    font = pygame.font.SysFont(None, 15)
    textSurf = font.render(str(message), True, BLACK)
    textRect = textSurf.get_rect()
    textRect.center = cornerX + int(rectSize / 2), cornerY + int(rectSize / 2)
    DISPLAYSURF.blit(textSurf, textRect)

def draw_Board(originX, originY):
    DISPLAYSURF.fill(BACKGROUND_COLOR)
    nodes = Flowfield.calc_integrated_field(flowNodes, originX, originY)
    for row in range(len(nodes)):
        for col in range(len(nodes[0])):
            coorX = nodes[row][col].getCoor(1)
            coorY = nodes[row][col].getCoor(2)
            message = nodes[row][col].getValue()
            if message > -1 and coorX != -1:
                display_tile(coorX, coorY, message, TILESIZE)
            else:
                pygame.draw.rect(DISPLAYSURF, BLACK, (coorX, coorY, TILESIZE, TILESIZE))

def clicked():
    mouseX, mouseY = pygame.mouse.get_pos()

    flowNodes[mouseX // TILESIZE][mouseY // TILESIZE].setValue(-1)

    print("X: " + str(mouseX // 40) + "  Y: " + str(mouseY // 40))

# def gameState(origin):



#Main Game Loop
while True:
    #Fill the surface white
    draw_Board(13,14)
    #Loop to check for a key or mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked()
        # if event.type == pygame.K_SPACE:
            # gameState()

    #Updates game state every frame
    pygame.display.update()





