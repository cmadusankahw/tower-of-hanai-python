from pathlib import Path
import gettext
gettext.install('hanoi', Path(__file__).parent)


def print_rules():
    print("--------- Tower of Hanoi ---------\n")
    print("Rules: ")
    print("  1) Only one disk can be moved at a time.\n  2) Each move consists of taking the upper disk from one of the stacks\n     and placing it on top of another stack\n     i.e. a disk can only be moved if it is the uppermost disk on a stack.\n  3) No disk may be placed on top of a smaller disk.\n")


def move(source, destination):
    destination.append(source.pop())


def possible_move(peg1, peg2):
    if peg1 and (not peg2 or peg1[-1] < peg2[-1]):
        return peg1, peg2
    else:
        return peg2, peg1


def print_pegs(a, b, c, discs):
    # print(a)
    # print(b)
    # print(c)
    print_tower(a, discs+2)
    print_tower(b, discs + 2)
    print_tower(c, discs + 2)
    print()


def print_tower(a, height):
    tower_bar = height - len(a)
    for i in range(tower_bar):
        print("|")
    for j in range(len(a)):
        print("*" * len(a), end=" ")
        print()


def tower_of_hanoi(discs):
    a = list(range(discs, 0, -1))
    b = []
    c = []

    minimum_moves = 2 ** discs - 1

    if discs % 2 == 1:
        peg = [a, c, b]
    else:
        peg = [a, b, c]

    moves = 0
    while len(c) != discs:
        if moves % 2 == 0:
            move(peg[0], peg[1])      # Smallest disc now on peg[1]
        else:
            source, destination = possible_move(peg[0], peg[2])
            move(source, destination)
            peg = peg[1:] + peg[:1]   # Rotate the peg ordering

        print_pegs(a, b, c ,discs)
        moves += 1

    print()
    print(('Moves:'), moves)
    print(('Minimal moves:'), minimum_moves)


if __name__ == '__main__':
    print_rules()
    dif_level = int(input(('Select Difficulty Level:\n 1)High \n 2)Medium \n 3)Easy \n\nLevel : ')))
    print(f"Difficulty level set to: {dif_level}\n")
    discs = int(input(('Enter the number of disks: ')))
    tower_of_hanoi(discs)