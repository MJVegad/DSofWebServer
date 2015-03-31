import math, System, Event, EventList, Request, RequestList, Client, random

class Simulation:
	"""To initiate and keep track of experiment's objects throughout simulation. It's members are,
		randomSeed : seed to generate different distribution values
		eventList : object of type EventList
		simulationTime : to synch with time(clock) during simulation
		clients : contains list of Client type objects, one for each client
		requestList : object of type RequestList
		system : object of type System
		departureCount : keep track of count of no. of events departed"""


	def __init__(self, sizeOfBuffer, timeout, numberOfThreads, numberOfCores, timeQuantum, contextSwitchTime, numberOfClients, randomSeed, arrivalTimeDistributionLambda, thinkTimeDistribution, serviceTimeDistribution, paramThinkTime1, paramServiceTime1, paramThinkTime2=None, paramServiceTime2=None):
		random.seed(randomSeed)
		self.eventList = EventList.EventList()
		self.simulationTime = 0
		self.departureCount = 0
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
			#schedule timeout of the request
			newEvent1 = Event.Event(self.simulationTime + request.arrivalTime + request.timeout, 4, request.requestId)        #4 - timeout
			self.eventList.enqueueEvent(newEvent1)

		self.system = System.System(sizeOfBuffer, numberOfCores, numberOfThreads, timeQuantum, contextSwitchTime)

	#to get core to schedule the thread, by threadId % numberOfCores
	def getCoreIdFromThreadId(self,threadId):
		if threadId is None:
			return -1
		else:
			return (threadId % self.system.numberOfCores)

	#to get request who generated the event
	def getRequestFromEvent(self, event):
		for x in list(range(len(self.requestList.requestList))):

			if (self.requestList.requestList[x].requestId == event.eventId):
				request = self.requestList.requestList[x]
				return request
			else:
				pass

	#to handle arrival events
	def arrivalEventHandler(self, event):
		availableThreadId = self.system.threadPool.getFreeThreadId()
		request = self.getRequestFromEvent(event)

		if request is not None:

			if (availableThreadId == -1 or availableThreadId == None):
				#if thread is not available, buffer the request
				request.setRequestState(2)
				self.system.buffer.addToBuffer(request, self.requestList)
			else:
				request.threadId = availableThreadId
				coreId = self.getCoreIdFromThreadId(availableThreadId)
				print ('************'+ str(availableThreadId))
				#allocate a thread to the request
				self.system.threadPool.allocateThread()


				if(self.system.cores[coreId].coreState == 0):
					#if core to be scheduled is free, execute the request on the core
					self.system.cores[coreId].coreState = 1
					request.setRequestState(1)
					if((request.remainingServiceTime) <= self.system.timeQuantum):
						#schedule departure of the request
						newEvent = Event.Event(self.simulationTime + request.remainingServiceTime, 1, request.requestId)
						self.eventList.enqueueEvent(newEvent)
					else:
						#schedule context switching of the request
						newEvent = Event.Event(self.simulationTime + self.system.timeQuantum , 2, request.requestId)
						self.eventList.enqueueEvent(newEvent)
				else:
					#put the request in core queue
					request.setRequestState(3)
					self.system.cores[coreId].enqueueRequest(request)
					print ('request ' + str(request.requestId) + ' enqueued in ' + str(coreId) + ' core')

	#to handle time quantum expired events of request
	def quantamExpiredEventHandler(self, event):
		request = self.getRequestFromEvent(event)
		request.remainingServiceTime = request.remainingServiceTime - self.system.timeQuantum
		#put current request into core queue
		coreId = self.getCoreIdFromThreadId(request.threadId)
		self.system.cores[coreId].enqueueRequest(request)
		print ('request ' + str(request.requestId) + 'enqueued in core' + str(coreId))
		request.setRequestState(3)
		#schedule next request from the queue
		nextEvent = Event.Event(self.simulationTime + self.system.contextSwitchTime, 3, coreId)
		self.eventList.enqueueEvent(nextEvent)

	#to handle departure of request
	def departureEventHandler(self, event):
		#remove request from requestList
		for x in range(len(self.requestList.requestList)):
			if (self.requestList.requestList[x].requestId == event.eventId):
				request = self.requestList.requestList[x]
				self.requestList.requestList = self.requestList.requestList[:x] + self.requestList.requestList[x+1:]
				break

        #increment departure count
		self.departureCount +=1
		print ('Departure EH : thread Id ' + str(request.threadId) +'|||||||| departurecount: ' + str(self.departureCount))
		#free the thread held by request
		self.system.threadPool.freeThread(request.threadId)
		#set the client state to thinking
		client = self.clients[request.clientId]
		client.clientStatus = 0   #0 - thinking

		#compute think time for the client
		if(client.paramThinkTime2 is None):
			client.thinkTime = client.getThinkTime(client.thinkTimeDistribution, client.paramThinkTime1)
		else:
			client.thinkTime = client.getThinkTime(client.thinkTimeDistribution, client.paramThinkTime1, client.paramThinkTime2)

		if(self.system.cores[self.getCoreIdFromThreadId(request.threadId)].queuedRequestsList.empty()):
			#set core state to free
			self.system.cores[self.getCoreIdFromThreadId(request.threadId)].coreState = 0        #0 - idle
		else:
			#schedule next request from core queue
			scheduleNextEvent = Event.Event(self.simulationTime + self.system.contextSwitchTime, 3, self.getCoreIdFromThreadId(request.threadId))
			self.eventList.enqueueEvent(scheduleNextEvent)

		#schedule new request from the client
		newRequest = Request.Request(request.clientId, request.arrivalTimeDistributionLambda, request.serviceTimeDistribution, request.param1, request.timeout, request.param2)
		self.requestList.addToRequestList(newRequest)
		newEvent = Event.Event(self.simulationTime + client.thinkTime, 0, newRequest.requestId)
		self.eventList.enqueueEvent(newEvent)
		#schedule timeout event
		newEvent1 = Event.Event(self.simulationTime + client.thinkTime + newRequest.timeout, 4, newRequest.requestId)        #4 - timeout
		self.eventList.enqueueEvent(newEvent1)

		if(self.system.buffer.requestsInBuffer):
			#schedule a request from buffer to get a thread
			requestFromBuffer = self.system.buffer.removeFromBuffer()
			newEvent = Event.Event(self.simulationTime, 0, requestFromBuffer.requestId)
			self.eventList.enqueueEvent(newEvent)

	#to handle scheduling of the request from core queue
	def scheduleNextRequestEventHandler(self, event):
		coreId = event.eventId

		if (not self.system.cores[coreId].queuedRequestsList.empty()):
			#get next request from RR core queue
			print('dequeueing request with core id : ' +str(coreId))
			dequedRequest = self.system.cores[coreId].dequeueRequest()
			print ('Schedule Next Request EH Request Id : '+ str(dequedRequest.requestId))
			dequedRequest.setRequestState(1)		#1 - executing
			if dequedRequest.remainingServiceTime <= self.system.timeQuantum :
				#schedule departure of the request
				departureEvent = Event.Event(self.simulationTime + dequedRequest.remainingServiceTime, 1, dequedRequest.requestId)
				self.eventList.enqueueEvent(departureEvent)
			else :
				#schedule time quantum expired event for request
				quantamExpiredEvent = Event.Event(self.simulationTime + self.system.timeQuantum, 2, dequedRequest.requestId)
				self.eventList.enqueueEvent(quantamExpiredEvent)

	#to print log message
	def printLogMessages(self, time, requestId, eventType):
		print (str(time)+'	'+ str(requestId)+'	'+str(eventType))


	#to handle timeout events of the request
	def timeoutEventHandler(self, event):
		request = self.getRequestFromEvent(event)
		if request is not None:
			#request still resides in the system, so respective client timeout occurs
			self.printLogMessages(self.simulationTime, event.eventId,'clientTimeout')
			#client generates a new request
			newRequest = Request.Request(request.clientId, request.arrivalTimeDistributionLambda, request.serviceTimeDistribution, request.param1, request.timeout, request.param2)
			self.requestList.addToRequestList(newRequest)
			#schedule arrival of the new request
			newEvent = Event.Event(self.simulationTime, 0, newRequest.requestId)
			self.eventList.enqueueEvent(newEvent)
			#schedule timeout of the new request
			newEvent1 = Event.Event(self.simulationTime + newRequest.timeout, 4, newRequest.requestId)
			self.eventList.enqueueEvent(newEvent1)


