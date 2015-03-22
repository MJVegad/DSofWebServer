import Simulation, Event, EventList

print ('Starting simulation')

def printLogMessages(time, eventType):
	print (str(time)+'			'+str(eventType))


printLogMessages('Time', '		EventType')

# (sizeOfBuffer, timeout, numberOfThreads, numberOfCores, timeQuantum, contextSwitchTime, numberOfClients, arrivalTimeDistributionLambda, thinkTimeDistribution, serviceTimeDistribution, paramThinkTime1, paramServiceTime1, paramThinkTime2=None, paramServiceTime2=None)
simulation = Simulation.Simulation(10, 8, 3, 1, 1, 1, 1, 1, 0, 0, 2, 1);

'''for index in list(range(len(simulation.eventList.eventList))):
	print (simulation.eventList.eventList[index].eventId)
	print (simulation.eventList.eventList[index].timestamp) '''

while simulation.eventList.eventList is not [] and simulation.simulationTime < 20:
	event = simulation.eventList.dequeueEvent()
	eventType = event.eventType
	#print (simulation.simulationTime)
	simulation.simulationTime = event.timestamp
	if eventType == 0 :
		printLogMessages(simulation.simulationTime, 'arrival')
		simulation.arrivalEventHandler(event)
	elif eventType == 1 :
		printLogMessages(simulation.simulationTime, 'departure')
		simulation.departureEventHandler(event)
	elif eventType == 2 :
		printLogMessages(simulation.simulationTime, 'quantumExpired')
		simulation.quantamExpiredEventHandler(event)
	elif eventType == 3 :
		#printLogMessages(simulation.simulationTime, 'scheduleNextRequest', simulation.getRequestFromEvent(event).requestId)
		simulation.scheduleNextRequestEventHandler(event)
	elif eventType == 4 :
		printLogMessages(simulation.simulationTime, 'clientTimeout')
		simulation.timeoutEventHandler(event)

print ('Simulation Completed')


