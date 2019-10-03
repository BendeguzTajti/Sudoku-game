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
            elif menu_coice.lower() == "b":
                clear()
                return menu()
            else:
                raise TypeError
        except TypeError:
            print("Invalid option!")
            time.sleep(1)
            clear()
            return menu()


def choose_difficulty():
    bold = "\u001b[1m"
    reset = "\u001b[0m"
    try:
        with open("choose_difficulty.txt", "r") as choose_diff:
            print(f"{bold}{choose_diff.read()}{reset}")
        difficulty = input("Choose a difficulty: ")
        if difficulty == "1":
            return 38
        elif difficulty == "2":
            return 30
        elif difficulty == "3":
            return 25
        elif difficulty == "4":
            clear()
            return choose_difficulty()
        else:
            raise ValueError
    except ValueError:
        print("Invalid number!")
        time.sleep(1)
        clear()
        return choose_difficulty()


def loading():
    os.system("setterm -cursor off")
    red_background = "\u001b[41m"
    bold = "\u001b[1m"
    reset = "\u001b[0m"
    with open("coke_ad.txt", "r") as ad:
        print(f"\n\n{red_background}{bold}{ad.read()}{reset}")
    print(f"{bold}* Buy the full game to remove ads\n\n\n{reset}")
    print(f"{bold}Creating sudoku...{reset}".center(80))
    bar_lenght = 0
    fill = ""
    print("\r")
    percent = 0
    for bar_lenght in range(0, 26):
        width = 25 - len(fill)
        width = " " * width
        bar = (f"{bold}|{fill + width}| ").center(75)
        fill += "█"
        percent += 4
        time.sleep(0.3)
        bar_lenght += 1
        sys.stdout.write(u"\u001b[1000D" + bar.center(75))
        sys.stdout.flush()
    time.sleep(0.5)
    os.system("setterm -cursor on")


def board_nums(num):
    ghost_list = ghostlist.createRandomTable(num)
    nums = copy.deepcopy(ghost_list)
    return nums, ghost_list


def locate_num(nums, ghost_list):
    try:
        x = int(input("\nEnter a line number( exit = 0 ): "))
        if x == 0:
            sys.exit()
        elif x > len(nums) or x < 1:
            raise ValueError
        y = int(input("Enter a collumn number: "))
        if y > len(nums) or y < 1:
            raise ValueError
        if isinstance(ghost_list[x - 1][y - 1], int):
            raise TypeError
    except ValueError:
        print("Your number must be between 0-10!")
        return locate_num(nums, ghost_list)
    except TypeError:
        print("The number in this block cannot be changed!")
        return locate_num(nums, ghost_list)
    return x, y


def append_or_delete(x, y, nums):
    try:
        if nums[x - 1][y - 1] == " ":
            your_num = int(input("Enter a number: "))
            nums[x - 1][y - 1] = your_num
        elif nums[x - 1][y - 1] != " ":
            nums[x - 1][y - 1] = " "
        else:
            raise ValueError
    except ValueError:
        print("Invalid option!")
        return append_or_delete(x, y, nums)


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
    fixed_nums = choose_difficulty()
    nums, ghost_list = board_nums(fixed_nums)
    check_sudoku(nums)
    clear()
    loading()
    clear()
    gamedraw.drawTable(nums,ghost_list)
    while not winCheck(nums):
        x, y = locate_num(nums, ghost_list)
        append_or_delete(x, y, nums)
        clear()
        gamedraw.drawTable(nums,ghost_list)
        check_sudoku(nums)
    sys.exit()

main()
