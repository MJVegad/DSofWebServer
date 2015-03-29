import Simulation, Event, EventList,configobj, sys

print ('Starting simulation')
print ('==================================')

def printLogMessages(time, requestId, eventType):
	print (str(time)+'	'+ str(requestId)+'	'+str(eventType))

#def __init__(self, sizeOfBuffer, timeout, numberOfThreads, numberOfCores, timeQuantum, contextSwitchTime, numberOfClients, arrivalTimeDistributionLambda, thinkTimeDistribution, serviceTimeDistribution, paramThinkTime1, paramServiceTime1, paramThinkTime2=None, paramServiceTime2=None):
configFile = sys.argv[1]
config = configobj.ConfigObj(configFile)
if config['TTPARAMOPTIONAL']=='None' and config['STPARAMOPTIONAL']=='None':
	simulation = Simulation.Simulation(int(config['SIZEOFBUFFER']),int(config['TIMEOUT']),int(config['NUMBEROFTHREADS']),int(config['NUMBEROFCORES']),int(config['TIMEQUANTUM']),int(config['CONTEXTSWITCHTIME']),int(config['NUMBEROFCLIENTS']),int(config['RANDOMSEED']),int(config['ARRIVALTIMEDISTRIBUTIONLAMBDA']),int(config['THINKTIMEDISTRIBUTION']),int(config['SERVICETIMEDISTRIBUTION']),int(config['THINKTIMEPARAM']),int(config['SERVICETIMEPARAM']))
elif config['TTPARAMOPTIONAL']=='None':
	simulation = Simulation.Simulation(int(config['SIZEOFBUFFER']),int(config['TIMEOUT']),int(config['NUMBEROFTHREADS']),int(config['NUMBEROFCORES']),int(config['TIMEQUANTUM']),int(config['CONTEXTSWITCHTIME']),int(config['NUMBEROFCLIENTS']),int(config['RANDOMSEED']),int(config['ARRIVALTIMEDISTRIBUTIONLAMBDA']),int(config['THINKTIMEDISTRIBUTION']),int(config['SERVICETIMEDISTRIBUTION']),int(config['THINKTIMEPARAM']),int(config['SERVICETIMEPARAM']),0,int(config['STPARAMOPTIONAL']))
elif config['STPARAMOPTIONAL']=='None':
	simulation = Simulation.Simulation(int(config['SIZEOFBUFFER']),int(config['TIMEOUT']),int(config['NUMBEROFTHREADS']),int(config['NUMBEROFCORES']),int(config['TIMEQUANTUM']),int(config['CONTEXTSWITCHTIME']),int(config['NUMBEROFCLIENTS']),int(config['RANDOMSEED']),int(config['ARRIVALTIMEDISTRIBUTIONLAMBDA']),int(config['THINKTIMEDISTRIBUTION']),int(config['SERVICETIMEDISTRIBUTION']),int(config['THINKTIMEPARAM']),int(config['SERVICETIMEPARAM']),int(config['TTPARAMOPTIONAL']))
else :
	simulation = Simulation.Simulation(int(config['SIZEOFBUFFER']),int(config['TIMEOUT']),int(config['NUMBEROFTHREADS']),int(config['NUMBEROFCORES']),int(config['TIMEQUANTUM']),int(config['CONTEXTSWITCHTIME']),int(config['NUMBEROFCLIENTS']),int(config['RANDOMSEED']),int(config['ARRIVALTIMEDISTRIBUTIONLAMBDA']),int(config['THINKTIMEDISTRIBUTION']),int(config['SERVICETIMEDISTRIBUTION']),int(config['THINKTIMEPARAM']),int(config['SERVICETIMEPARAM']),int(config['TTPARAMOPTIONAL']),int(config['STPARAMOPTIONAL']))


while (not simulation.eventList.eventList.empty() and simulation.simulationTime < 7):
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
		printLogMessages(simulation.simulationTime, event.eventId, 'core id for scheduleNextRequest')
		simulation.scheduleNextRequestEventHandler(event)
	elif eventType == 4 :
		#printLogMessages(simulation.simulationTime, event.eventId,'clientTimeout')
		simulation.timeoutEventHandler(event)

print ('Simulation Completed')
