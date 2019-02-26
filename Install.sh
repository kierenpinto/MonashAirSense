#Installation Script

#Place startup script in /etc/rc.local as 
#       /root/MonashAirSense/RUN Start
# or.... $this directory/RUN Start

pip install paho-mqtt
/root/MonashAirSense/RUN Start >> /etc/rc.local
