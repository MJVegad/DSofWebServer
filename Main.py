import Simulation, Event, EventList

print ('Starting simulation')

# (sizeOfBuffer, timeout, numberOfThreads, numberOfCores, timeQuantum, contextSwitchTime, numberOfClients, arrivalTimeDistributionLambda, thinkTimeDistribution, serviceTimeDistribution, paramThinkTime1, paramServiceTime1, paramThinkTime2=None, paramServiceTime2=None)
simulation = Simulation.Simulation(10, 8, 3, 2, 2, 1, 5, 1, 0, 0, 2, 6);

for event in simulation.eventList:
	print (event.timestamp)