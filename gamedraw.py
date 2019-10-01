def drawTable(table,ghosttable):
    red = "\u001b[31m"
    black = "\u001b[30m"
    background_white = "\u001b[47m"
    reset_color = "\u001b[0m"
    print ( f"     1   2   3   4   5   6   7   8   9 \n" + reset_color + black+ "   " + background_white + "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗" + reset_color) 
    for row in range(9):
        line = str(row) + "  "+ background_white + black + "║"
        for column in range(9):
            if (table[row][column] == ghosttable[row][column]) and (not table[row][column] == " "):
                if (column + 1)%3 == 0:
                    if column == 8:
                        line = line + red + " " + str(table[row][column]) + " " + black + "" + background_white
                    else:
                        line = line + red + " " + str(table[row][column]) + " " + black + "║" + background_white
                else:
                    line = line + red + " " + str(table[row][column]) + " " + black + "│" + background_white
            else:
                if (column + 1)%3 == 0:
                    if column == 8:
                        line = line + black + " " + str(table[row][column]) + " " + background_white
                    else:
                        line = line + black + " " + str(table[row][column]) + " " + black + "║" + background_white
                else:
                    line = line + black + " " + str(table[row][column]) + " " + black + "│" + background_white

        print(line + "║"+reset_color)
        if (row+1) % 3 == 0:
            if row == 8:
                print ( reset_color + black + "   " + background_white + "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝" + reset_color)            
            else:
                print ( reset_color + black + "   " + background_white + "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣" + reset_color)
        else:
            print ( reset_color + black + "   " + background_white + "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢" + reset_color)


