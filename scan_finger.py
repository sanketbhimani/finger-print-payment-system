import urllib2
import functions as f
import time
import keyboard
import time
import lcd as Lprint 
LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False
num=[]
ammount = [] #to save ammount 
global amount
def payment():
    ans=0
    k=keyboard.keyboard_value()
    while(k!='A'):
        j=int(k);
        print j
        ans=ans*10 + j
        k=keyboard.keyboard_value()
    print ans
    return ans

def mode_select() :
    print "select number"
    print "1)new user"
    print "2)withdraw money"
    Lprint.lcd_string("press 1)new user",LCD_LINE_1)
    Lprint.lcd_string("press 2)payment",LCD_LINE_2)
    k=keyboard.keyboard_value()
    return k


def scan_finger():
    f.start()
    f.start_led()

    current_id = int(f.current_count(),16)

    f.start_enroll(f.current_count())
    Lprint.lcd_byte(0x01, LCD_CMD)  #clear lcd
    Lprint.lcd_string("put your finger",LCD_LINE_1)
    print 'press finger 1'
    while(f.ispressfinger()==2):
        time.sleep(0.1)
    if(f.capture_image() == 1):
        if(f.enroll1() == 1):
            print 'remove finger 1'
            Lprint.lcd_string("remove your finger",LCD_LINE_1)
            while(f.ispressfinger()==1):
                time.sleep(0.1)
            print 'press finger 2'
            Lprint.lcd_string("put your finger again",LCD_LINE_1)
            while(f.ispressfinger()==2):
                time.sleep(0.1)
            if(f.capture_image() == 1):
                if(f.enroll2() == 1):
                    print 'remove finger 2'
                    Lprint.lcd_string("remove your finger",LCD_LINE_1)
                    while(f.ispressfinger()==1):
                        time.sleep(0.1)
                    print 'press finger 3'
                    Lprint.lcd_string("put your finger again",LCD_LINE_1)
                    while(f.ispressfinger()==2):
                        time.sleep(0.1)
                    if(f.capture_image() == 1):
                        if(f.enroll3() == 1):
                            print 'remove finger 3'
                            Lprint.lcd_string("successfull scanned:)",LCD_LINE_1)
                            time.sleep(1)
                            Lprint.lcd_string("enter your mobile no",LCD_LINE_1)

                            val1=''
                            val = ''
                            number = 0

                            while (val != 'D'):
                                Lprint.lcd_string("then Press D ",LCD_LINE_2)
                                val = keyboard.keyboard_value()
                                time.sleep(0.05)
                                val1=val1+val
                                if(val == 'C'):
                                    val1 = ''
                                    val = ''
                                    number = 0
                                    Lprint.lcd_string("enter again",LCD_LINE_1)
                                    time.sleep(1.5)
                                elif(val != 'D'):
                                    temp=int(val)
                                    number=number*10+temp
                                    Lprint.lcd_string(val1,LCD_LINE_1)
                            
##                            temp1=Lprint.c_d_to_a(number)
##                            temp1="number is:"+temp1
##                            Lprint.lcd_string(temp1,LCD_LINE_2)
##                            time.sleep(2)
                            Lprint.lcd_byte(0x01, LCD_CMD)
                            Lprint.lcd_string("thank you..",LCD_LINE_1)
                            time.sleep(1)
                            Lprint.lcd_byte(0x01, LCD_CMD)
                            Lprint.lcd_string("check sms in",LCD_LINE_1)
                            Lprint.lcd_string("your mobile",LCD_LINE_2)
                            time.sleep(2)
                            '''
                                send req. to server....
                                send Current_id and number
                            '''
			    
			    url = "http://malgadi.co.in/touch-n-pay/register_new_user.php?fid="+str(current_id)+"&mobileno="+str(number)
			    content = urllib2.urlopen(url).read()
			    if(content == '1'):
                                Lprint.lcd_string("registered successfully",LCD_LINE_1)
                                time.sleep(2)
                                '''if internet is not working then delete id if not upload on portal'''
	    			    


                            
                            while(f.ispressfinger()==1):
                                time.sleep(0.1)

                            for i in range(0,10):
                                val = keyboard.keyboard_value()

                            val1=''
                            for i in range(0,10):
                                val = keyboard.keyboard_value()
                                val1=val1+val
                                Lprint.lcd_string(val1,LCD_LINE_2)

                                num.insert(i,val)
                                print num[i]
                            Lprint.lcd_string("check message in",LCD_LINE_1)
                            Lprint.lcd_string("your phone",LCD_LINE_2)
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
                            Lprint.lcd_string("enroll 3 fail",LCD_LINE_1)
                            Lprint.lcd_string("please try again",LCD_LINE_2)
                            time.sleep(2)
                    else:
                        Lprint.lcd_string("3rd capture fail",LCD_LINE_1)
                        Lprint.lcd_string("please try again",LCD_LINE_2)
                        time.sleep(2)
                else:
                    Lprint.lcd_string("enroll 2 fail",LCD_LINE_1)
                    Lprint.lcd_string("please try again",LCD_LINE_2)
                    time.sleep(2)
            else:
                 Lprint.lcd_string("2nd capture fail",LCD_LINE_1)
                 Lprint.lcd_string("please try again",LCD_LINE_2)
                 time.sleep(2)
        else:
            Lprint.lcd_string("enroll 1 fail",LCD_LINE_1)
            Lprint.lcd_string("please try again",LCD_LINE_2)
            time.sleep(2)
    else:
        Lprint.lcd_string("1st capture fail",LCD_LINE_1)
        Lprint.lcd_string("please try again",LCD_LINE_2)
        time.sleep(2)                   

    f.stop_led()

