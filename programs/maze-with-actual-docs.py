#Imports
from graphics import *
from math import *
from random import *
from time import *
from sys import *
#Inputs
columns = int(input("How many columns across? "))
rows = int(input("How many rows up? "))
solved = input("Do you want the maze to be solved? (y/n) ")
#Setup the maze size 
if solved[0].lower() == "y":
    solved = True
else:
    solved = False
if columns > rows:
    scale = 1200/columns
else:
    scale = 700/rows
if columns*rows > 1000:
    #Makes sure code doesn't hit recursion limit (if a function runs itself too many times IDLE will stop the code to prevent crashes), the +50 is just precautionary
    setrecursionlimit((columns*rows)+50)
width = columns*scale
if width > 1500:
    width = 1500
height = rows*scale
if height > 750:
    height = 750
#Create the grid at size 1500px by 750px or less
win = GraphWin("Grid System",width,height, autoflush = False)
#Sets up how the graphics window will be used
win.setCoords(0,0,columns,rows)
#Class for each cell in the grid
class Cell:
    def __init__(self,i,j):
        #Creates each box
        self.box = Rectangle(Point(i,j),Point(i+1,j+1))
        self.box.setFill("black")
        self.box.setWidth(0)
        #Sets box coordinate points
        self.x = i
        self.y = j
        #Names each box after it's coordinate points
        self.name = str(i) + "," + str(j)
        #Draw walls
        northWall = Line(Point(i,j+1),Point(i+1,j+1))
        southWall = Line(Point(i,j),Point(i+1,j))
        eastWall = Line(Point(i+1,j),Point(i+1,j+1))
        westWall = Line(Point(i,j),Point(i,j+1))
        #What walls still exist
        self.n = True
        self.s = True
        self.e = True
        self.w = True
        #What walls still exist, but in a different form
        self.walls = [northWall,southWall,eastWall,westWall]
        #Has the box been visited in the creation or solution of the maze? 
        self.visit = False
        #Does the box exist?
        self.state = False
        #Draw walls
        for w in self.walls:
            w.setWidth(2)
            w.setFill("white")
    #Returns the name of the box
    def __repr__(self):
        return self.name
    #Draws the box
    def draw(self,win,wallCheck):
        self.win = win
        self.box.draw(win)
        self.state = True
        if wallCheck == True:
            for w in self.walls:
                w.draw(win)
    #Removes the given wall
    def demo(self,remove):
        if remove == 0:
            self.n = False
        elif remove == 1:
            self.s = False
        elif remove == 2:
            self.e = False
        elif remove == 3:
            self.w = False
        self.walls[remove].undraw()
    #Removes the box and all walls
    def undraw(self):
            try:
                self.state = False
                self.box.undraw()
            except:
                pass
            try:
                for w in self.walls:
                    w.undraw()
            except:
                pass
    #Toggles the box
    def toggle(self,win,check):
        if self.state:
            self.undraw()
        else:
            self.draw(win,check)
            
#--------------------------------------

grid = []
#Sets up an accessible list that has every cell in the grid
def makeGrid():
    for i in range(columns):
        grid.append([])
        for j in range(rows):
            grid[i].append(Cell(i,j))
            grid[i][j].toggle(win,True)
#Creates the beginning of the maze, with only the starting cell stored in it
def makeMaze():
    global mazeList
    global grid
    grid[0][0].visit = True
    grid[0][0].box.setFill("DeepPink2")
    x = 0
    y = 0
    while True:
        #Allows for visualization to exist and the maze to not instantly generate
        sleep(.0001)
        win.update()
        #Sets the position of the maze creator to the most recent cell added to the list
        x = maze[-1].x
        y = maze[-1].y
        #The following if statements see if the cells around the selected tile have been visited, and if they have it removes them from the choices to visit
        choices = [0,1,2,3]
        #NORTH
        if y == rows-1 or grid[x][y+1].visit == True:
            choices.remove(0)
        #SOUTH
        if y == 0 or grid[x][y-1].visit == True:
            choices.remove(1)
        #EAST
        if x == columns-1 or grid[x+1][y].visit == True:
            choices.remove(2)
        #WEST
        if x == 0 or grid[x-1][y].visit == True:
            choices.remove(3)
        """If the choices list isn't empty, demolish the wall in the randomly chosen direction and begin the process of moving the maze solver to that cell
        while removing 1 of 2 walls that need to be removed"""
        
        """It is necessary to remove two walls because each box has it's own 4 walls, so if the code wanted to move west one tile,
        it would need to remove the west wall of that tile, and the east wall of the tile that was moved into."""
        if choices != []:
            direction = choice(choices)
            grid[x][y].demo(direction)
            if direction == 0:
                #North
                y+=1
                direction = 1
            elif direction == 1:
                #South
                y-=1
                direction = 0
            elif direction == 2:
                #East
                x+=1
                direction = 3
            else:
                #West
                x-=1
                direction = 2
            #Completes moving the maze solver to the next tile over, while also demolishing the second wall
            grid[x][y].box.setFill("DeepPink2")
            grid[x][y].demo(direction)
            grid[x][y].visit = True
            maze.append(grid[x][y])
        else:
            #Coloring
            maze[-1].box.setFill("black")
            maze.pop(-1)
        if maze == []:
            #If there are no more tiles that have not been visited, color the starting tile green
            grid[0][0].box.setFill("green")
            break
