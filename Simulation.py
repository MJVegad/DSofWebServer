import math, System, Event, EventList

class Simulation:
	"""To begin and keep track of simulation"""
	def __init__(self, sizeOfBuffer, numberOfCores, numberOfThreads, timeQuantum, contextSwitchTime, cores, eventList, requestsList):
		self.eventList = eventList
		self.simulationTime = 0
		self.system = System(sizeOfBuffer, numberOfCores, numberOfThreads, timeQuantum, contextSwitchTime)
		self.requestList = requestslist

    def getCoreIdFromThreadId(self,threadId):
		return threadId%self.system.numberOfCores     	


	def arrivalEventHandler(self, event):
		availableThreadId = self.system.threadPool.getFreeThreadId()
		request = requestlist[event.id] 

		if (availableThreadId == -1):
			request.setRequestState(2)  #2-buffered 
			self.system.buffer.addToBuffer(request)
		else:
			coreId = getCoreIdFromThreadId(availableThreadId)
			self.system.threadPool.allocateThread(event.id, coreId, availableThreadId)


			if(self.system.cores[coreId].coreState == 0):     #0 - idle	
		 		self.system.cores[coreId].coreState = 1       #1 - busy	
		 		request.setRequestState(1)      #1 - executing 
		 		if((request.remainingServiceTime) < self.system.timeQuantum):
		 			newEvent = Event(self.simulationTime + request.remainingServiceTime, 1, coreId)
		 			EventList.enqueueEvent(newEvent)
		 		else:
		 			newEvent = Event(self.simulationTime + timeQuantum ,2, coreId)
		 			EventList.enqueueEvent(newEvent)
		 	else:
		 		request.requestState = 3         #3 - inCoreQueue              
		 		self.system.cores[coreId].enqueueRequest(request)	




