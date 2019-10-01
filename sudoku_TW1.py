import sys
import os
import copy
import time
import ghostlist
import gamedraw

def menu():
    with open("picture.txt", "r") as menu_picture:
        print(f"\u001b[1m{menu_picture.read()}\u001b[0m")
        try:
            menu_coice = input("Choose your option: ")
            if menu_coice.lower() == "s":
                pass
            elif menu_coice.lower() == "q":
                clear()
                with open("exit_picture.txt", "r") as exit_picture:
                    print(f"\u001b[1m{exit_picture.read()}\u001b[0m")
                    sys.exit()
            else:
                raise TypeError
        except TypeError:
            print("Invalid option!")
            return menu()

def loading():
    print("Creating sudoku...")
    for i in range(0, 100):
        time.sleep(0.03)
        sys.stdout.write(u"\u001b[1000D" + str(i + 1) + "%")
        sys.stdout.flush()

def board_nums():
    
    ghost_list = ghostlist.createRandomTable(5)
    nums = copy.deepcopy(ghost_list)
    return nums, ghost_list

def locate_num(nums, ghost_list):
    try:
        x_range = int(input("\nEnter a line number: "))
        if x_range > len(nums) or x_range < 1:
            raise ValueError
        y_range = int(input("Enter a collumn number: "))
        if y_range > len(nums) or y_range < 1:
            raise ValueError
        if isinstance(ghost_list[x_range - 1][y_range - 1], int):
            raise TypeError
    except ValueError:
        print("Your number must be between 0-10!")
        return locate_num(nums, ghost_list)
    except TypeError:
        print("The number in this block cannot be changed!")
        return locate_num(nums, ghost_list)
    return x_range, y_range

def append_or_delete(x_range, y_range, nums):
    try:
        if nums[x_range - 1][y_range - 1] == " ":
            your_num = int(input("Enter a number: "))
            nums[x_range - 1][y_range - 1] = your_num
        elif nums[x_range - 1][y_range - 1] != " ":
            nums[x_range - 1][y_range - 1] = " "
        else:
            raise ValueError
    except ValueError:
        print("Invalid option!")
        return append_or_delete(x_range, y_range, nums)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_sudoku(nums):
    count = 0
    for i in nums:
        count += i.count(" ")
    if count == 0:
        return True
    else:
        return False

def winCheck(table):
    win = False
    if check_sudoku(table):
        for row in range(9):
            for column in range(9):
                if not ghostlist.isNumberValidInRow(table,row,column,table[row][column], True):
                    win = False
                if not ghostlist.isNumberValidInColumn(table,row,column,table[row][column], True):
                    win = False
                if not ghostlist.isNumberValidInBlock(table,row,column,table[row][column]):
                    win = False
    return win

def main():
    clear()
    menu()
    clear()
    nums, ghost_list = board_nums()
    check_sudoku(nums)
    loading()
    clear()
    gamedraw.drawTable(nums,ghost_list)
    while not winCheck(nums):
        x_range, y_range = locate_num(nums, ghost_list)
        append_or_delete(x_range, y_range, nums)
        clear()
        gamedraw.drawTable(nums,ghost_list)
        check_sudoku(nums)
    sys.exit()

main()
