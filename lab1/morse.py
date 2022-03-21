import sys

MORSE_CODE = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
}


def morse(message):
    morse_text = ""
    last_slash = False
    for letter in message.lower():
        if letter.isalpha():
            morse_text += MORSE_CODE[letter] + " "
            last_slash = False
        elif letter == " " and not last_slash:
            morse_text += "/ "
            last_slash = True
    return morse_text


def main():
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        with open(filename) as file:
            lines = file.readlines()
            for line in lines:
                print(morse(line))
    else:
        print("No file name was given!")


if __name__ == "__main__":
    main()
