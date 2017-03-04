import struct
import serial
import time
import itertools

_time = 0.1

s = serial.Serial('/dev/ttyAMA0',9600)    #syntax for serial communication

def start():			# function for starting finger print sensor
	r=""			#string for reading the serial data
	b=""			#string for storing all the read serial data
	s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X01,0X00,0X01,0X01])  #serial syntax for starting the sensor
	time.sleep(_time)
        while s.in_waiting:			#wait untill serial data is recived
                r = s.read();			#reading serial data
                b = b + r			#storing the data
        res = [c for c in b]
	if(len(res) != 12):			#varify if string of 12 character is recived in ouyput	
		
		return start()                  #if proper response is not available then send the data again
        if res[8].encode("hex") == '30':	#'30' indicates function is excecuted successfully by the sensor
                print "start sensor Successful :)"
		return 1
        elif res[8].encode("hex") == '31':	#'31' indicates function is not successfully executed by the sensor
                print "start sensor Error :("
                print [elem.encode("hex") for elem in res]
		return -1
	else:
                return start()

def start_led():		# function for starting the C-mos led of finger print sensor
	r=""			#string for reading the serial data
	b=""			#string for storing all the read serial data
	
	s.write([0x55,0xAA,0X01,0X00,0X01,0X00,0X00,0X00,0X12,0X00,0X13,0X01])	 #serial syntax 
	time.sleep(_time)
	while s.in_waiting:		#varify if string of 12 character is recived in ouyput	
		r = s.read();		#reading serial data
		b = b + r		#storing the data
	res = [c for c in b]
        if(len(res) != 12):		#varify if string of 12 character is recived in ouyput	
 #               print "tryagain"
                return start_led()	#proper response is not available then send the data again
	if res[8].encode("hex") == '30':	#'30' indicates function is excecuted successfully by the sensor
		print "start led Successful :)"
		return 1
	elif res[8].encode("hex") == '31':	#'31' indicates function is not successfully executed by the sensor
		print "start led Error :("
		print [elem.encode("hex") for elem in res]
		return -1
	else:
                return start_led()

def stop_led():		#function for stop led
        r=""		#string for reading the serial data
        b=""		#string for storing all the read serial data
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X12,0X00,0X12,0X01])		#serial syntax	
        time.sleep(_time)
        
        while s.in_waiting:			#varify if string of 12 character is recived in ouyput	
                r = s.read();			#reading serial data
                b = b + r			#storing the data
        res = [c for c in b]
        if(len(res) != 12):			#varify if string of 12 character is recived in ouyput
#                print "tryagain"
                return stop_led()		#proper response is not available then send the data again
        if res[8].encode("hex") == '30':	#'30' indicates function is excecuted successfully by the sensor
                print "stop led Successful :)"
		return 1
        elif res[8].encode("hex") == '31':	#'31' indicates function is not successfully executed by the sensor
                print "stop led Error :("
                print [elem.encode("hex") for elem in res]
		return -1
	else:
                return stop_led()

def delete_all_ids():		# function for DELETE_ALL_IDS()
	r=""			#string for reading the serial data
 	b=""			#string for storing all the read serial data
 	
	s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X41,0X00,0X41,0X01])		#serial syntax	
        time.sleep(_time)
        
        time.sleep(3)
        while s.in_waiting:		#varify if string of 12 character is recived in ouyput	
                r = s.read();		#reading serial data
                b = b + r		#storing the data
        res = [c for c in b]
        if(len(res)!= 12):		#varify if string of 12 character is recived in ouyput
#                print "try again"
                return delete_all_ids()		#proper response is not available then send the data again
        if res[8].encode("hex") == '30':	#'30' indicates function is excecuted successfully by the sensor
                print "delete all ids Successful :)"
		return 1
        elif res[8].encode("hex") == '31':	#'31' indicates function is not successfully executed by the sensor
                print "delete all ids Error :("
                print [elem.encode("hex") for elem in res]
		return -1
	else:
                return delete_all_ids()


def capture_image():		# function for capture_image
        r=""			#string for reading the serial data
        b=""			#string for storing all the read serial data
        
	s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X60,0X00,0X60,0X01])		#serial syntax
        time.sleep(_time)
        
        while s.in_waiting:		#varify if string of 12 character is recived in ouyput
                r = s.read();		#reading serial data
                b = b + r		#storing the data
	res = [c for c in b]
        if(len(res) != 12):		#varify if string of 12 character is recived in ouyput
