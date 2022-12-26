import util

def main():
    lines = util.get_input(10).splitlines()
    x = 1
    values = [1]
    for line in lines:
        if line == "noop":
            values.append(x)
        else:
            values.append(x)
            values.append(x)
            x += int(line.split(" ")[1])

    print(values[20] * 20 + values[60] * 60 + values[100] * 100 + values[140] * 140 + values[180] * 180 + values[220] * 220)

def main2():
    lines = util.get_input(10).splitlines()
    x = 1
    values = []
    for line in lines:
        if line == "noop":
            values.append(x)
        else:
            values.append(x)
            values.append(x)
            x += int(line.split(" ")[1])

    for y in range(6):
        for x in range(40):
            val = values[y*40+x]
            if abs(val - x) < 2:
                print("#", end="")
            else:
                print(".", end="")

        print()



if __name__ == "__main__":
    main()
    main2()