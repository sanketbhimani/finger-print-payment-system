# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

def keyboard_value():           #function for reading keyboard input
    GPIO.setmode(GPIO.BCM)      #initialize board as bcm
    GPIO.setwarnings(False)
    GPIO.setup(2, GPIO.IN,pull_up_down=GPIO.PUD_UP)   #initialization of pin as input
    GPIO.setup(3,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #initialization of pin  as input
    GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #initialization of pin  as input
    GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #initialization of pin as input
    GPIO.setup(20,GPIO.OUT) #initialization of pin as output
    GPIO.setup(21,GPIO.OUT) #initialization of pin as output
    GPIO.setup(18,GPIO.OUT) #initialization of pin as output
    GPIO.setup(23,GPIO.OUT) #initialization of pin as output
    value=[['1','2','3','A'],  #keypad array for output
           ['4','5','6','B'],
           ['7','8','9','C'],
           ['*','0','#','D']]
    row=[21,20,18,23]  #controller pin connected to row of keypad
    col=[2,3,4,17]     #controller pin connected to column of keypad 
    
    for n in range(4):  #initialize all the output pin with high logic
        GPIO.output(row[n],True)

    while(True):            #loop will execute untill it finds which row and column are selected by press key
        
        for m in range(4):
##            time.sleep(0.05)
            GPIO.output(row[m],False)
            for i in range(4):
                if GPIO.input(col[i]) == 0:
                    ##print value[m][i]
                    while GPIO.input(col[i]) == 0:
                        pass
                    return value[m][i]      #return the press key value
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
