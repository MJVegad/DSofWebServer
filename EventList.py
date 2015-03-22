#from heapq import heappush, heappop
import heapq
import Event

class EventList:
	"""docstring for EventList"""
	eventList = []

	def enqueueEvent(self, event):
		heapq.heappush(self.eventList, event)
#		self.eventList.append(event)
#		self.eventList = heapq.heapify(self.eventList, self.cmpFunction)
	def dequeueEvent(self):
		return heapq.heappop(self.eventList)
	def __lt__(self, event):
		#print ('comparison')
		return self.timestamp < event.timestamp

#	def cmpFunction(event1, event2):
		#print ('comparison')
#		return event1.timestamp < event2.timestamp