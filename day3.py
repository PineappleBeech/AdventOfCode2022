import util

alphabet = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    split = util.get_input(3).splitlines()
    parts = [(set(i[:len(i)//2]), set(i[len(i)//2:])) for i in split]
    intersections = [i[0] & i[1] for i in parts]
    count = sum(alphabet.find(i.pop()) for i in intersections)
    print(count)

def main2():
    split = util.get_input(3).splitlines()
    grouped = [[set(split[i]), set(split[i+1]), set(split[i+2])] for i in range(0, len(split), 3)]
    intersections = [i[0] & i[1] & i[2] for i in grouped]
    count = sum(alphabet.find(i.pop()) for i in intersections)
    print(count)

if __name__ == "__main__":
    main()
    main2()