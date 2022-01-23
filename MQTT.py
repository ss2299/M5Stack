# M5Stick

from m5stack import *
from m5ui import *
from uiflow import *
from m5mqtt import M5mqtt
import wifiCfg

setScreenColor(0x111111)


wifiCfg.doConnect('ssid', 'password')
label0 = M5TextBox(0, 10, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
label1 = M5TextBox(0, 25, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
labelX = M5TextBox(0, 140, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)

i = 0
total = 0

if wifiCfg.wlan_sta.isconnected():
    m5mqtt = M5mqtt('', '192.168.1.122', 1883, '', '', 300)
    m5mqtt.start()

while True:
    if wifiCfg.wlan_sta.isconnected():
        label0.setText('Wifi Yes')
        label1.setText(wifiCfg.wlan_sta.ifconfig()[0])      
    else:
        label0.setText('Wifi NO')

    labelX.setText(str(i))
    i = i+1
    if i > 10:
        i = 0    
        total = total + 1
        m5mqtt.publish('total',str(total))

    wait_ms(2)

    