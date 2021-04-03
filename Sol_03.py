objects = ["|", "~", "~~~", "~~~~~"]


def print_rules():
    print("--------- Tower of Hanoi ---------\n")
    print("Rules: ")
    print(
        "  1) Only one disk can be moved at a time.\n  2) Each move consists of taking the upper disk from one of the stacks\n     and placing it on top of another stack\n     i.e. a disk can only be moved if it is the uppermost disk on a stack.\n  3) No disk may be placed on top of a smaller disk.\n")


def new_game():
    global twr
    global total_moves
    total_moves = -1
    twr = [[3, 2, 1], [], []]
    print_towers()


def print_towers():
    global total_moves
    total_moves += 1
    line = ""
    print("~" * 7 * 3)

    for row in range(2, -1, -1):
        for column in range(3):
            try:
                line += objects[twr[column][row]].center(7)
            except IndexError:
                line += objects[0].center(7)
        print(line)
        line = ""


def fast_forward(no_of_times):
    pass

def step_backward(move):
    move_discs(move)

def move_discs(move):
    try:
        if len(twr[move[0]]):
            if len(twr[move[1]]):
                if twr[move[0]][-1] < twr[move[1]][-1]:
                    twr[move[1]].append(twr[move[0]][-1])
                    twr[move[0]].pop()
                    print_towers()
                else:
                    print("It can't be moved!")
            else:
                twr[move[1]].append(twr[move[0]][-1])
                twr[move[0]].pop()
                print_towers()
        else:
            print("nothing to move!")
    except:
        print("please give a disc to move!")


def play_game():
    global move
    move = [1, 1]
    while True:
        query = input("1)Continue to next move?  2)Step backward? or 3)Fast forward? :")
        if query == "1":
            msg = input("Which disc to move, and where? [Disc No tower No] ")
            move = [int(i) - 1 for i in msg.split()]

            move_discs(move)

            # Game Over logic
            if (len(twr[2])) == 3 or (len(twr[1]) == 3):
                print("Congratulations! You Won!")
                print("Total moves made: ", total_moves)
                break
        elif query == "2":
            reversed_moves = [ele for ele in reversed(move)]
            print("backwarding one move...")
            step_backward(reversed_moves)
        elif query == "3":
            # fast forward code
            pass
        else:
            print("Incorrect choice! Please enter 1,2 or 3 as your choice!")


if __name__ == '__main__':
    print_rules()
    dif_level = int(input(('Select Difficulty Level:\n 1)High \n 2)Medium \n 3)Easy \n\nLevel : ')))
    print(f"Difficulty level set to: {dif_level}\n")
    new_game()
    play_game()
