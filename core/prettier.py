from time import sleep

class COLOURS():
    black: str = "\33[1;30m"
    red: str = "\33[1;31m"
    green: str = "\33[1;32m"
    yellow: str = "\33[1;33m"
    blue: str = "\33[1;34m"
    magenta: str = "\33[1;35m"
    cyan: str = "\33[1;36m"
    white: str = "\33[1;37m"
    default: str = "\33[1;39m"
    blue_blink: str = "\33[5;34m"
    reset: str = "\33[0;m"

def printy(text: str, color_code: str = COLOURS.default, time: int = 0, end: str = "\n"):
    if not time:
        print(color_code + text, end=end)
        return
    
    for i in range(len(text)):
        if i < len(text) - 1:
            print(color_code+text[:i], end="\r")
        else:
            print(color_code+text, end=end)
        sleep(time / len(text))

    print(COLOURS.reset+COLOURS.default, end="")