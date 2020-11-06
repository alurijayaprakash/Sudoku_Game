from cmu_112_graphics import *
from helpersudoku import *
from sample import *
import random

def appStarted(app):
    app.rows = 9
    app.cols = 9
    app.userInput = 0
    app.margin = 5 # margin around grid
    app.timerDelay = 100
    initSudokuBoard(app)
    app.waitingForFirstKeyPress = True
    app.waitingForKeyPress = False

def initSudokuBoard(app):
    myfreshlist = []
    app.selectedCell = [(0, 0)]
    app.direction = (0, +1) # (drow, dcol)
    app.sudokuBoard = generateNewBoard()
    print(app.sudokuBoard)
    for i in range(1):
        n = randint(0,8)
        m = randint(0,8)
        app.sudokuBoard[m][n] = 0
    #     print(n,m)
    #     myfreshlist[n][m] = 0
    # print("New List with random 0's ", myfreshlist)
    
    app.gameOver = False
# getCellBounds from grid-demo.py
def getCellBounds(app, row, col):
    # aka 'modelToView'
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = app.width - 2*app.margin
    gridHeight = app.height - 2*app.margin
    x0 = app.margin + gridWidth * col / app.cols
    x1 = app.margin + gridWidth * (col+1) / app.cols
    y0 = app.margin + gridHeight * row / app.rows
    y1 = app.margin + gridHeight * (row+1) / app.rows
    return (x0, y0, x1, y1)
def keyPressed(app, event):
    if (app.waitingForFirstKeyPress):
        app.waitingForFirstKeyPress = False
    elif (event.key == 'r'):
        initSudokuBoard(app)
    elif app.gameOver:
        return
    elif (event.key == 'Up'):
        app.direction = (-1, 0)
        app.waitingForKeyPress = True
    elif (event.key == 'Down'):
        app.direction = (+1, 0)
        app.waitingForKeyPress = True
    elif (event.key == 'Left'):
        app.direction = (0, -1)
        app.waitingForKeyPress = True
    elif (event.key == 'Right'):
        app.direction = (0, +1)
        app.waitingForKeyPress = True
    elif event.key >= '1' and event.key <= '9':
        app.userInput = int(event.key)
        row, col = app.selectedCell[0]
        app.sudokuBoard[row][col] = app.userInput
        # print(app.sudokuBoard)
        flag = isLegalSudoku(app.sudokuBoard)
        if not flag:
            app.sudokuBoard[row][col] = 0
        elif isGameOver(app):
            app.gameOver = True

def isGameOver(app):
    for row in range(app.rows):
        if 0 in app.sudokuBoard[row]:
            return False
    return True

def drawGameOver(app, canvas):
    if (app.gameOver):
        canvas.create_rectangle(  0,   0, 400, 400, fill="cyan", stipple = "gray25") 
        canvas.create_text(app.width/2, app.height/2, text='Game over!', fill='red', 
                           font='Arial 26')
        canvas.create_text(app.width/2, app.height/2+40,
                           text='Press r to restart!', fill='red',
                           font='Arial 26')
def takeStep(app):
    (drow, dcol) = app.direction
    (headRow, headCol) = app.selectedCell.pop()
    (newRow, newCol) = (headRow+drow, headCol+dcol)
    if (newRow < 0):
        newRow = app.rows - 1
    if (newCol < 0):
        newCol = app.cols - 1
    if (newRow >= app.rows):
        newRow = 0
    if (newCol >= app.cols):
        newCol = 0
    app.selectedCell.insert(0, (newRow, newCol))
    app.waitingForKeyPress = False

def timerFired(app):
    if app.gameOver or app.waitingForFirstKeyPress: return
    if app.waitingForKeyPress == True:
        takeStep(app)
    else:
        return

def drawBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            if row % 9 < 3 and col % 9 < 3:
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, fill='gray')
            elif row % 9 < 3 and col % 9 < 6:
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, fill='white')
            elif row % 9 < 3 and col % 9 < 9:
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, fill='gray')
            elif row % 9 < 6 and col % 9 < 3:
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, fill='white')
            elif row % 9 < 6 and col % 9 < 6:
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, fill='gray')
            elif row % 9 < 6 and col % 9 < 9:
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, fill='white')
            elif row % 9 < 9 and col % 9 < 3:
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, fill='gray')
            elif row % 9 < 9 and col % 9 < 6:
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, fill='white')
            elif row % 9 < 9 and col % 9 < 9:
                (x0, y0, x1, y1) = getCellBounds(app, row, col)
                canvas.create_rectangle(x0, y0, x1, y1, fill='gray')
            

def drawSudokuBoard(app, canvas):
    for row in range(app.rows):
        for col in range(app.cols):
            (x0, y0, x1, y1) = getCellBounds(app, row, col)
            (headRow, headCol) = app.selectedCell[0]
            if app.sudokuBoard[row][col] != 0:
                canvas.create_text(int(x0) + 25, int(y0) + 25, text=app.sudokuBoard[row][col], font=f'Arial {20}')

def drawSelectedCell(app, canvas):
    row, col = app.selectedCell[0]
    x0, y0, x1, y1 = getCellBounds(app, row, col)
    canvas.create_rectangle(x0, y0, x1, y1, fill='green')


def redrawAll(app, canvas):
    if (app.waitingForFirstKeyPress):
        canvas.create_text(app.width/2, app.height/2,
                           text='Press any key to start!',
                           font='Arial 26 bold')
    else:
        drawBoard(app, canvas)
        drawSelectedCell(app, canvas)
        drawSudokuBoard(app, canvas)
        drawGameOver(app, canvas)
runApp(width=400, height=400)