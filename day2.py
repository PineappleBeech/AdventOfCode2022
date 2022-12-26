import util

rock = [("A", "Y"), ("B", "X"), ("C", "Z")]
paper = [("A", "Z"), ("B", "Y"), ("C", "X")]
scissors = [("A", "X"), ("B", "Z"), ("C", "Y")]

def main():
    lines = util.get_input(2).splitlines()
    games = (line.split(" ") for line in lines)
    score = 0
    for game in games:
        if game[1] == "X":
            score += 0
        elif game[1] == "Y":
            score += 3
        elif game[1] == "Z":
            score += 6

        g = tuple(game)

        if g in rock:
            score += 1
        elif g in paper:
            score += 2
        elif g in scissors:
            score += 3
    print(score)



if __name__ == "__main__":
    main()