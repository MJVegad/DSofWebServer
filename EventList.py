from heapq import heappush, heappop
import Event

class EventList:
	"""docstring for EventList"""
	def __init__(self):
		self.eventList = []

	def enqueueEvent(self, event):
		self.eventList.append(event)

	def dequeueEvent(self):
		self.eventList.sort(key=lambda x: x.timestamp, reverse=True)
		event = self.eventList[1]
		self.eventList = self.eventList[2:]
		return event