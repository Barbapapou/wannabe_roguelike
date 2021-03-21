from typing import Tuple


import tcod


class TextInputHandler:

    def __init__(self, console: tcod.Console, coord: Tuple[int, int]):
        self.console: tcod.Console = console
        self.pos: Tuple[int, int] = coord
        self.written_string: str = ""
        self.typing: bool = False
        self.showed_string: str = f":{self.written_string}"

        self.console.print(self.pos[0], self.pos[1], self.showed_string)

    def on_render(self):
        self.showed_string: str = f":{self.written_string}"
        if self.typing:
            self.showed_string: str = f":{self.written_string}|"
        self.console.print(self.pos[0], self.pos[1], self.showed_string)

    def ev_keydown(self, event: tcod.event.KeyDown) -> bool:
        key = event.sym
        self.typing = True
        if 32 <= key <= 154:
            print(chr(key))
            self.written_string += chr(key)
            return True
        elif key == tcod.event.K_BACKSPACE:
            self.written_string = self.written_string[:-1]
            return True
        elif key == tcod.event.K_RETURN or key == tcod.event.K_ESCAPE:
            self.typing = False
            return False
        return True
