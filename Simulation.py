import math, System

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

		if (availableThreadId == -1):
			request = requestlist[event.id] 
			request.setRequestState(2)  #2-buffered 
			self.system.buffer.addToBuffer(request)
		else:
			coreId = getCoreIdFromThreadId(availableThreadId)
			self.system.threadPool.allocateThread(event.id, coreId, availableThreadId)


			if(self.system.cores[coreId].coreState == 0):     #0 - idle	
		 		self.system.cores[coreId].coreState = 1       #1 - busy	
		 		requestlist[event.id].setRequestState(1)      #1 - executing 

