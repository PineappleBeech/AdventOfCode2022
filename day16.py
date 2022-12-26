import re

import util

#from line_profiler_pycharm import profile

def time(path, paths):
    return sum(paths[p] for p in zip(path[:-1], path[1:])) + len(path) - 1

def cost(start, end, paths, valves):
    return valves[end] / (paths[(start, end)] + 1)

def score(path, time, paths, valves):
    time_counter = 0
    pressure = 0
    for p in zip(path[:-1], path[1:]):
        time_counter += paths[p] + 1
        pressure += valves[p[1]] * (time - time_counter)
    return pressure

def look_ahead(path, paths, valves):
    scores = {}
    for p in paths:
        if p[0] == path[-1] and p[1] not in path:
            if time(path + [p[1]], paths) < 30:
                scores.update(look_ahead(path + [p[1]], paths, valves))
    if len(scores) == 0:
        return {tuple(path): score(path, 30, paths, valves)}
    return scores

def main():
    lines = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()
    lines = util.get_input(16).splitlines()
    paths = {}
    valves = {}
    for line in lines:
        valve = re.match(r"Valve ([A-Z]{2})", line).group(1)
        flow = int(re.match(r"Valve [A-Z]{2} has flow rate=([0-9]+)", line).group(1))
        tunnels = re.findall(r"([A-Z]{2})", line)[1:]
        valves[valve] = flow
        for tunnel in tunnels:
            paths[(valve, tunnel)] = 1

    changed = True

    while changed:
        old_paths = paths.copy()
        changed = False
        for p1 in old_paths:
            for p2 in old_paths:
                if p1[1] == p2[0] and p1[0] != p2[1]:
                    if (p1[0], p2[1]) not in paths or paths[p1] + paths[p2] < paths[(p1[0], p2[1])]:
                        paths[(p1[0], p2[1])] = paths[p1] + paths[p2]
                        changed = True

    old_paths = paths.copy()

    valves["AA"] = -1

    for p in old_paths:
        if valves[p[0]] == 0 or valves[p[1]] == 0:
            del paths[p]

    valves["AA"] = 0

    final_path = ["AA"]

    print(final_path)

    options = look_ahead(final_path, paths, valves)

    final_path = max(options, key=options.get)
    print(final_path)
    print(options[final_path])
    print()

def to_tuple(l):
    return tuple(tuple(x) for x in l)

def contains(l, i):
    for x in l:
        if i in x:
            return True
    return False

def extend(l, index, value):
    l2 = list(l)
    l2[index] = l2[index] + (value,)
    return tuple(l2)

def score2(path, time, paths, valves):
    return sum(score(p, time, paths, valves) for p in path)

def look_ahead2(path, paths, valves, depth):
    if depth == 0:
        return {to_tuple(path): score2(path, 26, paths, valves)}
    scores = {}
    for p in paths:
        for i in range(2):
            if p[0] == path[i][-1] and not contains(path, p[1]):
                if time(path[i] + (p[1],), paths) < 26:
                    scores.update(look_ahead2(extend(path, i, p[1]), paths, valves, depth - 1))
    if len(scores) == 0:
        return {to_tuple(path): score2(path, 26, paths, valves)}
    return scores

def freeze(path):
    return frozenset(path)
    return (frozenset(frozenset(x[:-1]) for x in path), frozenset((path[0][-1], path[1][-1])))