#                print "tryagain"
                return capture_image()	#proper response is not available then send the data again
	if res[8].encode("hex") == '30':	#'30' indicates function is excecuted successfully by the sensor
                print "capture image Successful :)"
		return 1
        elif res[8].encode("hex") == '31':	#'31' indicates function is not successfully executed by the sensor
                print "capture image Error :("
                print [elem.encode("hex") for elem in res]
		return -1
	else:
                return capture_image()

#returns count in string format Ex. '06' for 6 count
def current_count():		# function for current_count
	r=""			#string for reading the serial data
        b=""			#string for storing all the read serial data
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X20,0X00,0X20,0X01])		#serial syntax
        time.sleep(_time)
        
        while s.in_waiting:		#varify if string of 12 character is recived in ouyput
                r = s.read();		#reading serial data
                b = b + r		#storing the data
        res = [c for c in b]
        if(len(res) != 12):		#varify if string of 12 character is recived in ouyput
#                print "tryagain"
                return current_count()		#proper response is not available then send the data again
        if res[8].encode("hex") == '30':	#'30' indicates function is excecuted successfully by the sensor
		
                print "currant count",res[4].encode("hex")
		print "Successful :)"
                return res[4].encode("hex")
        elif res[8].encode("hex") == '31':	#'31' indicates function is not successfully executed by the sensor
                print "currant count Error :("
                print [elem.encode("hex") for elem in res]
                return -1
        else:
                return current_count()


#accepts id in string format Ex '06'  for 6 id
def start_enroll(id):		# function for start_enroll
        r=""			#string for reading the serial data
        b=""			#string for storing all the read serial data
        
	cmd = [0x55,0xAA,0X01,0X00,0x00,0X00,0X00,0X00,0X22,0X00,0X22,0X01]		
	cmd[4] = int(id,16)
	chk_sum = int('0x55',16) + int('0xAA',16) + int('0x01',16) + int('0x22',16) + int('0x'+id,16)
	high = int(hex(chk_sum >> 8),16)
	low = int(hex(chk_sum & 0xFF),16)
	cmd[10] = low
	cmd[11] = high
        s.write(cmd)
        time.sleep(_time)
        
        while s.in_waiting:	#varify if string of 12 character is recived in ouyput
                r = s.read();
                b = b + r
        res = [c for c in b]
        if(len(res) != 12):		#proper response is not available then send the data again
#                print "tryagain"	#'30' indicates function is excecuted successfully by the sensor
                return start_enroll(id)
        if res[8].encode("hex") == '30':

                print "start enroll for id ",id
                print "Successful :)"
                return 1
        elif res[8].encode("hex") == '31':	#'31' indicates function is not successfully executed by the sensor
                print "start enroll for id "
		print "Error :("
                print [elem.encode("hex") for elem in res]
                return -1
        else:
                return start_enroll(id)

#return 1 for successfull
#return 2 for finger not pressed
#return 3 for invalid order
def enroll1():			# function for enrolling finger print
        r=""			#string for reading the serial data
        b=""			#string for storing all the read serial data
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X23,0X00,0X23,0X01])  
        time.sleep(_time)
        
        while s.in_waiting:
                r = s.read();
                b = b + r
        res = [c for c in b]
        if(len(res) != 12):		#varify if string of 12 character is recived in ouyput
                print "tryagain"
                return enroll1()
        if res[8].encode("hex") == '30':		#'30' indicates function is excecuted successfully by the sensor	
                print "Enroll 1 Successful :)"
                return 1
        elif res[8].encode("hex") == '31':		#'31' indicates function is not successfully executed by the sensor
		if res[4].encode("hex") == '12':
			print "finger not press Enroll 1  Error :("
			return 0
		elif res[4].encode("hex") == '0b' or res[4].encode("hex") == '0B':
			print "invalid enrollment order Enroll 1 Error :("
			return 1
                print "Enroll 1 Error :("
                print [elem.encode("hex") for elem in res]
                return 0
        else:
                return enroll1()


def enroll2():		# function for enrolling second finger-print
        r=""		#string for reading the serial data
        b=""		#string for storing all the read serial data
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X24,0X00,0X24,0X01])
        time.sleep(_time)
        
        while s.in_waiting:
                r = s.read();
                b = b + r
        res = [c for c in b]
        if(len(res) != 12):			#varify if string of 12 character is recived in ouyput
                print "tryagain"
                return enroll2()
        if res[8].encode("hex") == '30':	#'30' indicates function is excecuted successfully by the sensor
                print "Enroll 2 Successful :)"
                return 1
        elif res[8].encode("hex") == '31':	#'31' indicates function is not successfully executed by the sensor
                if res[4].encode("hex") == '12':
                        print "finger not press Enroll 2 Error :("
                        return 0
                elif res[4].encode("hex") == '0b' or res[4].encode("hex") == '0B':
                        print "invalid enrollment order Enroll 2 Error :("
                        return 1
                print "Enroll 2 Error :("
                print [elem.encode("hex") for elem in res]
                return 0
        else:
                return enroll2()

