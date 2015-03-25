import sys, os.path

def returnCmdStr(noOfArg) :
	cmdString = ''
	for index in range(noOfArg) :
		intVal = int(commandLineArgs[index])
		cmdString = cmdString + ' ' + str(intVal)
	return cmdString

if len(sys.argv) < 3 :
	print ('Command line format :: runDemo.sh <input-file> <output-file>')
	exit()

if not os.path.isfile(sys.argv[1]) :
	print ('Input file does not exist in the current directory')
	exit()

f = open(sys.argv[1], 'r')

commandLineArgs = []

for line in f :
	commandLineArgs.append(line)

commandLineArgs = commandLineArgs[:14]

if commandLineArgs[12] == '\n' and commandLineArgs[13] == '\n': 
	commandLineString = returnCmdStr(12)
elif commandLineArgs[12] == '\n' or commandLineArgs[13] == '\n':
	commandLineString = returnCmdStr(13)
else:
	commandLineString = returnCmdStr(14)

os.system("Main.py" + commandLineString)	