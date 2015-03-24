#from heapq import heappush, heappop
import heapq, queue
import Event

class EventList:
	"""docstring for EventList"""
	eventList = queue.PriorityQueue()


	def enqueueEvent(self, event):
		EventList.eventList.put((event.timestamp, event.eventType, event.eventId))

	def dequeueEvent(self):
		tuple=EventList.eventList.get()
		event=Event.Event(tuple[0],tuple[1],tuple[2])
		return event





