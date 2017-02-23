import functions
import functions as f
import keyboard
import time


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
    k=keyboard.keyboard_value()
    return k


#f.delete_all_ids()

def scan_finger():
    f.start_led()
    flg = 0
    if(f.start_enroll(f.current_count())==1):
        print 'press your finger 1st time'
        time.sleep(0.5)
        while (True):
            if(f.ispressfinger() == 1):
                if(f.capture_image() == 1):
                    if(f.enroll1()==1):
                        flg = 1
                        break;
                    else:
                        scan_finger()
                        
                
        time.sleep(0.5)
        print 'press your finger 2nd time'
        time.sleep(0.5)
        while(flg == 1):
            flg = 0
            while(True):
                if(f.ispressfinger() == 1):
                    if(f.capture_image() == 1):
                        if(f.enroll2()==1):
                            flg = 1
                            break;
                        else:
                            scan_finger()
                            
                
        time.sleep(0.5)
        print 'press your finger 3rd time'
        time.sleep(0.5)
        while(flg == 1):
            flg = 0
            while(True):
                if(f.ispressfinger() == 1):
                    if(f.capture_image() == 1):
                        if(f.enroll3()==1):
                            flg = 1
                            break;
                        else:
                            scan_finger()
        if(flg == 1):
            print 'bravoooooooooooooooooooooo :)'
            flg = 0
    f.stop_led()
def main():
   
    k=mode_select()
    amount=5000
    
    if (k=='1'):
        scan_finger()
    if (k== '2'):
        print 'put your finger'
        varify_finger()
        time.sleep(3)
        functions.capture_image()
        j=functions.identify()
        if(j==785):
            print "finger not found try again"
        
        else:
           ans=payment()
           amount=amount-ans
           print amount


main();
