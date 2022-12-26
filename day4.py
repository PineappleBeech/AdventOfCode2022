import util

def main():
    lines = util.get_input(4).splitlines()
    pairs = [line.split(",") for line in lines]
    total = 0
    for pair in pairs:
        start1, end1 = pair[0].split("-")
        start2, end2 = pair[1].split("-")
        if int(start1) >= int(start2) and int(end1) <= int(end2):
            total += 1
            continue
        if int(start2) >= int(start1) and int(end2) <= int(end1):
            total += 1
            continue

    print(total)

def main2():
    lines = util.get_input(4).splitlines()
    pairs = [line.split(",") for line in lines]
    total = 0
    for pair in pairs:
        start1, end1 = pair[0].split("-")
        start2, end2 = pair[1].split("-")
        if int(start1) <= int(end1) < int(start2) <= int(end2):
            continue
        elif int(start2) <= int(end2) < int(start1) <= int(end1):
            continue
        else:
            total += 1

    print(total)


if __name__ == "__main__":
    main()
    main2()