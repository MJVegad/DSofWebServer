import Simulation, Event, EventList

print ('Starting simulation')

def printLogMessages(time, requestId, eventType):
	print (str(time)+'			'+ str(requestId)+'			'+str(eventType))


printLogMessages('Time', '			RequestId', '		EventType')

#def __init__(self, sizeOfBuffer, timeout, numberOfThreads, numberOfCores, timeQuantum, contextSwitchTime, numberOfClients, arrivalTimeDistributionLambda, thinkTimeDistribution, serviceTimeDistribution, paramThinkTime1, paramServiceTime1, paramThinkTime2=None, paramServiceTime2=None):
simulation = Simulation.Simulation(10, 8, 1, 1, 1, 1, 2, 1, 0, 0, 2, 1);

'''for index in list(range(len(simulation.eventList.eventList))):
	print (simulation.eventList.eventList[index].eventId)
	print (simulation.eventList.eventList[index].timestamp) '''

while simulation.eventList.eventList is not [] and simulation.simulationTime < 20:
#while simulation.eventList.eventList is not []:

	event = simulation.eventList.dequeueEvent()
	eventType = event.eventType
	#print (event.eventId)
	simulation.simulationTime = event.timestamp

	if eventType == 0 :
		printLogMessages(simulation.simulationTime,event.eventId, 'arrival')
		simulation.arrivalEventHandler(event)
	elif eventType == 1 :
		printLogMessages(simulation.simulationTime,event.eventId, 'departure')
		simulation.departureEventHandler(event)
	elif eventType == 2 :
		printLogMessages(simulation.simulationTime,event.eventId, 'quantumExpired')
		simulation.quantamExpiredEventHandler(event)
	elif eventType == 3 :
		#printLogMessages(simulation.simulationTime, 'scheduleNextRequest', simulation.getRequestFromEvent(event).requestId)
		simulation.scheduleNextRequestEventHandler(event)
	elif eventType == 4 :
		printLogMessages(simulation.simulationTime, event.eventId,'clientTimeout')
		simulation.timeoutEventHandler(event)

print ('Simulation Completed')


