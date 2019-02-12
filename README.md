
# Monash Air Sense Client
This is the Monash Air Sense project, the client side application for real time detection of Air Quality metrics, that are subsequently reported to a central server at , the AnySense Server, via MQTT. Central to the operation of the project is MediaTek LinkIt 7688 board.

## Sensors supported (As of August 2018)
* Particulate Matter Sensor
  * Plantower PMS5003ST (UART0)
* Gas Sensor
  * SenseAir S8 (UART1)
  * Sensirion SGP30 (I2C)
* RTC: real time clock
  * DS3231 (I2C)

## Dependancies:
* Python 2.7.X- Python 3 will be supported in the future.
  * To check use python --version
* MRAA Python Library, included in the LinkIt 7688 board, but may also work with other       MRAA-supported platforms.
* Paho MQTT,a python library for communication over MQTT (Message Queuing Telemetry Transport).

## How to run this program?
Login to your development board, and change (`cd`) to your working directory.

1. Clone the latest version of the code repository:
   ```
   git clone https://github.com/kierenpinto/MonashAirSense.git
   ```
   NOTE: It is important to do this in the /root/ directory of the MediaTek device running OpenWrt.

2. Install paho library using the pip package manager.
   ```
   pip install paho-mqtt
   ```

3. Edit the file MonashAirSense_config.py to configure the system. You can enable and disable various features. Use either `True` or `False` boolean values to enable or disable respectively.
   * Sense_PM: Enable PM sensor
   * Sense_Tmp: Enable Temperature/Humidity sensor
   * Sense_Light: Enable Light sensor
   * Sense_Gas: Enable Gas sensor
   * Use_RTC_DS3231: Enable RTC (DS3231)
   ***
   * The import statements can be used to choose which module to use specific to each sensor. This is unlikely to be changed.
      * import xxx as yyy: Change xxx to the corresponding module (or leave it unchanged if you don't need a PM sensor)
    ***
   * GPS coordinates: including GPS_LAT and GPS_LON
   * MQTT settings: including MQTT_broker, MQTT_port, MQTT_topic, MQTT_auth and MQTT_interval
   * Restful settings: including Restful_URL and Restful_interval
  
4. Run the main program by
   ```
   python MonashAirSense.py
   ```
   <br/>
   It is important to place the MonashAirSense directory in the ' /root/ 'directory
   <br/>

5. You can check the results on the console printouts or on the MQTT broker.

6. Start-up application. (Service) On OpenWrt linux machines follow these instructions.
  <br/> Edit ```/etc/rc.local``` file in a text editor and add:
    ```
    /root/MonashAirSense/RUN start
    ```
  <br/> For more information visit (https://docs.onion.io/omega2-docs/running-a-command-on-boot.html)
# Reset WiFi Authentication
At some point you may have to put the device LinkIt 7688 from AP mode back to Station mode. To do this,
first press the MCU button to restart the device. The WiFi light will come on, and stay on while the system boots. Once this has finished it will turn off and begin to flash. At this point, hold down the WiFi button for 5 seconds but less than 20 seconds. The devices should change to Station Mode and will be accesible directly on its own WiFi network. 
### Note:
<br/>
The install.sh script will be completed in the future to streamline this process.
## Acknowledgements
This project was forked and modified from the [AnySense Project](https://github.com/cclljj/AnySense_7688)
