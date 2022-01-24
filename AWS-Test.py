from m5stack import *
from m5ui import *
from uiflow import *
from IoTcloud.AWS import AWS
import wifiCfg
import json

import time
import imu

setScreenColor(0x111111)


i = None

wifiCfg.doConnect('Affendy&Sense(2.4Ghz)', 'Imaffendy123!@#')
wifiCfg.autoConnect(lcdShow=False)
imu0 = imu.IMU()
label0 = M5TextBox(26, 89, "Text", lcd.FONT_Default, 0xFFFFFF, rotate=0)
title0 = M5Title(title="Title", x=3, fgcolor=0xFFFFFF, bgcolor=0x0000FF)



def fun_core2_msg_(topic_data):
    title0.setTitle(str(topic_data))
    pass


i = 0
aws = AWS(things_name='M5StickC', host='a15ne2ln1dpirc-ats.iot.ap-southeast-2.amazonaws.com', port=8883, keepalive=60, cert_file_path="/flash/res/M5StickC_Sydney-certificate.pem.crt", private_key_path="/flash/res/M5StickC_Sydney-private.pem.key")
aws.subscribe(str('core2/msg'), fun_core2_msg_)
aws.start()

while True:
    aws.publish(str('core2/env'), str(json.dumps({'tmp': '1'})))
    label0.setText(str(i))
    wait(10)
    i = i + 1
    wait_ms(2)
