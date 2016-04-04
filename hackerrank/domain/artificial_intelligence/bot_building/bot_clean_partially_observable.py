from functools import partial
import os.path


def deleteContent(pfile):
    pfile.seek(0)
    pfile.truncate()


def next_move(bot_x, bot_y, board):
    is_present = os.path.isfile('bot-building.txt')
    if is_present:
        f = open('bot-building.txt', 'r+')
    else:
        f = open('bot-building.txt', 'w')
    l = [['o' for j in range(5)] for i in range(5)]
    if is_present:
        i = 0
        for line in f:
            for j in range(5):
                l[i][j] = line[j]
            i += 1
    dirty_cells = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                dirty_cells.append((i, j))
                l[i][j] = '-'
            elif board[i][j] == '-' or board[i][j] == 'b':
                l[i][j] = '-'
    # print l
    x = bot_x
    y = bot_y
    if dirty_cells:
        # Get closest cell
        dist = lambda s, d: (s[0] - d[0]) ** 2 + (s[1] - d[1]) ** 2
        closest_dirty_cell = min(dirty_cells,
                                 key=partial(dist, (bot_x, bot_y)))
        x = closest_dirty_cell[0]
        y = closest_dirty_cell[1]
        if len(dirty_cells) > 1:
            for i in dirty_cells:
                l[i[0]][i[1]] = 'o'
    else:
        undiscovered_cells = []
        for i in range(5):
            for j in range(5):
                if l[i][j] == 'o':
                    undiscovered_cells.append((i, j))
        if undiscovered_cells:
            dist = lambda s, d: (s[0] - d[0]) ** 2 + (s[1] - d[1]) ** 2
            closest_dirty_cell = min(undiscovered_cells,
                                     key=partial(dist, (bot_x, bot_y)))
            x = closest_dirty_cell[0]
            y = closest_dirty_cell[1]
    deleteContent(f)
    for line in l:
        f.write("".join(line) + "\n")
    # print x, y
    move = ""
    if bot_y != y:
        if bot_y > y:
            move = "LEFT"
        else:
            move = "RIGHT"
    elif bot_x != x:
        if bot_x > x:
            move = "UP"
        else:
            move = "DOWN"
    else:
        move = "CLEAN"
    print move


if __name__ == "__main__":
    pos = [int(i) for i in raw_input().strip().split()]
    board = [[j for j in raw_input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
