import util

def main():
    lines = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122""".splitlines()
    lines = util.get_input(25).splitlines()
    total = 0
    for line in lines:
        total += from_s(line)
    print(to_s(total))

def to_s(x):
    num = ""
    while x != 0:
        x += 2
        if x % 5 == 0:
            num = "=" + num
        elif x % 5 == 1:
            num = "-" + num
        elif x % 5 == 2:
            num = "0" + num
        elif x % 5 == 3:
            num = "1" + num
        elif x % 5 == 4:
            num = "2" + num

        x //= 5

    return num

def from_s(num):
    x = 0
    for i, c in enumerate(num):
        x *= 5
        if c == "=":
            x -= 2
        elif c == "-":
            x -= 1
        elif c == "0":
            pass
        elif c == "1":
            x += 1
        elif c == "2":
            x += 2
    return x

if __name__ == "__main__":
    main()