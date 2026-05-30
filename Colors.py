def color(color_1: str, color_2: str):

    if ((color_1.lower(), color_2.lower()) == ("red", "yellow") or (color_2.lower(), color_1.lower()) == ("red", "yellow")):
        return print("Orange")
    elif ((color_1.lower(), color_2.lower()) == ("red", "blue") or (color_2.lower(), color_1.lower()) == ("red", "blue")):
        return print("Violet")
    elif ((color_1.lower(), color_2.lower()) == ("yellow", "blue") or (color_2.lower(), color_1.lower()) == ("yellow", "blue")):
        return print("Green")
    else:
        return print("Error")

color1 = str(input())
color2 = str(input())
color(color1, color2)