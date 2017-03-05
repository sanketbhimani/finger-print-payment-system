'''
* Project Name: 	e-Money transfer using fingertip through IOT device
* Author List:	 	Sanket Bhimani, Keyur Rakholiya , Earnest vekariya
* Filename: 		functions.py 
* Functions: 		start() , start_led() ,stop_led() , delete_all_ids() ,capture_image() ,current_count() ,start_enroll() ,
			enroll1() ,enroll2() ,enroll3() ,identify() , delete_id() ,ispressfinger()
* Global Variables:	No global variables.
'''



import struct			#improting python structure library
import serial			#importing serial library
import time
import itertools

_time = 0.1

s = serial.Serial('/dev/ttyAMA0',9600)    #syntax for serial communication


'''
function name: start()
#input:no input
#output:acknowldge from the sensor for successfull execution
#logic:sending the byte array of 12 bytes through UART to the sensor and decoding the data from the sensor according
to data sheet
#example call:functions.start()
'''

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

'''
function name: start_led()
#input:no input
#output:acknowldge from the sensor for successfull execution
#logic:sending the byte array of 12 bytes through UART to the sensor and decoding the data from the sensor according
to data sheet
#example call:functions.start_led()
'''	
	
	
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


	
	
'''
function name: stop_led()
#input:no input
#output:acknowldge from the sensor for successfull execution
#logic:sending the byte array of 12 bytes through UART to the sensor and decoding the data from the sensor according
to data sheet
#example call:functions.stop_led()
'''
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

'''
function name: delete_all_ids()
#input:no input
#output:acknowldge from the sensor for successfull execution
#logic:sending the byte array of 12 bytes through UART to the sensor and decoding the data from the sensor according
to data sheet
#example call:functions.delete_all_ids()
'''
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

'''
function name: capture_image()
#input:no input
#output:acknowldge from the sensor for successfull execution
#logic:sending the byte array of 12 bytes through UART to the sensor and decoding the data from the sensor according
to data sheet
#example call:functions.capture_image()
'''
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
'''
function name: current_count()
#input:no input
#output:acknowldge from the sensor for successfull execution and also total number of enrollment performed on the sensor
#logic:sending the byte array of 12 bytes through UART to the sensor and deccoding if there is any error in recived data
#example call:functions.current_count()
'''
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

'''
function name: start_enroll()
#input:the id at which enrollment will be performed
#output:acknowldge from the sensor for successfull execution
#logic:sending the byte array of 12 bytes through UART to the sensor and decoding the data from the sensor according
to data sheet
#example call:functions.start_enroll(34)
'''
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

'''
function name: enroll1()
#input:no input
#output:acknowldge from the sensor for successfull execution
#logic:sending the byte array of 12 bytes through UART to the sensor and decoding the data from the sensor according
to data sheet
#example call:functions.enroll1()
'''
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

'''
function name: enroll2()
#input:no input
#output:acknowldge from the sensor for successfull execution
#logic:sending the byte array of 12 bytes through UART to the sensor and decoding the data from the sensor according
to data sheet
#example call:functions.enroll2()
'''
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

'''
function name: enroll3()
#input:no input
#output:acknowldge from the sensor for successfull execution
#logic:sending the byte array of 12 bytes through UART to the sensor and decoding the data from the sensor according
to data sheet
#example call:functions.enroll3()
'''
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


'''
function name: identify()
#input:no input
#output:acknowldge from the sensor for successfull execution
#logic:sending the byte array of 12 bytes through UART to the sensor and decoding the data from the sensor according
to data sheet
#example call:functions.identify()
'''
def identify():  #function for identifyinhg the finger of user
        r=""	#string for reading data from string
        b=""	#string for storing the read data
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X51,0X00,0X51,0X01])	#serial syntax
        time.sleep(_time)
        
        while s.in_waiting:		#waiting untill serial output is not recived
                r = s.read();		#reading serial data
                b = b + r		#storing serial data
        res = [c for c in b]
        if(len(res) != 12):		#varify if obtain output has 12 character or not
                print "tryagain"
                return identify()	#call the function again if there is error
        if res[8].encode("hex") == '30':	#'30' indicates successfull execution of command
                print "Identify id: ", res[4].encode("hex"), res[5].encode("hex")
		print "Successful :)"
                return res[4].encode("hex")
        elif res[8].encode("hex") == '31': #'31' indicates unsuccessfull executin of command 
		
		if res[4].encode("hex") == '08':
			print "does not match any finger"
			return 785
                print "Identify Error :("
                print [elem.encode("hex") for elem in res]
                return 785
        else:
                print [elem.encode("hex") for elem in res]
                return identify()
'''
function name: delete_id()
#input:input id which you want to delete
#output:acknowldge from the sensor for successfull execution
#logic:sending the byte array of 12 bytes through UART to the sensor and decoding the data from the sensor according
to data sheet
#example call:functions.delete_id(4)
'''
def delete_id(id):	#function for delete id of user
        r=""		#string for reading data from string
        b=""		#string for storing the read data
        
        cmd = [0x55,0xAA,0X01,0X00,0x00,0X00,0X00,0X00,0X40,0X00,0X40,0X01]
        cmd[4] = int(id,16)
        chk_sum = int('0x55',16) + int('0xAA',16) + int('0x01',16) + int('0x40',16) + int(id,16)
        high = int(hex(chk_sum >> 8),16)
        low = int(hex(chk_sum & 0xFF),16)
        cmd[10] = low
        cmd[11] = high
        s.write(cmd)
        time.sleep(_time)
        
        while s.in_waiting:		#varify if obtain output has 12 character or not
                r = s.read();		#reading serial data
                b = b + r		#storing serial data
        res = [c for c in b]
        if(len(res) != 12):		#varify if obtain output has 12 character or not
#                print "tryagain"
                return delete_id(id)	#call the function again if there is error
        if res[8].encode("hex") == '30':	#'30' indicates successfull execution of command

                print "delete id ",id
                print "Successful :)"
                return 1
        elif res[8].encode("hex") == '31':	#'31' indicates unsuccessfull execution of command
                print "delete id ",id
		print "Error :("
                print [elem.encode("hex") for elem in res]
                return -1
        else:
                return delete_id(id)
'''
function name: ispressfinger()
#input:no input
#output:acknowldge from the sensor for successfull execution and also reponse if finger is pressed or not
#logic:sending the byte array of 12 bytes through UART to the sensor and decoding the data from the sensor according
to data sheet
#example call:functions.ispressfinger()
'''
def ispressfinger():		#function for delete id of user
        r=""			#string for reading data
        b=""			#string for storing data
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X26,0X00,0X26,0X01]) #serial syntax
        time.sleep(_time)
        
        while s.in_waiting:	#varify if obtain output has 12 character or not
                r = s.read();	#reading serial data
                b = b + r	#storing serial data
        res = [c for c in b]
        if(len(res) != 12):	#varify if obtain output has 12 character or not
                return ispressfinger()	#call the function again if there is error
        if res[8].encode("hex") == '30':	#'30' indicates successfull execution of command
		if res[4].encode("hex") == '00':
			return 1
		else:
			return 2
        elif res[8].encode("hex") == '31':	#'31' indicates successfull execution of command
                print "is press finger Error :("
                print [elem.encode("hex") for elem in res]
                return -1
        else:
                return ispressfinger()



