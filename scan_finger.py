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
                            for i in range(0,10):
                                val = keyboard.keyboard_value()
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
    f.stop_led()

def verify():
    f.start_led()
    print 'press finger'
    Lprint.lcd_byte(0x01, LCD_CMD) 
    Lprint.lcd_string("press finger..",LCD_LINE_1)
    while(f.ispressfinger()==2):
        time.sleep(0.1)
    if(f.capture_image() == 1):
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
             Lprint.lcd_byte(0x01, LCD_CMD) 
             Lprint.lcd_string("sending data... ",LCD_LINE_1)
            
             '''
                detected id and ammount send to server
                1) success remaining balance display and message
                2) insufficinet balance and message
            
             '''
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
