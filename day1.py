import util

def main():
    split = util.get_input(1).split("\n\n")

    calories = [sum(map(int, i.removesuffix("\n").split("\n"))) for i in split]

    calories.sort()

    print(calories[-1] + calories[-2] + calories[-3])

def one_line():
    print(sum(sorted([sum(map(int, i.removesuffix("\n").split("\n"))) for i in util.get_input(1).split("\n\n")])[-3:]))

if __name__ == "__main__":
    main()
    one_line()