#return 1 for successfull
#return 2 for finger not pressed
#return 3 for invalid order
def enroll3():			#enroll function
        r=""			#string for storing the read serial data
        b=""			#string for storing the read serial data
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X25,0X00,0X25,0X01]) #serial syntax
        time.sleep(_time)
        
        while s.in_waiting:		#wait untill output is recived to controller
                r = s.read();		#reading the data
                b = b + r		#storing the data
        res = [c for c in b]
        if(len(res) != 12):		#varify if 12 bits are recived in string
                print "tryagain"
                return enroll3()	#call function again if proper string is not recived
        if res[8].encode("hex") == '30':	#'30' indicates program has executed successfully by finger print sensor
                print "Enroll 3 Successful :)"
                return 1
        elif res[8].encode("hex") == '31':	#'31' indicates if function is not executed successfully by finger print sensor 
                if res[5].encode("hex") == '00':
                        print "id already exists: ",res[5].encode("hex")
                        print [elem.encode("hex") for elem in res]
			print "Enroll 3 Error :("
                        return 0
                elif res[4].encode("hex") == '0b' or res[4].encode("hex") == '0B':
                        print "invalid enrollment order Enoll 3 Error :("
                        print [elem.encode("hex") for elem in res]
                        return 1
                print "Enroll 3 Error :("
                print [elem.encode("hex") for elem in res]
                return 0
        else:
                return enroll3()


#returns id in string format Ex. '06' for 6 count
#return -2 for does not match any finger
def identify():
        r=""
        b=""
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X51,0X00,0X51,0X01])
        time.sleep(_time)
        
        while s.in_waiting:
                r = s.read();
                b = b + r
        res = [c for c in b]
        if(len(res) != 12):
                print "tryagain"
                return identify()
        if res[8].encode("hex") == '30':
                print "Identify id: ", res[4].encode("hex"), res[5].encode("hex")
		print "Successful :)"
                return res[4].encode("hex")
        elif res[8].encode("hex") == '31':
		
		if res[4].encode("hex") == '08':
			print "does not match any finger"
			return 785
                print "Identify Error :("
                print [elem.encode("hex") for elem in res]
                return 785
        else:
                print [elem.encode("hex") for elem in res]
                return identify()



#accepts id in hex
def delete_id(id):
        r=""
        b=""
        
        cmd = [0x55,0xAA,0X01,0X00,0x00,0X00,0X00,0X00,0X40,0X00,0X40,0X01]
        cmd[4] = int(id,16)
        chk_sum = int('0x55',16) + int('0xAA',16) + int('0x01',16) + int('0x40',16) + int(id,16)
        high = int(hex(chk_sum >> 8),16)
        low = int(hex(chk_sum & 0xFF),16)
        cmd[10] = low
        cmd[11] = high
        s.write(cmd)
        time.sleep(_time)
        
        while s.in_waiting:
                r = s.read();
                b = b + r
        res = [c for c in b]
        if(len(res) != 12):
#                print "tryagain"
                return delete_id(id)
        if res[8].encode("hex") == '30':

                print "delete id ",id
                print "Successful :)"
                return 1
        elif res[8].encode("hex") == '31':
                print "delete id ",id
		print "Error :("
                print [elem.encode("hex") for elem in res]
                return -1
        else:
                return delete_id(id)

def ispressfinger():
        r=""
        b=""
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X26,0X00,0X26,0X01])
        time.sleep(_time)
        
        while s.in_waiting:
                r = s.read();
                b = b + r
        res = [c for c in b]
        if(len(res) != 12):
#                print "tryagain"
                return ispressfinger()
        if res[8].encode("hex") == '30':
#                print "is press finger Successful :)"
		if res[4].encode("hex") == '00':
#			print "finger press"
			return 1
		else:
#			print "finger not press"
			return 2
        elif res[8].encode("hex") == '31':
                print "is press finger Error :("
                print [elem.encode("hex") for elem in res]
                return -1
        else:
                return ispressfinger()


####
####start()
####start_led()
##delete_all_ids()
####capture_image()
####identify()
##start()
##start_led()
##start_enroll('01')
###delete_all_ids()
##capture_image()
##enroll1()
##capture_image()
##enroll2()
##capture_image()
##enroll3()
##stop_led()
##current_count()
