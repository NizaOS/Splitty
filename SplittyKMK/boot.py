import supervisor
import usb_hid

supervisor.set_next_stack_limit(4096 + 4096)
usb_hid.enable(
    (usb_hid.Device.KEYBOARD,
     usb_hid.Device.MOUSE,
     usb_hid.Device.CONSUMER_CONTROL)
)
