'''
* Project Name: 	e-Money transfer using fingertip through IOT device
* Author List:	 	Sanket Bhimani, Keyur Rakholiya , Earnest vekariya
* Filename: 		scan_finger.py (main file from which all the function are called)
* Functions: 		payment();mode_select();varify()
* Global Variables:	No global variables.
'''






import urllib2
import functions as f
import time
import keyboard
import time
import lcd as Lprint
import pygame


import lcd as Lprint 

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
num=[]
ammount = [] #to save ammount 
global amount  #glabal variable for storing the amount



'''
function name:payment()
input:none
output:return amount entered by the user through keypad
logic:converting the character obtain from keypad function into integer and storing it in integer variable
function call:payment()
'''


def payment():
    ans=0	#variable for storing the amount enter by user through keypad
    k=keyboard.keyboard_value()  #call the function to obtain key pressed by the user on keypad
    while(k!='A'):	
        j=int(k);	#convert the character into integer
        print j		
        ans=ans*10 + j	#storing the entered amount in the variable
        k=keyboard.keyboard_value()	#call the function to obtain key pressed by the user on keypad
    print ans
    return ans


'''
function name:mode_select()
input:none
output: return the selected mode by the user  
logic:converting the character obtain from keypad function into integer and storing it in integer variable
function call:mode_select()
'''


def mode_select() :
    print "select number"
    print "1)new user"
    print "2)withdraw money"
    Lprint.lcd_string("press 1)new user",LCD_LINE_1)   #syntax for printing on lcd screen
    Lprint.lcd_string("press 2)payment",LCD_LINE_2)	 #syntax for printing on lcd screen
    k=keyboard.keyboard_value()
    return k


