def round_to_two(number: float) -> float:
    return round(number, 2)


def figure_size(elem: dict) -> tuple:
    el_count = len(elem)
    height = el_count * 0.2
    width = (el_count * 0.2) - 0.1
    return round_to_two(width), round_to_two(height)


def figure_padding(size: tuple, count: int) -> int | float:
    height = size[1]
    return height / (count + 1)


def figure_pos(size, y: int | float, offset: tuple) -> tuple:
    width = size[0]
    dx, dy = offset
    return round_to_two((width // 2) + dx), round_to_two(y + dy)


def figure_real_pos(outer_pos: tuple, inner_pos: tuple) -> tuple:
    outer_x, outer_y = outer_pos
    inner_x, inner_y = inner_pos
    return outer_x + inner_x, outer_y + inner_y


def figure_positions(size: tuple, elem_params: dict, offset: tuple) -> tuple:
    elem_count = len(elem_params)

    padding = figure_padding(size, elem_count)

    for counter in range(1, elem_count + 1):
        position = figure_pos(size, counter * padding, offset)
        yield position


def get_menu_params(menu: any) -> dict:
    params = {
        'frame': {
            'pos': menu.pos,
            'size': menu.size
        },
        'elements': {element.text: element.pos for element in menu.elements}
    }
    return params