paths = []
#Finds and creates both solutions
def makeEnd(x,y,direction,path):
    global grid
    global paths
    if len(direction) > 1:
        """This code makes use of recursion, which is where the program runs itself until there is only one possible thing to do.
        In this instance, makeEnd() may have multiple directions to check, and will save each direction as it's own instance of makeEnd(),
        running each of them one at a time (possibly creating even more makeEnd() instances) until all directions have been checked."""
        makeEnd(x,y,direction[1:len(direction)].copy(),path.copy())
    while True:
        sleep(.0001)
        win.update()
        if direction[0] == 0:
            y+=1
        elif direction[0] == 1:
            y-=1
        elif direction[0] == 2:
            x+=1
        elif direction[0] == 3:
            x-=1
        #Storing the path that this instance of makeEnd() is generating
        path.append(grid[x][y])
        #Makes sure that the current tile has been set to being visited
        grid[x][y].visit = True
        grid[x][y].box.setFill("SkyBlue2")
        choices = [0,1,2,3]
        #This set of if statements makes sure the maze solver does not try to index a tile that does not exist, or visit a tile that has already been visited
        #NORTH
        if y >= rows-1 or grid[x][y+1].visit == True or path[-1].n == True:
            choices.remove(0)
        #SOUTH
        if y == 0 or grid[x][y-1].visit == True or path[-1].s == True:
            choices.remove(1)
        #EAST
        if x >= columns-1 or grid[x+1][y].visit == True or path[-1].e == True:
            choices.remove(2)
        #WEST
        if x == 0 or grid[x-1][y].visit == True or path[-1].w == True:
            choices.remove(3)
        if len(choices) > 0:
            #If there is at least one tile to go to, run this function again
            makeEnd(x,y,choices,path)
            return
        else:
            #If there are no tiles to go to on this path, add this path to the list of paths for later size checking then run the function again
            paths.append(path)
            return
#When there are no instances to recurse and no paths to check, the previous function will end and the maze will now be solved
def solution():
    #Gets the variable for checking if the maze should be solved
    global solved
    #Makes all of the grid tiles unvisited
    for i in range(columns):
        for j in range(rows):
            grid[i][j].visit = False
    #Now that the tiles are no longer visited, the visit variable can be reused for finding the solution
    makeEnd(0,0,[None],[])
    #Setup for drawing lines from start to ends
    newLst = []
    maxLen = 0
    maxPath = None
    minLen = rows*columns
    minPath = None
    #Goes through the list of paths, finding the largest and smallest
    for i in paths:
        if len(i) > maxLen:
            maxPath = i
            maxLen = len(maxPath)
        if len(i) < minLen:
            minPath = i
            minLen = len(minPath)
    #Makes sure all tiles are black, then sets the start and both ends to their respective colors
    for i in range(columns):
        for j in range(rows):
            grid[i][j].box.setFill("black")
    grid[0][0].box.setFill("green")
    maxPath[-1].box.setFill("red")
    minPath[-1].box.setFill("blue")
    #Setup for making the lines
    lineList = []
    lineList2 = []
    #If you did not want the maze to be solved, you can click three times to get the solution if you end up deciding you want to see the solution
    if not solved:
        print("Click three times to get solution")
        win.getMouse()
        win.getMouse()
        win.getMouse()
        solved = True
    #If the player wants the maze to be solved, draw the lines to the solution
    if solved == True:
        for n,i in enumerate(maxPath):
            #Allows for visualization of path appearing
            sleep(.0001)
            #If the code has not reached the end of the path, begin drawing the next line segment to the solution
            if i != maxPath[-1]:
                win.update()
                #Sets the starting x,y and ending x,y of the next line segment. It will be placed at the center of the box, with the length being exactly that of the box
                x1 = i.x + .5
                y1 = i.y + .5
                x2 = maxPath[n+1].x + .5
                y2 = maxPath[n+1].y + .5
                #Creates the line segment
                newLine = Line(Point(x1,y1),Point(x2,y2))
                #Sets line width to be 1/4 of the box size, so it never look too big
                newLine.setWidth(scale/4)
                #Draws and colors the line, and adds the line to the list containing every line segment
                newLine.setFill("green")
                newLine.draw(win)
                lineList.append(newLine)
        for n,i in enumerate(minPath):
            #Allows for visualization of path appearing
            sleep(.0001)
            #If the code has not reached the end of the path, begin drawing the next line segment to the near solution
            if i != minPath[-1]:
                win.update()
                #Sets the starting x,y and ending x,y of the next line segment. It will be placed at the center of the box, with the length being exactly that of the box
                x1 = i.x + .5
                y1 = i.y + .5
                x2 = minPath[n+1].x + .5
                y2 = minPath[n+1].y + .5
                #Creates the line
                newLine = Line(Point(x1,y1),Point(x2,y2))
                #Sets line width to be 1/4 of the box size, so it never look too big
                newLine.setWidth(scale/4)
                #Draws and colors the line, and adds the line to the list containing every line segment
                newLine.setFill("red")
                newLine.draw(win)
                lineList2.append(newLine)
        #For some reason some line segments would not be colored, so this is a failsafe to make sure they are all the correct color
        for i in lineList:
            i.setFill("green")
        for i in lineList2:
            i.setFill("red")

#Runs each function (with the exception of mazeEnd(), which needs to be run inside of the solution() function), and also sets up the maze after the grid is created
makeGrid()
maze = [grid[0][0]]
makeMaze()
solution()

