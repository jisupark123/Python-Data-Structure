class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0

    def __str__(self):
        return "{" + f"{self.key}" + "}"


def make_set(x) -> Node:
    return Node(x)


def find(x: Node) -> Node:
    if x.parent is x:
        return x
    return find(x.parent)


def union(x: Node, y: Node) -> None:
    main_x, main_y = find(x), find(y)
    if main_x.rank >= main_y.rank:
        main_y.parent = main_x
        main_y.rank += 1
    else:
        main_x.parent = main_y
        main_x.rank += 1


def is_same_set(x: Node, y: Node) -> bool:
    return find(x) is find(y)


from sys import stdin

input = stdin.readline
n, m = map(int, input().split())

sets = []
for i in range(n + 1):
    sets.append(make_set(i))

for _ in range(m):
    cmd, x, y = map(int, input().split())
    if cmd == 0:
        union(sets[x], sets[y])
    else:
        print("YES") if is_same_set(sets[x], sets[y]) else print("NO")
