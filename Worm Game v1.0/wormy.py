import random, pygame, sys
from pygame.locals import *

FPS = 30
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
CELLSIZE = 20
assert WINDOW_WIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOW_HEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELL_WIDTH = int(WINDOW_WIDTH / CELLSIZE)
CELL_HEIGHT = int(WINDOW_HEIGHT / CELLSIZE)

white = ("white")
black = ("black")
red = ("red")
green = ("green")
darkgreen = ("darkgreen")
darkgray = ("darkgray")
bg_color = black

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

HEAD = 0 # syntactic sugar: index of the worm's head

def main():
    global FPSCLOCK, screen, font
    
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    font = pygame.font.Font("freesansbold.ttf", 18)
    pygame.display.set_caption("Worm Game")
    
    showStartScreen()
    running = True
    while running:
        runGame()
        showGameOverScreen()
        
def runGame():
    #set a random start point
    startx = random.randint(5, CELL_WIDTH - 6)
    starty = random.randint(5, CELL_HEIGHT - 6)
    wormCoordinates = [{'x': startx,      'y': starty},
                       {'x': startx - 1, 'y': starty},
                       {'x': startx - 2, 'y': starty}]
    direction = RIGHT
    
    #start the apple in a random place 
    apple = getRandomLocation()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()
            
            # check if the worm has hit itself or the edge
            if wormCoordinates[HEAD]['x'] == -1 or wormCoordinates[HEAD]['x'] == CELL_WIDTH or wormCoordinates[HEAD]['y'] == -1 or wormCoordinates[HEAD]['y'] == CELL_HEIGHT:
                return #for game over
            for wormBody in wormCoordinates[1:]:
                if wormBody['x'] == wormCoordinates[HEAD]['x'] and wormBody['y'] == wormCoordinates[HEAD]['y']:
                    return 
                
                #check if worm has written an apple
                if wormCoordinates[HEAD]['x'] == apple['x'] and wormCoordinates[HEAD]['y'] == apple['y']:
                    
                    #don't remove worm's tail segment
                    apple = getRandomLocation()
                else:
                    del wormCoordinates[-1] #remove worm's tail segment
                    
                # move the worm by adding a segment in the direction it is moving
                if direction == UP:
                    newHead = {'x': wormCoordinates[HEAD]['x'], 'y': wormCoordinates[HEAD]['y'] - 1}
                elif direction == DOWN:
                    newHead = {'x': wormCoordinates[HEAD]['x'], 'y': wormCoordinates[HEAD]['y'] + 1}
                elif direction == LEFT:
                    newHead = {'x': wormCoordinates[HEAD]['x'] - 1, 'y': wormCoordinates[HEAD]['y']}
                elif direction == RIGHT:
                    newHead = {'x': wormCoordinates[HEAD]['x'] + 1, 'y': wormCoordinates[HEAD]['y']}
                wormCoordinates.insert(0, newHead)
                
                #drawing the screen
                screen.fill(black)
                drawGrid()
                drawWorm(wormCoordinates)
                drawApple(apple)
                drawScore(len(wormCoordinates) - 3)
                pygame.display.update()
                FPSCLOCK.tick(FPS)
  
#drawing a "press a key" text to the screen  
def drawPressKeyMsg():
    pressKeySurf = font.render("Press a key to play", True, darkgray)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOW_WIDTH - 200, WINDOW_HEIGHT - 30)
    screen.blit(pressKeySurf, pressKeyRect)
    
    
#check for press key function
def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()
    
    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key
        
        
#the start screen
def showStartScreen():
    titleFont = pygame.font.Font("freesansbold.ttf", 100)
    titleSurf1 = titleFont.render("Wormy!", True, white, darkgreen)
    titleSurf2 = titleFont.render("Wormy!", True, green)
    
    degrees1 = 0
    degrees2 = 0
    running = True
    while running:
        
        screen.fill(black)
        
        #rotating the start screen text
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        screen.blit(rotatedSurf1, rotatedRect1)
        
        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        screen.blit(rotatedSurf2, rotatedRect2)
        
        drawPressKeyMsg()
        
        if checkForKeyPress():
            pygame.event.get()
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        
        degrees1 += 3 #rotate by 3 degrees each frame
        degrees2 += 7 #roate by 7 degrees each frame
        
def terminate():
    pygame.quit()
    sys.exit()
    

#deciding where the apple appears
def getRandomLocation():
    return {'x': random.randint(0, CELL_WIDTH - 1), 'y': random.randint(0, CELL_HEIGHT - 1)}
    
    
#GAME OVER SCREENS
def showGameOverScreen():
    gameoverfont = pygame.font.Font("freesansbold.ttf", 150)
    gameSurf = gameoverfont.render("Game", True, white)
    overSurf = gameoverfont.render("Over!", True, white)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOW_WIDTH / 2, 10)
    overRect.midtop = (WINDOW_WIDTH / 2, gameRect.height + 10 + 25)
    
    screen.blit(gameSurf, gameRect)
    screen.blit(overSurf, overRect)
    drawPressKeyMsg()
    pygame.display.update()
    
    pygame.time.wait(500) #delay for 500 milliseconds
    checkForKeyPress() #to clear out any key presses in the event queue
    
    running = True
    while running:
        if checkForKeyPress():
            pygame.event.get() #clear event queue
            return
            
#drawing functions
def drawScore(score):
    scoreSurf = font.render("Score: %s" % (score), True, white)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOW_WIDTH - 120, 10)
    screen.blit(scoreSurf, scoreRect)
    
def drawWorm(wormCoordinates):
    for coord in wormCoordinates:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(screen, darkgreen, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(screen, green, wormInnerSegmentRect)
        
def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(screen, red, appleRect)
    
def drawGrid():
    for x in range(0, WINDOW_WIDTH, CELLSIZE): #DRAW VERTICAL LINES
        pygame.draw.line(screen, darkgray, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELLSIZE): #DRAW HORIZONTAL LINES
        pygame.draw.line(screen, darkgray, (0, y), (WINDOW_WIDTH, y))
        
if __name__ == "__main__":
    main()
    