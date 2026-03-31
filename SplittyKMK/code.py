from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
import board

print("the kmk libs r working")

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.D2, board.D3, board.D4, board.D5, board.D6
)

keyboard.row_pins = (
    board.D10, board.D9, board.D8, board.D7
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R, KC.T,
        KC.A, KC.S, KC.D, KC.F, KC.G,
        KC.Z, KC.X, KC.C, KC.V, KC.B,
        KC.ESC, KC.SPACE, KC.ENTER, KC.BSPC, KC.TAB
    ]
]

keyboard.go()
