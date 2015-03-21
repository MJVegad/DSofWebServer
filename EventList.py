from heapq import heappush, heappop
import Event

class EventList:
	"""docstring for EventList"""
	def __init__(self, arg):
		self.eventList = []
	def enqueEvent(self, event):
		heapq.heappush(self.eventList, event)
	def dequeEvent(self):
		return heapq.heappop(self.eventList)
	def __lt__(self, event):
		return self.timestamp < event.timestamp