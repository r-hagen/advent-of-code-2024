input = open("day04.in").read().split("\n")

G = [list(x) for x in input]
rows = len(G)
columns = len(G[0])

search_term = list("XMAS")


def search_right(r, c):
    if c + 3 >= columns:
        return False
    term = [G[r][col] for col in range(c, c + 4)]
    return term == search_term


def search_left(r, c):
    if c - 3 < 0:
        return False
    term = [G[r][col] for col in range(c, c - 4, -1)]
    return term == search_term


def search_down(r, c):
    if r + 3 >= rows:
        return False
    term = [G[row][c] for row in range(r, r + 4)]
    return term == search_term


def search_up(r, c):
    if r - 3 < 0:
        return False
    term = [G[row][c] for row in range(r, r - 4, -1)]
    return term == search_term


def search_right_up(r, c):
    if r - 3 < 0 or c + 3 >= columns:
        return False
    term = [G[r - i][c + i] for i in range(4)]
    return term == search_term


def search_right_down(r, c):
    if r + 3 >= rows or c + 3 >= columns:
        return False
    term = [G[r + i][c + i] for i in range(4)]
    return term == search_term


def search_left_up(r, c):
    if r - 3 < 0 or c - 3 < 0:
        return False
    term = [G[r - i][c - i] for i in range(4)]
    return term == search_term


def search_left_down(r, c):
    if r + 3 >= rows or c - 3 < 0:
        return False
    term = [G[r + i][c - i] for i in range(4)]
    return term == search_term


ans1 = 0
for r in range(len(G)):
    for c in range(len(G[r])):
        if G[r][c] == "X":
            if search_right(r, c):
                ans1 += 1
            if search_left(r, c):
                ans1 += 1
            if search_down(r, c):
                ans1 += 1
            if search_up(r, c):
                ans1 += 1
            if search_right_up(r, c):
                ans1 += 1
            if search_right_down(r, c):
                ans1 += 1
            if search_left_up(r, c):
                ans1 += 1
            if search_left_down(r, c):
                ans1 += 1
print("part1", ans1)


search_term = list("MAS")
ans2 = 0
for r in range(len(G)):
    for c in range(len(G[r])):
        if G[r][c] == "A":
            if r - 1 >= 0 and r + 1 < rows and c - 1 >= 0 and c + 1 < columns:
                d1 = [G[r - 1][c - 1], G[r][c], G[r + 1][c + 1]]
                d2 = [G[r + 1][c - 1], G[r][c], G[r - 1][c + 1]]
                if d1 == search_term or d1[::-1] == search_term:
                    if d2 == search_term or d2[::-1] == search_term:
                        ans2 += 1
print("part2", ans2)
