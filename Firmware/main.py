import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

keyboard = KMKKeyboard()

# This perfectly matches the exact traces snaking out of your XIAO in the image!
keyboard.matrix = KeysScanner(
    pins=[
        board.D9,  # Physical Pin 11 -> Switch 1
        board.D8,  # Physical Pin 10 -> Switch 2
        board.D7,  # Physical Pin 9  -> Switch 3
      
    ]
)

# This assigns actual keyboard functions to your 8 switches (ordered Switch 1 through 8).
# Right now, they map to numbers 1 through 8. You can change these anytime!
keyboard.keymap = [
    [
        KC.N1,  # Switch 1
        KC.N2,  # Switch 2
        KC.N3,  # Switch 3
       
    ]
]

if __name__ == '__main__':
    keyboard.go()