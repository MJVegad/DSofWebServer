import sys, os, configobj
import matplotlib.pyplot as plt

if len(sys.argv) < 2 :
	print ('Command line format :: runDemo.py <input-file>')
	exit()

if not os.path.isfile(sys.argv[1]) :
	print ('Input file does not exist in the current directory')
	exit()

#os.system('python3' + ' Main.py ' + sys.argv[1])
os.system('rm graph1.log')

def plotGraph(list1, list2):
        colors={'Average response time':'blue'}
        markers={'Average response time':'o'}
        lss={'No. of users':'--'}

        plt.plot(list2, list1, label='Average response time', ls=lss['No. of users'], color=colors['Average response time'], marker=markers['Average response time'], markersize=9, mew=2, linewidth=2)
        #plt.axis(xmin=0)
        #plt.axis(xmax=25)
        plt.xlabel('No.of users')
        plt.ylabel('Average response time')
        plt.grid(b='on')
        plt.title('Avg. response time vs. No. of users')
        plt.savefig("graph1.pdf", bbox_inches='tight')



averageResponseTime = []
numberOfUsers = []
#def __init__(self, sizeOfBuffer, timeout, numberOfThreads, numberOfCores, timeQuantum, contextSwitchTime, numberOfClients, arrivalTimeDistributionLambda, thinkTimeDistribution, serviceTimeDistribution, paramThinkTime1, paramServiceTime1, paramThinkTime2=None, paramServiceTime2=None):
configFile = sys.argv[1]
config = configobj.ConfigObj(configFile)

