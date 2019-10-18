from threading import Thread
import time
import lcm
from Communication import message_t

lc = lcm.LCM()


	
class heartbeat_Init(Thread):
	def __init__(self):
		Thread.__init__(self)
		self.prev_time = time.time()
		self.msg = message_t()
		self.Object_Detected = False
		
	def run(self):
		while True:
			self.msg.timestamp = int(time.time() * 1000000)
			if self.Object_Detected == False:
				
				if time.time() - self.prev_time >1:
					self.msg.danger = False
					self.prev_time = time.time()
					lc.publish("Obstacle", self.msg.encode())
			else:
				self.msg.danger = True
				lc.publish("Obstacle", self.msg.encode())
				
			
