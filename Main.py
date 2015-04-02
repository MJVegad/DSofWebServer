import Simulation, Event, EventList,configobj, sys, os, Request
#import matplotlib.pyplot as plt


print ('Starting simulation')
print ('==================================')

def printLogMessages(time, requestId, eventType):
	print (str(time)+'	'+ str(requestId)+'	'+str(eventType))

'''
def plotGraph(list1, list2):
	colors={'Average response time':'blue'}
	markers={'Average response time':'o'}
	lss={'No. of users':'--'}

	plt.plot(list2, list1, label='Average response time', ls=lss['No. of users'], color=colors['Average response time'], marker=markers['Average response time'], markersize=9, mew=2, linewidth=2)
	#blt.axis(xmin=0)
	#plt.axis(xmax=25)
	plt.xlabel('No.of users')
	plt.ylabel('Average response time')
	plt.grid(b='on')
	plt.title('Avg. response time vs. No. of users')
	plt.savefig("graph1.pdf", bbox_inches='tight')
'''

'''
#def __init__(self, sizeOfBuffer, timeout, numberOfThreads, numberOfCores, timeQuantum, contextSwitchTime, numberOfClients, arrivalTimeDistributionLambda, thinkTimeDistribution, serviceTimeDistribution, paramThinkTime1, paramServiceTime1, paramThinkTime2=None, paramServiceTime2=None):
configFile = sys.argv[1]
config = configobj.ConfigObj(configFile)
'''
if len(sys.argv) == 15:
	simulation = Simulation.Simulation(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]),int(sys.argv[8]),int(sys.argv[9]),int(sys.argv[10]),int(sys.argv[11]),int(sys.argv[12]),int(sys.argv[13]))
elif len(sys.argv) == 17 and int(sys.argv[14]) == 0:
	simulation = Simulation.Simulation(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]),int(sys.argv[8]),int(sys.argv[9]),int(sys.argv[10]),int(sys.argv[11]),int(sys.argv[12]),int(sys.argv[13]),0,int(sys.argv(15)))
elif len(sys.argv) == 16:
	simulation = Simulation.Simulation(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]),int(sys.argv[8]),int(sys.argv[9]),int(sys.argv[10]),int(sys.argv[11]),int(sys.argv[12]),int(sys.argv[13]),int(sys.argv[14]))
else :
	simulation = Simulation.Simulation(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7]),int(sys.argv[8]),int(sys.argv[9]),int(sys.argv[10]),int(sys.argv[11]),int(sys.argv[12]),int(sys.argv[13]),int(sys.argv[14]),int(sys.argv[15]))


while (not simulation.eventList.eventList.empty() and simulation.departureCount < int(sys.argv[len(sys.argv)-1])):
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

#print ('departurecount===============> '+ str(simulation.departureCount))
averageResponseTime = simulation.metrics.getAvgResponseTime(simulation.departureCount)
numberOfUsers = len(simulation.clients)

if not os.path.isfile('graph1.log'):
	with open('graph1.log', mode='w', encoding='utf-8') as a_file:
	    a_file.write(str(averageResponseTime)+' '+str(numberOfUsers)+'\n')
else:
	with open('graph1.log', mode='a', encoding='utf-8') as a_file:
	    a_file.write(str(averageResponseTime)+' '+str(numberOfUsers)+'\n')



print ('$$$$$$$$$$$$$$$$$$$$$$Avg. response time============> '+ str(simulation.metrics.getAvgResponseTime(simulation.departureCount)))
print ('Matric 2 :: Average Badput - '+ str(simulation.metrics.getBadput(simulation.simulationTime)))
print ('Matric 3 :: Average Goodput - '+ str(simulation.metrics.getGoodput(simulation.simulationTime)))
print ('Matric 4 :: Average Throughput - '+ str(simulation.metrics.getThroughput(simulation.simulationTime)))
print ('------------------------------------Simulation Completed---------------------------------')
