import mraa
import mqtt
import time
import string
import os
import json
from reports import Report
from threading import Timer
from datetime import datetime


import MonashAirSense_config as Conf

# fields = Conf.fields #Initiate shared variable
values = Conf.values #Initiate shared variable
timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
local_report = Report('/root',timestamp[0],timestamp[1])

def upload_data():
	#After upload_data is first run, it is run again at the specified interval
	Timer(Conf.MQTT_interval,upload_data,()).start()

	#Formats and sends data over MQTT
	timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
	pairs = timestamp.split(" ")
	values["meta"]["date"] = pairs[0] #Date
	values["meta"]["time"] = pairs[1] #Time
	values["meta"]["timestamp"] = time.time()
	msg = json.dumps(values) #Convert to JSON for sending to server.
	#Initiate and send MQTT
	MQTT = mqtt.mqtt(Conf.MQTT_broker,Conf.MQTT_port,Conf.MQTT_topic + "/" + Conf.DEVICE_ID,Conf.MQTT_auth)
	MQTT.pub(msg)
	local_report.addEvent(values)
	local_report.save()
	print 'published and saved'
	if 's_d0' in values:
		print 'data ' + str(values["s_d0"])


def display_data(disp):
	Timer(5, display_data, {disp}).start()
	timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
	pairs = timestamp.split(" ")
	empty_str = "                    "
        disp.setCursor(0,0)                                                                
	disp.write(empty_str)
        disp.setCursor(0,0)                                                                
	disp.write("ID: " + Conf.DEVICE_ID)
        disp.setCursor(1,0)                                                                
	disp.write(empty_str)
        disp.setCursor(1,0)                                                                
	disp.write("Date: " + pairs[0])
        disp.setCursor(2,0)                                                                
	disp.write(empty_str)
        disp.setCursor(2,0)                                                                
	disp.write("Time: " + pairs[1])
        disp.setCursor(3,0)                                                                
	disp.write(empty_str)
        disp.setCursor(3,0)                                                                
        disp.write('Temp = %.2f' % values["s_t0"])                                           
        disp.setCursor(4,0)                                                                
	disp.write(empty_str)
        disp.setCursor(4,0)                                                                
        disp.write('rH = %.2f' % values["s_h0"])
        disp.setCursor(5,0)                                                                
	disp.write(empty_str)
        disp.setCursor(5,0)                                                                
        disp.write('PM2.5 = %d' % values["s_d0"])                                             
        disp.setCursor(6,0)                                                                
	disp.write(empty_str)
        disp.setCursor(6,0)                                                                
        disp.write('TVOC = %d' % values["s_gg"])

def reboot_system():
	os.system("reboot")


def main():
	if Conf.Reboot_Time > 0:
		Timer(Conf.Reboot_Time, reboot_system,()).start()

	#Check if sensors are enabled in configuration. If they are, initiate them.
	if Conf.Pm_Sense_Enabled:
		pm_data = '1'
		pm = Conf.pm_sensor.sensor(Conf.pm_q) #Pass in the queue
		pm.start()
	# if Conf.Tmp_Sense_Enabled:
	# 	tmp_data = '2'
	# 	tmp = Conf.tmp_sensor.sensor(Conf.tmp_q)
	# 	tmp.start()
	# 	tmp_data = {'Tmp':0.0, 'RH':0}
	# if Conf.Gas_Sense_Enabled:
	# 	gas_data = '4'
	# 	gas = Conf.gas_sensor.sensor(Conf.gas_q)
	# 	gas.start()
	# if Conf.Disp_Enabled:
	# 	disp = Conf.upmLCD.SSD1306(0, 0x3C)
	# 	disp.clear()
	print('upload first run')
	upload_data()

	# display_data(disp)
	interval = Conf.Main_Proc_Update_Interval
	start_time = 0
	end_time = 0
	while True:
		start_time = time.time()
		if Conf.Pm_Sense_Enabled and not Conf.pm_q.empty():
			while not Conf.pm_q.empty(): # This makes sure we're not behind in the queue.
				pm_data = Conf.pm_q.get()
			values["payload"]['PM']=dict()
			for item in pm_data: #Goes through each piece of data output
				if Conf.float_re_pattern.match(str(pm_data[item])):
					values["payload"]['PM'][str(item)]= round(float(pm_data[item]),2)
				else:
					values["payload"]['PM'][str(item)] = pm_data[item]
		
		# if Conf.Tmp_Sense_Enabled and not Conf.tmp_q.empty():
		# 	while not Conf.tmp_q.empty():
		# 		tmp_data = Conf.tmp_q.get()
                #         for item in tmp_data:                                                                 
                #                 if item in fields:                                                                
                #                         values[fields[item]] = tmp_data[item]                                     
		# 			if Conf.float_re_pattern.match(str(values[fields[item]])):
		# 				values[fields[item]] = round(float(values[fields[item]]),2)
                #                 else:                                                                             
                #                         values[item] = tmp_data[item]                                          
		# if Conf.Gas_Sense_Enabled and not Conf.gas_q.empty():
		# 	while not Conf.gas_q.empty():
		# 		gas_data = Conf.gas_q.get()
                #         for item in gas_data:                                                                 
                #                 if item in fields:                                                                
                #                         values[fields[item]] = gas_data[item]                                     
		# 			if Conf.float_re_pattern.match(str(values[fields[item]])):
		# 				values[fields[item]] = round(float(values[fields[item]]),2)
                #                 else:                                                                             
                #                         values[item] = gas_data[item]
		end_time = time.time()
		time.sleep(max(0,interval-(start_time-end_time)))
if __name__ == '__main__':
        main()                                    

