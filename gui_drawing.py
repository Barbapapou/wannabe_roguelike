import tcod


def draw_array(console: tcod.Console, nbr_row: int, nbr_column: int, pad_x: int, pad_y: int, start_x: int, start_y: int):
    for i in range(nbr_column * (pad_x + 1) + 1):
        for j in range(nbr_row * (pad_y + 1) + 1):
            x = start_x + i
            y = start_y + j
            if x == start_x and y == start_y:
                console.print(x, y, "┌")
            elif x == start_x + (pad_x + 1) * nbr_column and y == start_y:
                console.print(x, y, "┐")
            elif x == start_x and y == start_y + (pad_y + 1) * nbr_row:
                console.print(x, y, "└")
            elif x == start_x + (pad_x + 1) * nbr_column and y == start_y + (pad_y + 1) * nbr_row:
                console.print(x, y, "┘")
            elif x == start_x and j % (pad_y + 1) == 0:
                console.print(x, y, "├")
            elif x == start_x + (pad_x + 1) * nbr_column and j % (pad_y + 1) == 0:
                console.print(x, y, "┤")
            elif i % (pad_x + 1) == 0 and y == start_y:
                console.print(x, y, "┬")
            elif i % (pad_x + 1) == 0 and y == start_y + (pad_y + 1) * nbr_row:
                console.print(x, y, "┴")
            elif i % (pad_x + 1) == 0 and j % (pad_y + 1) == 0:
                console.print(x, y, "┼")
            elif i % (pad_x + 1) == 0:
                console.print(x, y, "│")
            elif j % (pad_y + 1) == 0:
                console.print(x, y, "─")
