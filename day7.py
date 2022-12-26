import util
import io

total = 0

def main():
    global total

    text = io.StringIO('''\
$ cd /
$ ls
dir x
$ cd x
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
dir l
$ cd l
$ ls
dir m
$ cd m
$ ls
100 trr
''')
    text = io.StringIO(util.get_input(7))
    files = {}
    folders = []
    cd = ""
    while (line := text.readline().strip()) != "":
        args = line.split(" ")
        assert args[0] == "$"
        if args[1] == "cd":
            if args[2] == "/":
                cd = ""
            elif args[2] == "..":
                cd = "/".join(cd.split("/")[:-1])
                print(f"Back to {cd}")
            else:
                cd = f"{cd}/{args[2]}"
                print(f"Entered {cd}")
                folders.append(cd)

        elif args[1] == "ls":
            cur = text.tell()
            while (i := text.readline().strip()) != "" and i[0] != "$":
                if not i.startswith("dir"):
                    split = i.split(" ")
                    name = "/".join([cd, split[1]])
                    size = int(split[0])
                    files[name] = size
                else:
                    #name = "/".join([cd, i.split(" ")[1]])
                    #folders.append(name)
                    pass
                cur = text.tell()
            text.seek(cur)

    total = 0
    smallfolders = []
    smallfiles = []
    for f in set(folders):
        if f == "/":
            continue
        size = 0
        print(f"ls: {f}: Is a directory")
        for k, v in files.items():
            if k.startswith(f + "/"):
                #print(f" - {k} ({v} bytes)")
                size += v
        print(f" - {size} bytes")
        if size <= 100000:
            total += size
            smallfolders.append(f)
            for k, v in files.items():
                if k.startswith(f):
                    smallfiles.append(k)

    print(f"Total: {total} bytes")

    filetree = {}
    for i in files:
        split = i.split("/")
        assert not (split) == 1
        cur = filetree
        for f in split[:-1]:
            if f not in cur:
                cur[f] = {}
            cur = cur[f]
        cur[split[-1]] = files[i]

    total = 0

    smallfolders2 = []

    calc_size(filetree, smallfolders2, "")

    #'/bfqzjjct/phslrcw'

    smallfolders2 = [i[1:] for i in smallfolders2]

    for i in smallfolders:
        smallfolders2.remove(i)

    print(total)

def calc_size(tree, l, path):
    global total

    if isinstance(tree, int):
        return tree
    else:
        s = sum(calc_size(tree[i], l, "/".join([path, i])) for i in tree)
        if s <= 100000:
            total += s
            l.append(path)
        return s

def main2():
    text = io.StringIO(util.get_input(7))
    files = {}
    folders = []
    cd = ""
    while (line := text.readline().strip()) != "":
        args = line.split(" ")
        assert args[0] == "$"
        if args[1] == "cd":
            if args[2] == "/":
                cd = ""
            elif args[2] == "..":
                cd = "/".join(cd.split("/")[:-1])
            else:
                cd = f"{cd}/{args[2]}"
                folders.append(cd)

        elif args[1] == "ls":
            cur = text.tell()
            while (i := text.readline().strip()) != "" and i[0] != "$":
                if not i.startswith("dir"):
                    split = i.split(" ")
                    name = "/".join([cd, split[1]])
                    size = int(split[0])
                    files[name] = size
                else:
                    # name = "/".join([cd, i.split(" ")[1]])
                    # folders.append(name)
                    pass
                cur = text.tell()
            text.seek(cur)

    foldersizes = {}
    for f in set(folders):
        if f == "/":
            continue
        size = 0
        for k, v in files.items():
            if k.startswith(f):
                size += v
        foldersizes[f] = size

    size_needed = sum(files.values()) - 40000000

    print(f"Size needed: {size_needed}")

    smallest = 1000000000000000000
    smallestfolder = ""

    for f in foldersizes:
        if foldersizes[f] >= size_needed and foldersizes[f] < smallest:
            smallestfolder = f
            smallest = foldersizes[f]

    print(smallestfolder, smallest)

if __name__ == "__main__":
    main()
    #main2()