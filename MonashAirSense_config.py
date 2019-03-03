#Choose which file to be used as each sensor.
from sensors import pm_g5st as pm_sensor
# import th_htu21d as tmp_sensor
from sensors import gas_tvoc_sgp30 as gas_sensor
# import pyupm_i2clcd as upmLCD

# Choose to enable particular sensors.
# True for enabled or False for disabled.
Pm_Sense_Enabled = True                          
Tmp_Sense_Enabled = False
Light_Sense_Enabled = False
Gas_Sense_Enabled = False
Disp_Enabled = False


GPS_LAT = 25.1933
GPS_LON = 121.7870
APP_ID = "MonashAirSense"
DEVICE_ID = "DEVICE_ID1234"
DEVICE = "LINKIT 4822"

""" MQTT SETTINGS """
MQTT_broker = 'm13.cloudmqtt.com'
MQTT_port = 12504                  
MQTT_topic = 'datastream'
MQTT_interval = 10			# interval between every two MQTT messages (seconds)
MQTT_auth = {'username':"bheazjan", 'password':"Zj8TLcRab1Wt"}
Reboot_Time = 86400			# interval to reboot (seconds); 0 for no-rebooting

FS_SD = "/mnt/mmcblk0p1" #SD CARD LOCATION- Note this may be deprecated

#Device Main Process Update Interval - to lower CPU usage and reduce overheating
Main_Proc_Update_Interval = 1 #seconds

#################################
# The following code must not be changed!

import uuid
import re
from multiprocessing import Queue

float_re_pattern = re.compile("^-?\d+\.\d+$")                                                                                               
num_re_pattern = re.compile("^-?\d+\.\d+$|^-?\d+$")

mac = str(':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])).upper()
DEVICE_ID = mac.replace(':','')                                                                           

pm_q = Queue()                                                                                                                     
tmp_q = Queue()                                                                                                                     
light_q = Queue()                                                                                                                   
gas_q = Queue()  
tvoc_q = Queue()

 #Define the shared variable values initial state. 
                                           
values = {"meta":
                {      "app"           :       APP_ID,
                "version"       :       "1.0.0", #App version
                "device_id"     :       DEVICE_ID,                  
                "device"        :       DEVICE,                                           
                "gps_lat"       :       GPS_LAT,                    
                "gps_lon"       :       GPS_LON,                     
                "date"          :       "1900-01-01",                        
                "time"          :       "00:00:00",                          
                } 
        }                      
