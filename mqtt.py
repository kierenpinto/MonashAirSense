import paho.mqtt.publish as publish
import paho.mqtt.client as mqttclient

class mqtt:
	def __init__(self, MQTT_broker, MQTT_port, MQTT_topic,MQTT_auth):
		self.host = MQTT_broker
		self.port = MQTT_port
		self.topic = MQTT_topic
		self.auth = MQTT_auth

		#Use this for more frequent messages
		self.client_instance = mqttclient.Client()
		self.client_instance.username_pw_set(self.auth['username'],self.auth['password'])
		self.client_instance.connect(self.host,self.port)
	
	def pub(self, data):
		try:
			#Infrequent Messages:
			# publish.single(self.topic, data, hostname=self.host, port = self.port, auth=self.auth)
			
			#Frequent Messages
			self.client_instance.publish(self.topic,data)
		except:
			print('Send Error !')

		


