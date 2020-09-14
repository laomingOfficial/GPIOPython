#匯入模組 - Import library
import RPi.GPIO as GPIO
import time

#Pin變數 - Pin variable
LED_PIN = 21

#設置GPIO - GPIO Setup
GPIO.setmode(GPIO.BCM) #GPIO.BCM (GPIO引腳號) / GPIO.BOARD (物理引腳號)
GPIO.setup(LED_PIN, GPIO.OUT)

#無限循環
while True:
	#輸出高電平 High
	GPIO.output(LED_PIN, 1)
	#卡著等待0.1秒，再繼續執行下一行
	time.sleep(0.1)
	#輸出低電平 Low
	GPIO.output(LED_PIN, 0)
	#卡著等待0.1秒，再繼續循環
	time.sleep(0.1)