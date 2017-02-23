import struct
import serial
import time
import itertools

_time = 0.1

s = serial.Serial('/dev/ttyAMA0',9600)

def start():
	r=""
	b=""
	s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X01,0X00,0X01,0X01])
	time.sleep(_time)
        while s.in_waiting:
                r = s.read();
                b = b + r
        res = [c for c in b]
	if(len(res) != 12):
#		print "tryagain"
		return start()
        if res[8].encode("hex") == '30':
                print "start sensor Successful :)"
		return 1
        elif res[8].encode("hex") == '31':
                print "start sensor Error :("
                print [elem.encode("hex") for elem in res]
		return -1
	else:
                return start()

def start_led():
	r=""
	b=""
	
	s.write([0x55,0xAA,0X01,0X00,0X01,0X00,0X00,0X00,0X12,0X00,0X13,0X01])
	time.sleep(_time)
	while s.in_waiting:
		r = s.read();
		b = b + r
	res = [c for c in b]
        if(len(res) != 12):
 #               print "tryagain"
                return start_led()
	if res[8].encode("hex") == '30':
		print "start led Successful :)"
		return 1
	elif res[8].encode("hex") == '31':
		print "start led Error :("
		print [elem.encode("hex") for elem in res]
		return -1
	else:
                return start_led()

def stop_led():
        r=""
        b=""
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X12,0X00,0X12,0X01])
        time.sleep(_time)
        
        while s.in_waiting:
                r = s.read();
                b = b + r
        res = [c for c in b]
        if(len(res) != 12):
#                print "tryagain"
                return stop_led()
        if res[8].encode("hex") == '30':
                print "stop led Successful :)"
		return 1
        elif res[8].encode("hex") == '31':
                print "stop led Error :("
                print [elem.encode("hex") for elem in res]
		return -1
	else:
                return stop_led()

def delete_all_ids():
	r=""
 	b=""
 	
	s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X41,0X00,0X41,0X01])
        time.sleep(_time)
        
        time.sleep(3)
        while s.in_waiting:
                r = s.read();
                b = b + r
        res = [c for c in b]
        if(len(res)!= 12):
#                print "try again"
                return delete_all_ids()
        if res[8].encode("hex") == '30':
                print "delete all ids Successful :)"
		return 1
        elif res[8].encode("hex") == '31':
                print "delete all ids Error :("
                print [elem.encode("hex") for elem in res]
		return -1
	else:
                return delete_all_ids()


def capture_image():
        r=""
        b=""
        
	s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X60,0X00,0X60,0X01])
        time.sleep(_time)
        
        while s.in_waiting:
                r = s.read();
                b = b + r
	res = [c for c in b]
        if(len(res) != 12):
#                print "tryagain"
                return capture_image()
	if res[8].encode("hex") == '30':
                print "capture image Successful :)"
		return 1
        elif res[8].encode("hex") == '31':
                print "capture image Error :("
                print [elem.encode("hex") for elem in res]
		return -1
	else:
                return capture_image()

#returns count in string format Ex. '06' for 6 count
def current_count():
	r=""
        b=""
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X20,0X00,0X20,0X01])
        time.sleep(_time)
        
        while s.in_waiting:
                r = s.read();
                b = b + r
        res = [c for c in b]
        if(len(res) != 12):
#                print "tryagain"
                return current_count()
        if res[8].encode("hex") == '30':
		
                print "currant count",res[4].encode("hex")
		print "Successful :)"
                return res[4].encode("hex")
        elif res[8].encode("hex") == '31':
                print "currant count Error :("
                print [elem.encode("hex") for elem in res]
                return -1
        else:
                return current_count()


#accepts id in string format Ex '06'  for 6 id
def start_enroll(id):
        r=""
        b=""
        
	cmd = [0x55,0xAA,0X01,0X00,0x00,0X00,0X00,0X00,0X22,0X00,0X22,0X01]
	cmd[4] = int(id,16)
	chk_sum = int('0x55',16) + int('0xAA',16) + int('0x01',16) + int('0x22',16) + int('0x'+id,16)
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
                return start_enroll(id)
        if res[8].encode("hex") == '30':

                print "start enroll for id ",id
                print "Successful :)"
                return 1
        elif res[8].encode("hex") == '31':
                print "start enroll for id ",id
		print "Error :("
                print [elem.encode("hex") for elem in res]
                return -1
        else:
                return start_enroll(id)

#return 1 for successfull
#return 2 for finger not pressed
#return 3 for invalid order
def enroll1():
        r=""
        b=""
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X23,0X00,0X23,0X01])
        time.sleep(_time)
        
        while s.in_waiting:
                r = s.read();
                b = b + r
        res = [c for c in b]
        if(len(res) != 12):
                print "tryagain"
                return enroll1()
        if res[8].encode("hex") == '30':
                print "Enroll 1 Successful :)"
                return 1
        elif res[8].encode("hex") == '31':
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

#return 1 for successfull
#return 2 for finger not pressed
#return 3 for invalid order
def enroll2():
        r=""
        b=""
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X24,0X00,0X24,0X01])
        time.sleep(_time)
        
        while s.in_waiting:
                r = s.read();
                b = b + r
        res = [c for c in b]
        if(len(res) != 12):
                print "tryagain"
                return enroll2()
        if res[8].encode("hex") == '30':
                print "Enroll 2 Successful :)"
                return 1
        elif res[8].encode("hex") == '31':
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
def enroll3():
        r=""
        b=""
        
        s.write([0x55,0xAA,0X01,0X00,0X00,0X00,0X00,0X00,0X25,0X00,0X25,0X01])
        time.sleep(_time)
        
        while s.in_waiting:
                r = s.read();
                b = b + r
        res = [c for c in b]
        if(len(res) != 12):
                print "tryagain"
                return enroll3()
        if res[8].encode("hex") == '30':
                print "Enroll 3 Successful :)"
                return 1
        elif res[8].encode("hex") == '31':
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
