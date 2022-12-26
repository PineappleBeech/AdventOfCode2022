import util

def main():
    text = util.get_input(5)
    piles, moves = text.split("\n\n")
    moves = moves.splitlines()
    piles = piles.splitlines()
    pile_height = len(piles) - 1
    pile_count = 9
    pile_array = [[] for i in range(pile_count)]
    for i in range(len(pile_array)):
        for h in range(pile_height):
            if piles[pile_height - h - 1][i*4+1] == " ":
                break
            else:
                pile_array[i].append(piles[pile_height - h - 1][i*4+1])
    for move in moves:
        words = move.split(" ")
        count = int(words[1])
        start = int(words[3])
        end = int(words[5])
        for i in range(count):
            pile_array[end-1].append(pile_array[start-1].pop())
    for i in range(len(pile_array)):
        print(pile_array[i][-1], end="")
    print()


def main2():
    text = util.get_input(5)
    piles, moves = text.split("\n\n")
    moves = moves.splitlines()
    piles = piles.splitlines()
    pile_height = len(piles) - 1
    pile_count = 9
    pile_array = [[] for i in range(pile_count)]
    for i in range(len(pile_array)):
        for h in range(pile_height):
            if piles[pile_height - h - 1][i*4+1] == " ":
                break
            else:
                pile_array[i].append(piles[pile_height - h - 1][i*4+1])
    for move in moves:
        words = move.split(" ")
        count = int(words[1])
        start = int(words[3]) - 1
        end = int(words[5]) - 1
        temp = pile_array[start][-count:]
        pile_array[start] = pile_array[start][:-count]
        pile_array[end] = pile_array[end] + temp

    for i in range(len(pile_array)):
        print(pile_array[i][-1], end="")
    print()


if __name__ == "__main__":
    main()
    main2()
