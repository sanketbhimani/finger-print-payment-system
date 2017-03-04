# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

def keyboard_value():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(2, GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(20,GPIO.OUT)
    GPIO.setup(21,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(23,GPIO.OUT)
    value=[['1','2','3','A'],
           ['4','5','6','B'],
           ['7','8','9','C'],
           ['*','0','#','D']]
    row=[21,20,18,23]
    col=[2,3,4,17]
    
    for n in range(4):
        GPIO.output(row[n],True)

    while(True):
        
        for m in range(4):
##            time.sleep(0.05)
            GPIO.output(row[m],False)
            for i in range(4):
                if GPIO.input(col[i]) == 0:
                    ##print value[m][i]
                    while GPIO.input(col[i]) == 0:
                        pass
                    return value[m][i]
            GPIO.output(row[m],True)
<<<<<<< HEAD
#while 1:
 #   k = keyboard_value()
  #  print k
=======
<<<<<<< HEAD
##while 1:
##    k = keyboard_value()
##    print k
=======

>>>>>>> e83d3e93573a883f466bccd4f1a1410d1f72c728
>>>>>>> 4cea4ae5945e3310c96d77bc52ff75e1da540fac
