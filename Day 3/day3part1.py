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

def getNumberFromCoords(grid, used, row, col):
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
    if not checkNumber(row, col, used):
        used.append(coords)
        return int(numString)
    else:
        return 0

with open("input") as file:
    symbols = []
    numbersUsed = [] #list of list of coordinates
    total = 0
    grid = file.readlines()
    rowCount = len(grid)
    colCount = len(grid[0])
    
    for row in range(rowCount):
        for col in range(colCount):
            if not grid[row][col].isalnum() and grid[row][col] != "." and grid[row][col] != "\n": #found a symbol
                symbols.append((row,col))
                
    for symbolRow, symbolCol in symbols:
        for adjRow, adjCol in adjacentCoords(symbolRow, symbolCol, rowCount, colCount):
            if grid[adjRow][adjCol].isnumeric():
                total += getNumberFromCoords(grid, numbersUsed, adjRow, adjCol)
                 
    print(total)

