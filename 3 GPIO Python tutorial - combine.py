#匯入模組 - Import library
import RPi.GPIO as GPIO
import time

#Pin變數 - Pin variable
BUTTON_PIN = 16
LED_PIN = 21

#設置GPIO - GPIO Setup
GPIO.setmode(GPIO.BCM) #GPIO.BCM (GPIO引腳號) / GPIO.BOARD (物理引腳號)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)

#無限循環
while True:
    #讀取硬體信號/狀態
    BUTTON_STATUS = GPIO.input(BUTTON_PIN)
    if (BUTTON_STATUS == True):
        #如果信號是高電平，就打印'3.3'
        #高電平 = High 或 1 或 3.3V 或 True
        print('3.3')
        
        #輸出高電平 High
        GPIO.output(LED_PIN, 1)
    else:
        #如果信號是低電平，就打印'0'
        #低電平 = Low 或 0 或 0V 或 False
        print('0')
        
        #輸出低電平 Low
        GPIO.output(LED_PIN, 0)
        
    #卡著等待0.1秒，再繼續循環
    time.sleep(0.1)