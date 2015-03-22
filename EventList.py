#from heapq import heappush, heappop
import heapq
import Event

class EventList:
	"""docstring for EventList"""

	def __init__(self):
		self.eventList = []

	def enqueueEvent(self, event):
		self.eventList.append(event)

	def dequeueEvent(self):
		self.eventList.sort(key=lambda x: x.timestamp)
		event = self.eventList[0]
		self.eventList = self.eventList[1:]
		return event