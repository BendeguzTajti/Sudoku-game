import sys
import os
import copy
import time
def menu():
    with open ("picture.txt", "r") as menu_picture:
        print(f"\u001b[1m{menu_picture.read()}\u001b[0m")
        try:
            menu_coice = input("Choose your option: ")
            if menu_coice.lower() == "s":
                pass
            elif menu_coice.lower() == "q":
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
    ghost_list = [
        [9," ",7," "," ",2," ",5," "],
        [5," "," "," ",9,8,7,1,2],
        [" ",2," ",7," "," "," ",9,3],
        [" ",6,8," ",7," "," "," "," "],
        [" "," "," ",8," ",3," "," "," "],
        [" "," "," "," ",4," ",2,6," "],
        [8,1," "," "," ",7," ",3," "],
        [6,9,2,5,3," "," "," ",7],
        [" ",7," ",1," "," ",6," ",4]
    ]
    nums = copy.deepcopy(ghost_list)
    return nums,ghost_list
def board_creation(nums):
    red = "\u001b[31m"
    black = "\u001b[30m"
    background_white = "\u001b[47m"
    reset_color = "\u001b[0m"

    line_0 = (f"    1   2   3   4   5   6   7   8   9\n  {background_white}{black}╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗{reset_color}\n{'1'}{black} {background_white}║ {red}{nums[0][0]}{black} │ {nums[0][1]} │ {red}{nums[0][2]}{black} ║ {nums[0][3]} │ {nums[0][4]} │ {red}{nums[0][5]}{black} ║ {nums[0][6]} │ {red}{nums[0][7]}{black} │ {nums[0][8]} ║{reset_color}\n")
    line_1 = (f"{black}  {background_white}╟───┼───┼───╫───┼───┼───╫───┼───┼───╢{reset_color}\n{'2'}{black} {background_white}║ {red}{nums[1][0]}{black} │ {nums[1][1]} │ {nums[1][2]} ║ {nums[1][3]} │ {red}{nums[1][4]}{black} │ {red}{nums[1][5]}{black} ║ {red}{nums[1][6]}{black} │ {red}{nums[1][7]}{black} │ {red}{nums[1][8]}{black} ║{reset_color}\n")
    line_2 = (f"{black}  {background_white}╟───┼───┼───╫───┼───┼───╫───┼───┼───╢{reset_color}\n{'3'}{black} {background_white}║ {nums[2][0]} │ {red}{nums[2][1]}{black} │ {nums[2][2]} ║ {red}{nums[2][3]}{black} │ {nums[2][4]} │ {nums[2][5]} ║ {nums[2][6]} │ {red}{nums[2][7]}{black} │ {red}{nums[2][8]}{black} ║{reset_color}\n")
    line_3 = (f"{black}  {background_white}╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣{reset_color}\n{'4'}{black} {background_white}║ {nums[3][0]} │ {red}{nums[3][1]}{black} │ {red}{nums[3][2]}{black} ║ {nums[3][3]} │ {red}{nums[3][4]}{black} │ {nums[3][5]} ║ {nums[3][6]} │ {nums[3][7]} │ {nums[3][8]} ║{reset_color}\n")
    line_4 = (f"{black}  {background_white}╟───┼───┼───╫───┼───┼───╫───┼───┼───╢{reset_color}\n{'5'}{black} {background_white}║ {nums[4][0]} │ {nums[4][1]} │ {nums[4][2]} ║ {red}{nums[4][3]}{black} │ {nums[4][4]} │ {red}{nums[4][5]}{black} ║ {nums[4][6]} │ {nums[4][7]} │ {nums[4][8]} ║{reset_color}\n")
    line_5 = (f"{black}  {background_white}╟───┼───┼───╫───┼───┼───╫───┼───┼───╢{reset_color}\n{'6'}{black} {background_white}║ {nums[5][0]} │ {nums[5][1]} │ {nums[5][2]} ║ {nums[5][3]} │ {red}{nums[5][4]}{black} │ {nums[5][5]} ║ {red}{nums[5][6]}{black} │ {red}{nums[5][7]}{black} │ {nums[5][8]} ║{reset_color}\n")
    line_6 = (f"{black}  {background_white}╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣{reset_color}\n{'7'}{black} {background_white}║ {red}{nums[6][0]}{black} │ {red}{nums[6][1]}{black} │ {nums[6][2]} ║ {nums[6][3]} │ {nums[6][4]} │ {red}{nums[6][5]}{black} ║ {nums[6][6]} │ {red}{nums[6][7]}{black} │ {nums[6][8]} ║{reset_color}\n")
    line_7 = (f"{black}  {background_white}╟───┼───┼───╫───┼───┼───╫───┼───┼───╢{reset_color}\n{'8'}{black} {background_white}║ {red}{nums[7][0]}{black} │ {red}{nums[7][1]}{black} │ {red}{nums[7][2]}{black} ║ {red}{nums[7][3]}{black} │ {red}{nums[7][4]}{black} │ {nums[7][5]} ║ {nums[7][6]} │ {nums[7][7]} │ {red}{nums[7][8]}{black} ║{reset_color}\n")
    line_8 = (f"{black}  {background_white}╟───┼───┼───╫───┼───┼───╫───┼───┼───╢{reset_color}\n{'9'}{black} {background_white}║ {nums[8][0]} │ {red}{nums[8][1]}{black} │ {nums[8][2]} ║ {red}{nums[8][3]}{black} │ {nums[8][4]} │ {nums[8][5]} ║ {red}{nums[8][6]}{black} │ {nums[8][7]} │ {red}{nums[8][8]}{black} ║{reset_color}\n  {black}{background_white}╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝{reset_color}")
    lines = (line_0+line_1+line_2+line_3+line_4+line_5+line_6+line_7+line_8)
    print(lines)

def locate_num(nums,ghost_list):
    try:
        x_range = int(input("\nEnter a line number: "))
        if x_range > len(nums) or x_range < 1:
            raise ValueError
        y_range = int(input("Enter a collumn number: "))
        if y_range > len(nums) or y_range < 1:
            raise ValueError
        if type(ghost_list[x_range-1][y_range-1]) == int:
            raise TypeError
    except ValueError:
        print("Your number must be between 0-10!")
        return locate_num(nums,ghost_list)
    except TypeError:
        print("The number in this block cannot be changed!")
        return locate_num(nums,ghost_list)
    return x_range,y_range

def append_or_delete(x_range,y_range,nums):
    print(f"\n(a) Append\n(d) Delete\n")
    choice = input(f"Choose an option: ")
    try:
        if choice.lower() == "a":
            your_num = int(input("Enter a number: "))
            nums[x_range-1][y_range-1] = your_num
        elif choice.lower() == "d":
            nums[x_range-1][y_range-1] = " "
        else:
            raise ValueError
    except ValueError:
        print("Invalid option!")
        return append_or_delete(x_range,y_range,nums)

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

def main():
    clear()
    menu()
    clear()
    nums,ghost_list = board_nums()
    check_sudoku(nums)
    loading()
    clear()
    board_creation(nums)
    while check_sudoku(nums) == False:
        x_range,y_range = locate_num(nums,ghost_list)
        append_or_delete(x_range,y_range,nums)
        clear()
        board_creation(nums)
        check_sudoku(nums)
    sys.exit()
main()