#@profile
def main2():
    lines = """Valve AA has flow rate=0; tunnels lead to valves DA, IA, BA
Valve BA has flow rate=13; tunnels lead to valves CA, AA
Valve CA has flow rate=2; tunnels lead to valves DA, BA
Valve DA has flow rate=20; tunnels lead to valves CA, AA, EA
Valve EA has flow rate=3; tunnels lead to valves FA, DA
Valve FA has flow rate=0; tunnels lead to valves EA, GA
Valve GA has flow rate=0; tunnels lead to valves FA, HA
Valve HA has flow rate=22; tunnel leads to valve GA
Valve IA has flow rate=0; tunnels lead to valves AA, JA
Valve JA has flow rate=21; tunnel leads to valve IA""".splitlines()
    lines = util.get_input(16).splitlines()
    print("jjeijko")
    paths = {}
    valves = {}
    for line in lines:
        valve = re.match(r"Valve ([A-Z]{2})", line).group(1)
        flow = int(re.match(r"Valve [A-Z]{2} has flow rate=([0-9]+)", line).group(1))
        tunnels = re.findall(r"([A-Z]{2})", line)[1:]
        valves[valve] = flow
        for tunnel in tunnels:
            paths[(valve, tunnel)] = 1

    changed = True

    while changed:
        old_paths = paths.copy()
        changed = False
        for p1 in old_paths:
            for p2 in old_paths:
                if p1[1] == p2[0] and p1[0] != p2[1]:
                    if (p1[0], p2[1]) not in paths or paths[p1] + paths[p2] < paths[(p1[0], p2[1])]:
                        paths[(p1[0], p2[1])] = paths[p1] + paths[p2]
                        changed = True

    old_paths = paths.copy()

    valves["AA"] = -1

    for p in old_paths:
        if valves[p[0]] == 0 or valves[p[1]] == 0:
            del paths[p]

    valves["AA"] = 0

    final_path = to_tuple([["AA"], ["AA"]])

    current_layer = [final_path]
    max_score = 0
    old_max_score = -1
    max2 = 0

    i = 0

    path_map = {}
    for p in paths:
        if p[0] not in path_map:
            path_map[p[0]] = {}

        path_map[p[0]][p[1]] = paths[p]

    for p in path_map.values():
        p[""] = ""

    # iterate through layers/turns
    while True:
        i += 1
        print(f"Doing layer {i} with {len(current_layer)} paths")
        next_layer = []
        j = 0
        for path in current_layer:
            j += 1
            if j % 1000 == 0:
                print(f"Doing path {j} of {len(current_layer)}")
            # for each path, iterate through all combinations of extensions
            for p1 in path_map[path[0][-1]]:
                for p2 in path_map[path[1][-1]]:
                    if p1 == p2:
                        continue
                    # focus on path 1
                    if len(path[0]) > len(path[1]):
                        p2 = ""
                    # focus on path 2
                    elif len(path[0]) < len(path[1]):
                        p1 = ""

                    if p1 == "" and p2 == "":
                        continue

                    new_path = path

                    # continues make sure that the path is extended or skipped
                    if p1 != "":
                        if not contains(path, p1):
                            if time(path[0] + (p1,), paths) < 26:
                                new_path = extend(new_path, 0, p1)
                            else:
                                continue  # not continuing gives duplicate paths
                        else:
                            continue  # invalid path is different to no path - causes duplicates
                    if p2 != "":
                        if not contains(path, p2):
                            if time(path[1] + (p2,), paths) < 26:
                                new_path = extend(new_path, 1, p2)
                            else:
                                continue
                        else:
                            continue

                    if new_path != path:
                        next_layer.append(new_path)
                        max2 = max(max2, score2(new_path, 26, paths, valves))

                    # path 1 is longer
                    if p2 == "":
                        break

                # path 2 is longer
                if p1 == "":
                    break

        if len(next_layer) == 0:
            break

        next_layer_sets = {}

        for path in next_layer:
            if freeze(path) not in next_layer_sets:
                next_layer_sets[freeze(path)] = path
            else:
                next_layer_sets[freeze(path)] = max(next_layer_sets[freeze(path)], path, key=lambda x: score2(x, 26, paths, valves))

        print(f"Reduced from {len(next_layer)} to {len(next_layer_sets)} paths")
        next_layer = list(next_layer_sets.values())

        next_layer_scores = {}
        for path in next_layer:
            next_layer_scores[path] = score2(path, 26, paths, valves)

        next_layer = sorted(next_layer, key=lambda x: next_layer_scores[x], reverse=True)
        next_layer = next_layer[:1000]

        old_max_score = max(max_score, old_max_score)
        max_score = max(score2(path, 26, paths, valves) for path in next_layer)
        max_paths = [path for path in next_layer if score2(path, 26, paths, valves) == max_score]
        if max_score > old_max_score:
            print(f"New max score: {max_score}")
            max_path = [path for path in next_layer if score2(path, 26, paths, valves) == max_score]
            #break

        current_layer = set(next_layer)
        print(f"Removed {len(next_layer) - len(current_layer)} duplicate paths out of {len(next_layer)}")

    #final_path = max(options, key=options.get)
    print(old_max_score)
    print(max_path)
    print(max2)

if __name__ == "__main__":
    main2()