import util

def main():
    text = util.get_input(6)
    for i in range(len(text) - 3):
        s = set(text[i:i+4])
        if len(s) == 4:
            print(i+4)
            break

def main2():
    text = util.get_input(6)
    for i in range(len(text) - 13):
        s = set(text[i:i+14])
        if len(s) == 14:
            print(i+14)
            break

if __name__ == "__main__":
    main()
    main2()
