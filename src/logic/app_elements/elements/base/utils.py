digit = int | float


def round_to_two(number: float) -> float:
    return round(number, 2)


def figure_size(elem: tuple[any]) -> tuple[float, float] | None:
    el_count = len(elem)
    if el_count == 0:
        return

    height = el_count * 0.2
    width = (el_count * 0.2) - 0.1
    return round_to_two(width), round_to_two(height)


def figure_padding(size: tuple[digit, digit], count: int) -> digit:
    height = size[1]
    return height / (count + 1)


def figure_pos(size, y: digit, offset: tuple) -> tuple[float, float]:
    width = size[0]
    dx, dy = offset
    return round_to_two((width / 2) + dx), round_to_two(y + dy)


def figure_real_pos(outer_pos: tuple[digit, digit], inner_pos: tuple[digit, digit]) -> tuple[float, float]:
    outer_x, outer_y = outer_pos
    inner_x, inner_y = inner_pos
    return round_to_two(outer_x + inner_x), round_to_two(outer_y + inner_y)


def figure_positions(size: tuple[digit, digit], elem_params: tuple[any],
                     offset: tuple) -> tuple[digit, digit]:
    elem_count = len(elem_params)

    padding = figure_padding(size, elem_count)

    for counter in range(1, elem_count + 1):
        position = figure_pos(size, counter * padding, offset)
        yield position