'''
function name:scan_finger()
input:none
output:return acknowledgement of successfull image scan by the user if not then show the error message on lcd
logic:converting the character obtain from keypad function into integer and storing it in integer variable
function call:scan_finger()
'''
def scan_finger():
    f.start()		#function to start the sensor
    f.start_led()	#function to start the led


    current_id = int(f.current_count(),16)


    f.start_enroll(f.current_count())	#function for starting enrollment for storing the finger-print of user 
    Lprint.lcd_byte(0x01, LCD_CMD)  #clear lcd
    Lprint.lcd_string("put your finger",LCD_LINE_1)	 #syntax for printing on lcd screen
    print 'press finger 1'
    while(f.ispressfinger()==2):	#check if finger is pressed or not
        time.sleep(0.1)
    if(f.capture_image() == 1):		#capture image
        if(f.enroll1() == 1):	#check if successfull enrollment of user has done or not
            print 'remove finger 1'
            Lprint.lcd_string("remove your finger",LCD_LINE_1)	 #syntax for printing on lcd screen
            while(f.ispressfinger()==1):	#check if finger is pressed or not
                time.sleep(0.1)
            print 'press finger 2'
            Lprint.lcd_string("put your finger again",LCD_LINE_1)	 #syntax for printing on lcd screen
            while(f.ispressfinger()==2):	#check if finger is pressed or not
                time.sleep(0.1)
            if(f.capture_image() == 1):	#capture image
                if(f.enroll2() == 1):	#check if successfull enrollment of user has done or not
                    print 'remove finger 2'
                    Lprint.lcd_string("remove your finger",LCD_LINE_1)	 #syntax for printing on lcd screen
                    while(f.ispressfinger()==1):	#check if finger is pressed or not
                        time.sleep(0.1)
                    print 'press finger 3'
                    Lprint.lcd_string("put your finger again",LCD_LINE_1)	 #syntax for printing on lcd screen
                    while(f.ispressfinger()==2): #check if finger is pressed or not
                        time.sleep(0.1)
                    if(f.capture_image() == 1):	#capture image
                        if(f.enroll3() == 1):	#check if successfull enrollment of user has done or not
                            print 'remove finger 3'
                            Lprint.lcd_string("successfull scanned:)",LCD_LINE_1)	 #syntax for printing on lcd screen
                            time.sleep(1)
                            Lprint.lcd_string("enter your mobile no",LCD_LINE_1)	#syntax for printing on lcd screen

                            val1=''
                            val = ''
                            number = 0

                            while (val != 'D'):
                                Lprint.lcd_string("then Press D ",LCD_LINE_2)	 #syntax for printing on lcd screen
                                val = keyboard.keyboard_value()		#calling the function to read the key pressed by the user on keypad
                                time.sleep(0.05)
                                val1=val1+val
                                if(val == 'C'):		#cancel command
                                    val1 = ''
                                    val = ''
                                    number = 0
                                    Lprint.lcd_string("enter again",LCD_LINE_1)	 #syntax for printing on lcd screen
                                    time.sleep(1.5)
                                elif(val != 'D'):	#varify end of mobile numer
                                    temp=int(val)
                                    number=number*10+temp	#store the number in variable
                                    Lprint.lcd_string(val1,LCD_LINE_1)
                            

                            Lprint.lcd_byte(0x01, LCD_CMD)
                            Lprint.lcd_string("thank you..",LCD_LINE_1) #syntax for printing on lcd screen
                            time.sleep(1)
                            Lprint.lcd_byte(0x01, LCD_CMD)
                            Lprint.lcd_string("check sms in",LCD_LINE_1)	 #syntax for printing on lcd screen
                            Lprint.lcd_string("your mobile",LCD_LINE_2)		 #syntax for printing on lcd screen
                            time.sleep(2)
                            '''
                                send req. to server....
                                send Current_id and number
                            '''
			    
			    url = "http://malgadi.co.in/touch-n-pay/register_new_user.php?fid="+str(current_id)+"&mobileno="+str(number)
			    content = urllib2.urlopen(url).read()	#syntax to update the web server
			    if(content == '1'):
                                Lprint.lcd_string("registered successfully",LCD_LINE_1)	 #syntax for printing on lcd screen
                                time.sleep(2)
                                '''if internet is not working then delete id if not upload on portal'''
	    			    


                            
                            while(f.ispressfinger()==1):	#syntax if finger id pressed or not
                                time.sleep(0.1)


                            for i in range(0,10):	# to store 10 digit mobile number
                                val = keyboard.keyboard_value()

                            val1=''
                            for i in range(0,10):
                                val = keyboard.keyboard_value()
                                val1=val1+val	#to store number in string
                                Lprint.lcd_string(val1,LCD_LINE_2)

                                num.insert(i,val)
                                print num[i]
                            Lprint.lcd_string("check message in",LCD_LINE_1)	 #syntax for printing on lcd screen
                            Lprint.lcd_string("your phone",LCD_LINE_2)	 #syntax for printing on lcd screen
                            time.sleep(2)
                            userid = f.current_count() # userid is in 'hex' format, covert it in decimal and minus 1
                            
                            print 'user id is:'
                            print userid 
                            '''
                                send req. to server....
                                send userid and num array
                            '''
                            while(f.ispressfinger()==1):
                                time.sleep(0.1)


                        else:
                            Lprint.lcd_string("enroll 3 fail",LCD_LINE_1)	 #syntax for printing error message on lcd screen
                            Lprint.lcd_string("please try again",LCD_LINE_2)	 #syntax for printing on lcd screen
                            time.sleep(2)
                    else:
                        Lprint.lcd_string("3rd capture fail",LCD_LINE_1)	 #syntax for printing error message on lcd screen
                        Lprint.lcd_string("please try again",LCD_LINE_2)	 #syntax for printing on lcd screen
                        time.sleep(2)
                else:
                    Lprint.lcd_string("enroll 2 fail",LCD_LINE_1)	 #syntax for printing error message on lcd screen
                    Lprint.lcd_string("please try again",LCD_LINE_2)	 #syntax for printing on lcd screen
                    time.sleep(2)
            else:
                 Lprint.lcd_string("2nd capture fail",LCD_LINE_1)	 #syntax for printing error message on lcd screen
                 Lprint.lcd_string("please try again",LCD_LINE_2)	 #syntax for printing error message on lcd screen
                 time.sleep(2)
        else:
            Lprint.lcd_string("enroll 1 fail",LCD_LINE_1)	 #syntax for printing error message on lcd screen
            Lprint.lcd_string("please try again",LCD_LINE_2)	 #syntax for printing error message on lcd screen
            time.sleep(2)
    else:
        Lprint.lcd_string("1st capture fail",LCD_LINE_1)	 #syntax for printing error message on lcd screen
        Lprint.lcd_string("please try again",LCD_LINE_2)	 #syntax for printing error message on lcd screen
        time.sleep(2)                   

    f.stop_led()
