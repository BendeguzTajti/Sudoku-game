import random

def createRandomTable(num):
    table = []
    for i in range(0,9):
        subTable = []
        for j in range(0,9):
            subTable.append(" ")
        table.append(subTable)
    
    filledTable = fillTable(table, num)
    return filledTable

def fillTable ( table, num):
    for i in range ( 0, num):
        integer = random.randint(1,9)
        row = random.randint(0,8)
        column = random.randint(0,8)
        while not(isNumberValidInColumn(table,row,column,integer) and isNumberValidInRow(table,row,column,integer) and isNumberValidInBlock(table,row,column,integer)):
            integer = random.randint(1,9)
            row = random.randint(0,8)
            column = random.randint(0,8)            
        table[row][column] = integer
    return table

def isNumberValidInColumn(table,row,column,number):
    valid = True
    for r in table:
        if not r == row:
            r[column] = str(r[column])
            if not r[column] == " ":
                if int(r[column]) == number:
                    valid = False
        else:
            if str.isnumeric(r[column]):
                valid = False
    return valid

def isNumberValidInRow(table,row,column,number):
    valid = True
    for num in table[row]:
        if not num == " ":
            if int(num) == number:
                valid = False
            if num == column:
                valid = False
    return valid

def isNumberValidInBlock(table,row,column,number):
    allIndex = getAllIndexOfBlock(row,column)
    valid = True
    for index in allIndex:
        num = table[index[0]][index[1]]
        if not str(num) == " ":
            if int(num) == number:
                valid = False
    return valid

def getAllIndexOfBlock(row,column):
    #[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2] 
    allIndex = []
    row_dif = (row)%3
    col_dif = (column)%3
    #print ( "START : " + (str(row+1)) + "%3 =" + str(row_dif) + "  -> STARTING: (3-(" + str(row_dif) + " -1)) ")
    startingrow = row - row_dif
    startingcol = column - col_dif  
    for i in range(3):
        subTable = []
        for j in range(3):
            indexTable = []
            indexTable.append(startingrow + i)
            indexTable.append(startingcol + j)
            allIndex.append(indexTable)
        #allIndex.append(subTable)      
    return allIndex






