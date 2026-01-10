import storage
import usb_cdc
import usb_hid
import adafruit_ble

ble = adafruit_ble.BLERadio()
ble.name = "XIAO-Split-20"

storage.disable_usb_drive() 
usb_cdc.disable()
usb_hid.enable(boot_device=1)