for numberOfClients in config['NUMBEROFCLIENTS']:
	if config['TTPARAMOPTIONAL']=='None' and config['STPARAMOPTIONAL']=='None':
		#simulation = Simulation.Simulation(int(config['SIZEOFBUFFER']),int(config['TIMEOUT']),int(config['NUMBEROFTHREADS']),int(config['NUMBEROFCORES']),int(config['TIMEQUANTUM']),int(config['CONTEXTSWITCHTIME']),int(numberOfClients),int(config['RANDOMSEED']),int(config['ARRIVALTIMEDISTRIBUTIONLAMBDA']),int(config['THINKTIMEDISTRIBUTION']),int(config['SERVICETIMEDISTRIBUTION']),int(config['THINKTIMEPARAM']),int(config['SERVICETIMEPARAM']))
		os.system('python3 '+'Main.py '+config['SIZEOFBUFFER']+' '+config['TIMEOUT']+' '+config['NUMBEROFTHREADS']+' '+config['NUMBEROFCORES']+' '+config['TIMEQUANTUM']+' '+config['CONTEXTSWITCHTIME']+' '+numberOfClients+' '+config['RANDOMSEED']+' '+config['ARRIVALTIMEDISTRIBUTIONLAMBDA']+' '+config['THINKTIMEDISTRIBUTION']+' '+config['SERVICETIMEDISTRIBUTION']+' '+config['THINKTIMEPARAM']+' '+config['SERVICETIMEPARAM']+' '+config['DEPARTURESTOTERMINATE'])
	elif config['TTPARAMOPTIONAL']=='None':
		os.system('python3 '+'Main.py '+config['SIZEOFBUFFER']+' '+config['TIMEOUT']+' '+config['NUMBEROFTHREADS']+' '+config['NUMBEROFCORES']+' '+config['TIMEQUANTUM']+' '+config['CONTEXTSWITCHTIME']+' '+numberOfClients+' '+config['RANDOMSEED']+' '+config['ARRIVALTIMEDISTRIBUTIONLAMBDA']+' '+config['THINKTIMEDISTRIBUTION']+' '+config['SERVICETIMEDISTRIBUTION']+' '+config['THINKTIMEPARAM']+' '+config['SERVICETIMEPARAM']+' '+str(0)+' '+config['STPARAMOPTIONAL']+' '+config['DEPARTURESTOTERMINATE'])
		#simulation = Simulation.Simulation(int(config['SIZEOFBUFFER']),int(config['TIMEOUT']),int(config['NUMBEROFTHREADS']),int(config['NUMBEROFCORES']),int(config['TIMEQUANTUM']),int(config['CONTEXTSWITCHTIME']),int(numberOfClients),int(config['RANDOMSEED']),int(config['ARRIVALTIMEDISTRIBUTIONLAMBDA']),int(config['THINKTIMEDISTRIBUTION']),int(config['SERVICETIMEDISTRIBUTION']),int(config['THINKTIMEPARAM']),int(config['SERVICETIMEPARAM']),0,int(config['STPARAMOPTIONAL']))
	elif config['STPARAMOPTIONAL']=='None':
	    os.system('python3 '+'Main.py '+config['SIZEOFBUFFER']+' '+config['TIMEOUT']+' '+config['NUMBEROFTHREADS']+' '+config['NUMBEROFCORES']+' '+config['TIMEQUANTUM']+' '+config['CONTEXTSWITCHTIME']+' '+numberOfClients+' '+config['RANDOMSEED']+' '+config['ARRIVALTIMEDISTRIBUTIONLAMBDA']+' '+config['THINKTIMEDISTRIBUTION']+' '+config['SERVICETIMEDISTRIBUTION']+' '+config['THINKTIMEPARAM']+' '+config['SERVICETIMEPARAM']+' '+config['TTPARAMOPTIONAL']+' '+config['DEPARTURESTOTERMINATE'])
		#simulation = Simulation.Simulation(int(config['SIZEOFBUFFER']),int(config['TIMEOUT']),int(config['NUMBEROFTHREADS']),int(config['NUMBEROFCORES']),int(config['TIMEQUANTUM']),int(config['CONTEXTSWITCHTIME']),int(numberOfClients),int(config['RANDOMSEED']),int(config['ARRIVALTIMEDISTRIBUTIONLAMBDA']),int(config['THINKTIMEDISTRIBUTION']),int(config['SERVICETIMEDISTRIBUTION']),int(config['THINKTIMEPARAM']),int(config['SERVICETIMEPARAM']),int(config['TTPARAMOPTIONAL']))
	else :
		os.system('python3 '+'Main.py '+config['SIZEOFBUFFER']+' '+config['TIMEOUT']+' '+config['NUMBEROFTHREADS']+' '+config['NUMBEROFCORES']+' '+config['TIMEQUANTUM']+' '+config['CONTEXTSWITCHTIME']+' '+numberOfClients+' '+config['RANDOMSEED']+' '+config['ARRIVALTIMEDISTRIBUTIONLAMBDA']+' '+config['THINKTIMEDISTRIBUTION']+' '+config['SERVICETIMEDISTRIBUTION']+' '+config['THINKTIMEPARAM']+' '+config['SERVICETIMEPARAM']+' '+config['TTPARAMOPTIONAL']+' '+config['STPARAMOPTIONAL']+' '+config['DEPARTURESTOTERMINATE'])
		#simulation = Simulation.Simulation(int(config['SIZEOFBUFFER']),int(config['TIMEOUT']),int(config['NUMBEROFTHREADS']),int(config['NUMBEROFCORES']),int(config['TIMEQUANTUM']),int(config['CONTEXTSWITCHTIME']),int(numberOfClients),int(config['RANDOMSEED']),int(config['ARRIVALTIMEDISTRIBUTIONLAMBDA']),int(config['THINKTIMEDISTRIBUTION']),int(config['SERVICETIMEDISTRIBUTION']),int(config['THINKTIMEPARAM']),int(config['SERVICETIMEPARAM']),int(config['TTPARAMOPTIONAL']),int(config['STPARAMOPTIONAL']))
	#doSimulation(simulation, config['DEPARTURESTOTERMINATE'])

	#print ('departurecount===============> '+ str(simulation.departureCount))
	#averageResponseTime.append(Main.averageResponseTime)
	#numberOfUsers.append(Main.numberOfUsers)
	#print ('$$$$$$$$$$$$$$$$$$$$$$Avg. response time============> '+ str(simulation.metrics.getAvgResponseTime(simulation.departureCount)))
	#print ('------------------------------------Simulation Completed---------------------------------')


print ('Wait..!! Generating graphs....')
plotGraph(averageResponseTime,numberOfUsers)