def verify():
    f.start_led()
    print 'press finger'
    Lprint.lcd_byte(0x01, LCD_CMD) 
    Lprint.lcd_string("press finger..",LCD_LINE_1)
    while(f.ispressfinger()==2):
        time.sleep(0.1)
    if(f.capture_image() == 1):

        detected_id = f.identify()
        
        if(detected_id != 785):
             detected_id = int(detected_id,16)
             print 'remove finger'
             Lprint.lcd_byte(0x01, LCD_CMD) 
             Lprint.lcd_string("enter ammount ",LCD_LINE_1)
             val = ''
             val1 = 'ammount'
             ammount = 0
             while(val != 'D'):
                 val = keyboard.keyboard_value()
                 time.sleep(0.05)
                 val1=val1+val
                 Lprint.lcd_string("Press D ",LCD_LINE_2)
                 if(val == 'c'):
                     val = ''
                     val1 = 'ammount'
                     ammount = 0
                     Lprint.lcd_string("enter again",LCD_LINE_1)
                     time.sleep(1.5)
                     
                 elif(val != 'D'):
                     temp=int(val)
                     ammount=ammount*10+temp
                     Lprint.lcd_string(val1,LCD_LINE_1)

        detectedid = f.identify()
        if(detectedid != 785):
             print 'remove finger'
             Lprint.lcd_byte(0x01, LCD_CMD) 
             Lprint.lcd_string("enter ammount ",LCD_LINE_1)

             val = keyboard.keyboard_value()
             i=0
             while(val != 'D'):
                 ammount.insert(i,val)
                 i = i +1
                 Lprint.lcd_byte(0x01, LCD_CMD) 
                 Lprint.lcd_string("press D ",LCD_LINE_2)
                 val = keyboard.keyboard_value()

             val = ''
             i=0
             val_string = 'ammount:'
             Lprint.lcd_string(" then press D ",LCD_LINE_2)
             while(val != 'D'):
                 ammount.insert(i,val)
                 i = i +1
                 val = keyboard.keyboard_value()
                 val_string = val_string + val
                 Lprint.lcd_string(val_string,LCD_LINE_1)

             Lprint.lcd_byte(0x01, LCD_CMD) 
             Lprint.lcd_string("sending data... ",LCD_LINE_1)
            
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
             Lprint.lcd_string("enter ammount ",LCD_LINE_1)
             
	     if content == '1':
                 Lprint.lcd_string("payment successfull",LCD_LINE_1)
                 time.sleep(1.5)
             if content == '2':
                 Lprint.lcd_string("insufficent",LCD_LINE_1)
                 Lprint.lcd_string("balance",LCD_LINE_2)
                 time.sleep(1.5)
        else:
            Lprint.lcd_byte(0x01, LCD_CMD) 
            Lprint.lcd_string("user not found",LCD_LINE_1)
            time.sleep(2)
            
    else:       
        Lprint.lcd_byte(0x01, LCD_CMD) 
        Lprint.lcd_string("sorry....",LCD_LINE_1)
        Lprint.lcd_string("try again",LCD_LINE_2)
        time.sleep(2)
           
    f.stop_led()

def main(): 
    while(1):
        k = mode_select()
        if(k == '1'):
            scan_finger()
        if(k=='2'):
            y = verify()
        if(k == '#'):
            '''
            send req. to server to update the database
            press #
            '''
            Lprint.lcd_byte(0x01, LCD_CMD) 
            Lprint.lcd_string("database updated..",LCD_LINE_1)
            time.sleep(2)
            
        
Lprint.lcd_init()    
main()

#f.delete_all_ids()
#scan_finger()
#f.current_count()
#verify()
