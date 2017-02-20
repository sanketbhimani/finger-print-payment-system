import functions
import keyboard
import time



##start_enroll(k)
##print 'put finger'
##time.sleep(3)
##
##
##capture_image()
##enroll1()
##capture_image()
##enroll2()
##capture_image()
##enroll3()
##
##stop_led()
##
##
##time.sleep(5)
##
##start_led()
##capture_image()
##identify()
##stop_led()

#while True:
 #   k = keyboard.keyboard_value()
 #   print k
global amount
def payment():
    ans=0
    k=keyboard.keyboard_value()
    while(k!='A'):
        ans=ans*10 + k
        k=keyboard.keyboard_value()
    amount=amount-ans
def mode_select() :
    print "select number"
    print "1)new user"
    print "2)withdraw money"
    k=keyboard.keyboard_value()
    return k
##
##functions.start_led()
##functions.delete_all_ids()
k = functions.current_count()
print k

functions.start()
k=mode_select()
amount=5000

if (k=='1'):
    
    functions.start_led()
    count=functions.current_count()
    print count
    functions.start_enroll(count)
    print 'put finger'
    time.sleep(3)
    functions.capture_image()
    if(functions.enroll1()):
        functions.capture_image()
        if(functions.enroll2()):
            functions.capture_image()
            if(functions.enroll3()):
                print 'bravooooooooo...!'
                

if (k== '2'):
    print 'put your finger'
    time.sleep(3)
    functions.capture_image()
    functions.identify()
    payment()