'''
function name:varify()
input:none
output:find the user who have enroll thier finger print and return the id of the user & return error message if
user not found
logic:This function find the user id from database and calls the payment mode function for the payment of money
and after that it updates the database
function call:varify()
'''
def verify():
    f.start_led()		#call the function to start the led of finger-print sensor
    print 'press finger'
    Lprint.lcd_byte(0x01, LCD_CMD) 	
    Lprint.lcd_string("press finger..",LCD_LINE_1)	 #syntax for printing on lcd screen
    while(f.ispressfinger()==2):	#varify if finger is pressed or not
        time.sleep(0.1)
    if(f.capture_image() == 1):		#varify if image is captured successfully

        detected_id = f.identify()	#to store the id of the user
        
        if(detected_id != 785):			#syntax if proper id is obtained
             detected_id = int(detected_id,16)
             print 'remove finger'		
             Lprint.lcd_byte(0x01, LCD_CMD) 
             Lprint.lcd_string("enter ammount ",LCD_LINE_1)	 #syntax for printing on lcd screen
             val = ''
             val1 = 'ammount'
             ammount = 0
             while(val != 'D'):
                 val = keyboard.keyboard_value()  #function for reading the switch press by the user in keypad
                 time.sleep(0.05)
                 val1=val1+val     		#storing the amount in string
                 Lprint.lcd_string("Press D ",LCD_LINE_2)	 #syntax for printing on lcd screen
                 if(val == 'c'):        #varify cancel command
                     val = ''
                     val1 = 'ammount'    
                     ammount = 0
                     Lprint.lcd_string("enter again",LCD_LINE_1)	 #syntax for printing on lcd screen
                     time.sleep(1.5)
                     
                 elif(val != 'D'):			#press d for exiting
                     temp=int(val)
                     ammount=ammount*10+temp		#store the amount entered by the user in string
                     Lprint.lcd_string(val1,LCD_LINE_1)


        detectedid = f.identify()     #store the id of detected user finger print in the variable
        if(detectedid != 785):
             print 'remove finger'
             Lprint.lcd_byte(0x01, LCD_CMD) 
             Lprint.lcd_string("enter ammount ",LCD_LINE_1)	 #syntax for printing on lcd screen

             val = keyboard.keyboard_value()
             i=0
             while(val != 'D'):
                 ammount.insert(i,val)
                 i = i +1
                 Lprint.lcd_byte(0x01, LCD_CMD) 
                 Lprint.lcd_string("press D ",LCD_LINE_2)	 #syntax for printing on lcd screen
                 val = keyboard.keyboard_value()

             val = ''
             i=0
             val_string = 'ammount:'
             Lprint.lcd_string(" then press D ",LCD_LINE_2)	 #syntax for printing on lcd screen
             while(val != 'D'):
                 ammount.insert(i,val)
                 i = i +1
                 val = keyboard.keyboard_value()
                 val_string = val_string + val
                 Lprint.lcd_string(val_string,LCD_LINE_1)   #print the string on lcd


             Lprint.lcd_byte(0x01, LCD_CMD) 
             Lprint.lcd_string("sending data... ",LCD_LINE_1)	 #syntax for printing on lcd screen
            
             '''
                detected id and ammount send to server
                1) success remaining balance display and message
                2) insufficinet balance and message
            
             '''
	     url = "http://malgadi.co.in/touch-n-pay/do_payment.php?fid="+str(detected_id)+"&cost="+str(ammount)
	     print 'response from website'
	     
             content = urllib2.urlopen(url).read()
             print content
             Lprint.lcd_byte(0x01, LCD_CMD) 
             Lprint.lcd_string("enter ammount ",LCD_LINE_1)	 #syntax for printing on lcd screen
             
	     if content == '1':
                 Lprint.lcd_string("payment successfull",LCD_LINE_1)	 #syntax for printing on lcd screen
                 time.sleep(1.5)
             if content == '2':
                 Lprint.lcd_string("insufficent",LCD_LINE_1)	 #syntax for printing on lcd screen
                 Lprint.lcd_string("balance",LCD_LINE_2)	 #syntax for printing on lcd screen
                 time.sleep(1.5)

        else:
            Lprint.lcd_byte(0x01, LCD_CMD) 
            Lprint.lcd_string("user not found",LCD_LINE_1)	 #syntax for printing on lcd screen
            time.sleep(2)
            
    else:       
        Lprint.lcd_byte(0x01, LCD_CMD) 
        Lprint.lcd_string("sorry....",LCD_LINE_1)	 #syntax for printing on lcd screen
        Lprint.lcd_string("try again",LCD_LINE_2)	 #syntax for printing on lcd screen
        time.sleep(2)
           
    f.stop_led()

def main(): 
    while(1):
        k = mode_select()  #selecting mode for :1)new user 2)payment
        if(k == '1'):	#for enrollment of new user finger print
            scan_finger()	#function used to store the finger print of the user
        if(k=='2'):	#mode selection for payment
            y = verify()	#store the id of the user in the variable
        if(k == '#'):
            '''
            send req. to server to update the database
            press #
            '''
            Lprint.lcd_byte(0x01, LCD_CMD) 
            Lprint.lcd_string("database updated..",LCD_LINE_1)	 #syntax for printing on lcd screen
            time.sleep(2)
            

Lprint.lcd_init()    
main()


