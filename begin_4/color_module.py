print("Hello from module.py")
print(
    """The module contains:
    1. variable called var
    2. dictionary called colors
    3. cool function called colorText
    4. lame function called meh
    """
)

var = "Variable inside color_module"

Colors = {
    "RESET": "\u001b[0m",

    "BLACK-BR": "\u001b[30;1m",
    "RED-BR": "\u001b[31;1m",
    "GREEN-BR": "\u001b[32m",
    "BLUE-BR": "\u001b[34;1m",
    "MAGENTA-BR": "\u001b[35m",
    "CYAN-BR": "\u001b[36m",

    "RED-BG": "\u001b[41;1m",
    "GREEN-BG": "\u001b[42;1m",
    "CYAN-BG": "\u001b[46;1m",
}


def colorText(regular_text):
    for color in Colors:
        regular_text = regular_text.replace("((" + color + "))", Colors[color])
    return regular_text


def meh():
    function_message = "((RED-BR))Hi i'm lame function((RESET))"
    print(colorText(function_message))
