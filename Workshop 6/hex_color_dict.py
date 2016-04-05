HEX_COLORS = {"Alice Blue": "#f0f8ff", "Antique White": "#faebd7", "Antique White1": "#ffefdb",
              "Antique White2": "#eedfcc", "Antique White3": "#cdc0b0", "Antique White4": "#8b8378",
              "Aqua Marine1": "#7fffd4"}
# print(STATE_NAMES)

color = input("Enter color name: ").title()
while color != "":
    if color in HEX_COLORS:
        print(color, "is", HEX_COLORS[color])
        color = input("Enter color name: ").title()
    else:
        print("Invalid color name")
        color = input("Enter color name: ").title()
