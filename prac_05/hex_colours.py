COLOR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}

color_name = input("Enter a color name: ").lower()
while color_name != "":
    try:
        color_name=[key for key, value in COLOR_TO_HEX.items() if key.lower() == color_name]
        color_name="".join(color_name)
        hex=COLOR_TO_HEX[color_name]
        print(f"The hex code for {color_name} is {hex}")
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter a color name: ").lower()

