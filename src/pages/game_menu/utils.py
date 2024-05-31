def figure_size(elem: dict) -> tuple:
    el_count = len(elem)
    height = el_count * 0.2
    width = (el_count * 0.2) - 0.1
    return width, height


def figure_padding(size: tuple, count: int) -> int | float:
    height = size[1]
    return height / (count + 1)


def figure_pos(size, y: int | float, offset: tuple) -> tuple:
    width = size[0]
    dx, dy = offset
    return round((width // 2) + dx, 2), round(y + dy, 2)


def figure_real_pos(outer_pos: tuple, inner_pos: tuple) -> tuple:
    outer_x, outer_y = outer_pos
    inner_x, inner_y = inner_pos
    return outer_x + inner_x, outer_y + inner_y


def figure_positions(size: tuple, elem_params: dict, offset: tuple):
    elem_count = len(elem_params)

    padding = figure_padding(size, elem_count)

    for counter in range(1, elem_count + 1):
        yield figure_pos(size, counter * padding, offset)
