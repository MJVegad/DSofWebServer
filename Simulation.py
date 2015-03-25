import math, System, Event, EventList, Request, RequestList, Client

class Simulation:
	"""To begin and keep track of simulation"""


	def __init__(self, sizeOfBuffer, timeout, numberOfThreads, numberOfCores, timeQuantum, contextSwitchTime, numberOfClients, arrivalTimeDistributionLambda, thinkTimeDistribution, serviceTimeDistribution, paramThinkTime1, paramServiceTime1, paramThinkTime2=None, paramServiceTime2=None):
		self.eventList = EventList.EventList()
		self.simulationTime = 0
		self.clients = []

		for y in list(range(numberOfClients)):
			self.clients.append(Client.Client(y, thinkTimeDistribution, paramThinkTime1, 0, paramThinkTime2))        #0 - thinking

		self.requestList = RequestList.RequestList()
		
		for index in list(range(numberOfClients)):
			if serviceTimeDistribution == 1 or serviceTimeDistribution == 2: # Uniform or Normal distribution
				request = Request.Request(index, arrivalTimeDistributionLambda, serviceTimeDistribution, timeout, paramServiceTime1, paramServiceTime2)
			else:
				request = Request.Request(index, arrivalTimeDistributionLambda, serviceTimeDistribution, timeout, paramServiceTime1)
			
			self.requestList.addToRequestList(request)
			#print (self.requestList.requestList[index].arrivalTime)
			newEvent = Event.Event(self.simulationTime + request.arrivalTime, 0, request.requestId)
			self.eventList.enqueueEvent(newEvent)
			newEvent1 = Event.Event(self.simulationTime + request.arrivalTime + request.timeout, 4, request.requestId)        #4 - timeout
			self.eventList.enqueueEvent(newEvent1)

		self.system = System.System(sizeOfBuffer, numberOfCores, numberOfThreads, timeQuantum, contextSwitchTime)

	def getCoreIdFromThreadId(self,threadId):
		if threadId is None:
			return -1
		else:
			return (threadId % self.system.numberOfCores)

	def getRequestFromEvent(self, event):
		#print (list(range(event.eventId)))
		for x in list(range(len(self.requestList.requestList))):

			if (self.requestList.requestList[x].requestId == event.eventId):
				request = self.requestList.requestList[x]
				return request
			else:
				pass
				#break
		#return request
	

	def arrivalEventHandler(self, event):
		availableThreadId = self.system.threadPool.getFreeThreadId()
		request = self.getRequestFromEvent(event)

		if request is not None:
			if (availableThreadId == -1 or availableThreadId == None):
				request.setRequestState(2)  #2-buffered
				self.system.buffer.addToBuffer(request)
			else:
				request.threadId = availableThreadId
				coreId = self.getCoreIdFromThreadId(availableThreadId)
				print ('************'+ str(availableThreadId))
				self.system.threadPool.allocateThread()

				if(self.system.cores[coreId].coreState == 0):     #0 - idle
					self.system.cores[coreId].coreState = 1       #1 - busy
					request.setRequestState(1)      #1 - executing
					if((request.remainingServiceTime) <= self.system.timeQuantum):
						newEvent = Event.Event(self.simulationTime + request.remainingServiceTime, 1, request.requestId)
						self.eventList.enqueueEvent(newEvent)
					else:
						newEvent = Event.Event(self.simulationTime + self.system.timeQuantum , 2, request.requestId)
						self.eventList.enqueueEvent(newEvent)
				else:
					request.setRequestState(3)         #3 - inCoreQueue
					self.system.cores[coreId].enqueueRequest(request)
					print ('request ' + str(request.requestId) + ' enqueued in ' + str(coreId) + ' core')


	def quantamExpiredEventHandler(self, event):
		# 	get core id
		#   get request object
		#   add request object in core queue
		request = self.getRequestFromEvent(event)
		request.remainingServiceTime = request.remainingServiceTime - self.system.timeQuantum
		coreId = self.getCoreIdFromThreadId(request.threadId)
		self.system.cores[coreId].enqueueRequest(request)
		print ('request ' + str(request.requestId) + 'enqueued in ' + str(coreId) + ' core')
		request.setRequestState(3)                  #3 - inCoreQueue
		nextEvent = Event.Event(self.simulationTime + self.system.contextSwitchTime, 3, coreId)
		self.eventList.enqueueEvent(nextEvent)

	def departureEventHandler(self, event):

		for x in range(len(self.requestList.requestList)):
			if (self.requestList.requestList[x].requestId == event.eventId):
				request = self.requestList.requestList[x]
				self.requestList.requestList = self.requestList.requestList[:x] + self.requestList.requestList[x+1:]
				break

		print ('Departure EH : thread Id ' + str(request.threadId))
		self.system.threadPool.freeThread(request.threadId)
		client = self.clients[request.clientId]
		client.clientStatus = 0   #0 - thinking

		if(client.paramThinkTime2 is None):
			client.thinkTime = client.getThinkTime(client.thinkTimeDistribution, client.paramThinkTime1)
		else:
			client.thinkTime = client.getThinkTime(client.thinkTimeDistribution, client.paramThinkTime1, client.paramThinkTime2)

		if(self.system.cores[self.getCoreIdFromThreadId(request.threadId)].queuedRequestsList.empty()):
			self.system.cores[self.getCoreIdFromThreadId(request.threadId)].coreState = 0        #0 - idle
		else:
			scheduleNextEvent = Event.Event(self.simulationTime + self.system.contextSwitchTime, 3, self.getCoreIdFromThreadId(request.threadId))
			self.eventList.enqueueEvent(scheduleNextEvent)

		newRequest = Request.Request(request.clientId, request.arrivalTimeDistributionLambda, request.serviceTimeDistribution, request.param1, request.timeout, request.param2)
		self.requestList.addToRequestList(newRequest)
		newEvent = Event.Event(self.simulationTime + client.thinkTime, 0, newRequest.requestId)
		self.eventList.enqueueEvent(newEvent)
		newEvent1 = Event.Event(self.simulationTime + client.thinkTime + newRequest.timeout, 4, newRequest.requestId)        #4 - timeout
		self.eventList.enqueueEvent(newEvent1)

		if(self.system.buffer.requestsInBuffer):
			requestFromBuffer = self.system.buffer.removeFromBuffer()
			newEvent = Event.Event(self.simulationTime, 0, requestFromBuffer.requestId)
			self.eventList.enqueueEvent(newEvent)

	def scheduleNextRequestEventHandler(self, event):
		# get coreId on which next request is to be scheduled
		coreId = event.eventId
		#print ('====================>'+str(self.system.cores[coreId].queuedRequestsList[0].requestId))

		if (not self.system.cores[coreId].queuedRequestsList.empty()):
			print('dequeueing request with core id : ' + str(self.system.cores[coreId].queuedRequestsList.qsize()))
			dequedRequest = self.system.cores[coreId].dequeueRequest()
			print ('Schedule Next Request EH Request Id : '+ str(dequedRequest.requestId))
			dequedRequest.setRequestState(1)		#1 - executing
			if dequedRequest.remainingServiceTime <= self.system.timeQuantum :
				departureEvent = Event.Event(self.simulationTime + dequedRequest.remainingServiceTime, 1, dequedRequest.requestId)
				self.eventList.enqueueEvent(departureEvent)
			else :
				quantamExpiredEvent = Event.Event(self.simulationTime + self.system.timeQuantum, 1, dequedRequest.requestId)
				self.eventList.enqueueEvent(quantamExpiredEvent)

	def printLogMessages(self, time, requestId, eventType):
		print (str(time)+'	'+ str(requestId)+'	'+str(eventType))



	def timeoutEventHandler(self, event):
		request = self.getRequestFromEvent(event)
		if request is not None:
			self.printLogMessages(self.simulationTime, event.eventId,'clientTimeout')
			newRequest = Request.Request(request.clientId, request.arrivalTimeDistributionLambda, request.serviceTimeDistribution, request.param1, request.timeout, request.param2)
			self.requestList.addToRequestList(newRequest)
			newEvent = Event.Event(self.simulationTime, 0, newRequest.requestId)
			self.eventList.enqueueEvent(newEvent)
			newEvent1 = Event.Event(self.simulationTime + newRequest.timeout, 4, newRequest.requestId)
			self.eventList.enqueueEvent(newEvent1)


