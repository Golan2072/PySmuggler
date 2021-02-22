# PySmuggler main file

import stellagama
import map


class Player:
    def __init__(self, starmap):
        self.coordinates = (1, 1)
        self.starmap = starmap
        self.location = starmap[self.coordinates[0]][self.coordinates[1]]

    def jump(self):
        coordinates_input = str(input("INPUT COORDINATES (4 DIGITS HEX LOCATION): "))
        coordinates = (int(coordinates_input[1]), int(coordinates_input[3]))
        if coordinates in self.location.neighbors and self.starmap[coordinates[0]][coordinates[1]].startype != " ":
            self.coordinates = coordinates
            self.location = self.starmap[self.coordinates[0]][self.coordinates[1]]
            print(f"JUMP to {self.location.names} SUCCESSFUL")
        elif self.starmap[coordinates[0]][coordinates[1]].startype != " ":
            print("DESTINATION NOT IN RANGE")
        else:
            print("NO VALID JUMP DESTINATION")


def command_prompt(player, commands, renderer):
    print("")
    print(f"AVAILABLE COMMANDS: {' / '.join(commands)} / EXIT")
    command = input("ENTER COMMAND: ").upper()
    if command in commands:
        return command
    elif command == "EXIT":
        print("TERMINATING PROGRAM")
        quit()
    else:
        stellagama.clear_screen()
        print(renderer + "\n")
        print(f"LOCATION: {player.location.hex} {player.location.names}\n")
        print("INVALID COMMAND")