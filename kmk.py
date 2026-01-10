import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.split import Split, SplitType
from kmk.modules.layers import Layers
from kmk.modules.power import Power
from kmk.modules.vbat import Vbat

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2, board.D3, board.D4)
keyboard.row_pins = (board.D10, board.D9, board.D8, board.D7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

layers = Layers()
power = Power()

vbat = Vbat(
    pin=board.A0,
    divider=2.48,
    voltage_max=4.2,
    voltage_min=3.5
)

split = Split(
    split_type=SplitType.BLE,
    use_data_pin_for_side=False,
    split_side=None,
)

keyboard.modules = [layers, power, vbat, split]

keyboard.keymap = [
    [
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,      KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,      KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,      KC.N,    KC.M,    KC.COMMA,KC.DOT,  KC.SLSH,
        KC.LCTL, KC.LALT, KC.LGUI, KC.LSFT, KC.SPC,    KC.ENT,  KC.BSPC, KC.TAB,  KC.RSFT, KC.MO(1),
    ],
    [
        KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,     KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,
        KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,     KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, KC.QUOT,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS, KC.TRNS, KC.BAT,  KC.TRNS, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS, KC.DEL,  KC.TRNS, KC.TRNS, KC.TRNS,
    ]
]

if __name__ == '__main__':
    keyboard.go()
