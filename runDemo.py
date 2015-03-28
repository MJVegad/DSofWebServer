import sys, os

if len(sys.argv) < 2 :
	print ('Command line format :: runDemo.py <input-file>')
	exit()

if not os.path.isfile(sys.argv[1]) :
	print ('Input file does not exist in the current directory')
	exit()

os.system('python3' + ' Main.py ' + sys.argv[1])


