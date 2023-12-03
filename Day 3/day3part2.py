def adjacentCoords(row, col, maxRow, maxCol):
    """outputs a set of all coordinates adjacent to row and col"""
    out = []
    temp = []
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if i != 0 or j != 0:
                temp.append((row+i, col+j))
    for candRow, candCol in temp:
        if candRow in range(0,maxRow) and candCol in range(0,maxCol):
            out.append((candRow, candCol))
    return out
            
def checkNumber(row, col, numbersUsed):
    """checks if number has already been accounted for"""
    for coordSet in numbersUsed:
        if (row, col) in coordSet:
            return True
    return False

def getNumberFromCoords(grid, row, col, used):
    if checkNumber(row, col, used):
        return -1
    thisRow = grid[row]
    numString = thisRow[col]
    coords = [(row, col)]
    try:
        check = thisRow[col+1]
        offset = 1
        while check.isnumeric():
            numString += check
            coords.append((row, col+offset))
            offset += 1
            check = thisRow[col+offset]
    except:
        pass
    try:
        check = thisRow[col-1]
        offset = -1
        while check.isnumeric():
            numString = check + numString
            coords.append((row, col+offset))
            offset -= 1
            check = thisRow[col+offset]
    except:
        pass
    used.append(coords)
    return int(numString)

def addGear(row, col, maxRow, maxCol, grid):
    coordsUsed = []
    numCount = 0
    product = 1
    for row, col in adjacentCoords(row, col, maxRow, maxCol):
        if grid[row][col].isnumeric():
            value = getNumberFromCoords(grid, row, col, coordsUsed)
            if value > 0:
                numCount += 1
                product *= value
    if numCount == 2:
        return product
    else:
        return 0
        

with open("input") as file:
    gears = []
    asterisks = []
    total = 0
    grid = file.readlines()
    rowCount = len(grid)
    colCount = len(grid[0])
    
    for row in range(rowCount):
        for col in range(colCount):
            if grid[row][col] == "*": #found a symbol
                asterisks.append((row,col))
                
    for symbolRow, symbolCol in asterisks:
        total += addGear(symbolRow, symbolCol, rowCount, colCount, grid)

                
                 
    print(total)

