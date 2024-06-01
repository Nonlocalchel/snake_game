from src.pages.game_menu.input import Input

new_input = Input('Имя', (0, 0))

print(new_input.text)

new_input.change('remove')
new_input.change('remove')
new_input.change('s')

print(new_input.text)