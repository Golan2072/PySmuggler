# PySmuggler Map Script

import stellagama
import main


class Star:
    def __init__(self, startype, gas_giant, starport, naval, scout, names, hex_column, hex_row):
        self.startype = startype
        self.gas_giant = gas_giant
        self.starport = starport
        self.naval = naval
        self.scout = scout
        self.names = names
        self.column = hex_column
        self.row = hex_row
        if self.column == 10 and self.row != 10:
            self.hex = f"100{self.row}"
        elif self.column != 10 and self.row == 10:
            self.hex = f"0{self.column}10"
        elif self.column == 10 and self.row == 10:
            self.hex = "1010"
        else:
            self.hex = f"0{self.column}0{self.row}"
        self.neighbors = ["", (self.column, self.row - 1), (self.column + 1, self.row - 1), (self.column + 1, self.row),
                          (self.column, self.row + 1), (self.column - 1, self.row), (self.column - 1, self.row - 1)]

    def name_converter(self):
        new_name = f"{self.names: <{7}}".upper()
        self.mapname = (new_name[:7]) if len(new_name) > 7 else new_name


def blank_map():
    starmap = {}
    for column in range(0, 11):
        starmap[column] = {}
        for map_row in range(0, 11):
            starmap[column][map_row] = Star(" ", " ", "   ", " ", "_", "       ", 0, 0)
    return starmap


def base_row(base_row_string):
    row_string = ""
    for i in range(0, 4):
        row_string += base_row_string
    return row_string


def hex_number(column, row, worldtype):
    if column % 2 == 0:
        if (row == 1) or (row == 0):
            return "____"
        elif worldtype == " ":
            return "____"
        elif row == 11:
            return f"0{column}10"
        else:
            return f"0{column}0{row - 1}"
    else:
        if worldtype == " ":
            return "____"
        elif row == 10:
            return f"0{column}10"
        else:
            return f"0{column}0{row}"


def starmap_renderer(starmap):
    global row
    global column
    star_string = f"\n HEXACORP OS v.21.1\n\n CEPHEUS SECTOR\n\n {base_row('  _____       ')}\n"

    for row in range(1, 11):
        star_string += f"  / {starmap[1][row].starport}{starmap[1][row].gas_giant}\{starmap[2][row - 1].names}/ {starmap[3][row].starport}{starmap[3][row].gas_giant}\{starmap[4][row - 1].names}/ {starmap[5][row].starport}{starmap[5][row].gas_giant}\{starmap[6][row - 1].names}/ {starmap[7][row].starport}{starmap[7][row].gas_giant}\{starmap[8][row - 1].names}/ \n"
        star_string += f" /{starmap[1][row].naval}  {starmap[1][row].startype}   \{starmap[2][row - 1].scout}{hex_number(2, row, starmap[2][row - 1].startype)}/{starmap[3][row].naval}  {starmap[3][row].startype}   \{starmap[4][row - 1].scout}{hex_number(4, row, starmap[4][row - 1].startype)}/{starmap[5][row].naval}  {starmap[5][row].startype}   \{starmap[6][row - 1].scout}{hex_number(6, row, starmap[6][row - 1].startype)}/{starmap[7][row].naval}  {starmap[7][row].startype}   \{starmap[8][row - 1].scout}{hex_number(8, row, starmap[8][row - 1].startype)}/ \n"
        star_string += f" \{starmap[1][row].names}/ {starmap[2][row].starport}{starmap[2][row].gas_giant}\{starmap[3][row].names}/ {starmap[4][row].starport}{starmap[4][row].gas_giant}\{starmap[5][row].names}/ {starmap[6][row].starport}{starmap[6][row].gas_giant}\{starmap[7][row].names}/ {starmap[8][row].starport}{starmap[8][row].gas_giant}\ \n"
        star_string += f"  \{starmap[1][row].scout}{hex_number(1, row, starmap[1][row].startype)}/{starmap[2][row].naval}  {starmap[2][row].startype}   \{starmap[3][row].scout}{hex_number(3, row, starmap[3][row].startype)}/{starmap[4][row].naval}  {starmap[4][row].startype}   \{starmap[5][row].scout}{hex_number(5, row, starmap[5][row].startype)}/{starmap[6][row].naval}  {starmap[6][row].startype}   \{starmap[7][row].scout}{hex_number(7, row, starmap[7][row].startype)}/{starmap[8][row].naval}  {starmap[8][row].startype}   \ \n"
    star_string += f"        \{starmap[2][10].names}/     \{starmap[4][10].names}/     \{starmap[6][10].names}/     \{starmap[8][10].names}/\n"
    star_string += f"         \{starmap[2][10].scout}{hex_number(2, 11, starmap[2][row].startype)}/       \{starmap[4][10].scout}{hex_number(4, 11, starmap[4][10].startype)}/       \{starmap[6][10].scout}{hex_number(6, 11, starmap[6][10].startype)}/       \{starmap[8][10].scout}{hex_number(8, 11, starmap[8][10].startype)}/\n\n"
    return star_string


def starmap_screen_render(starmap):
    stellagama.clear_screen()
    print(starmap_renderer(starmap) + "\n")
    print(f"LOCATION: {player.location.hex} {player.location.names}\n")


def star_data(starmap, renderer, stars):
    data_star = input("ENTER STAR COORDINATES: ")
    if data_star in stars:
        star = starmap[int(data_star[1])][int(data_star[3])]
        print(f"STAR DATA: STAR TYPE {star.startype}")
    else:
        stellagama.clear_screen()
        print(renderer + "\n")
        print(f"LOCATION: {player.location.hex} {player.location.names}\n")
        print("INVALID INPUT")


def map_menu(player, starmap):
    print(starmap_renderer(starmap) + "\n")
    print(f"LOCATION: {player.location.hex} {player.location.names}\n")
    destination = 0
    while True:
        command = main.command_prompt(player, ["JUMP", "DATA"], starmap_renderer(starmap))
        if command == "JUMP":
            starmap_screen_render(starmap)
            player.jump()
        elif command == "DATA":
            starmap_screen_render(starmap)
            star_data(starmap, starmap_renderer(starmap), ["0101", "0201", "0102", "0205"])
        else:
            pass


if __name__ == '__main__':
    starmap = blank_map()
    starmap[1][1] = Star("@", "*", " V ", "*", "^", "TEST   ", 1, 1)
    starmap[2][1] = Star("O", " ", " IV", " ", " ", "TEST2  ", 2, 1)
    starmap[1][2] = Star("O", " ", "III", " ", " ", "TEST3  ", 1, 2)
    starmap[2][5] = Star("O", " ", " I ", " ", " ", "TEST4  ", 1, 2)
    player = main.Player(starmap)
    map_menu(player, starmap)
