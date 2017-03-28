import time
import json
def findTimeTest(time, data):
	timeToRun = []
	seconds = convertToSeconds(time)
	##text=List of strings to be written to file
	for i in data:
		# with open('csvfile.csv','wb') as file:
		# 	file.write(str(i.get('distance')))
		secondsTotal = i.get('distance')/(1609.34/seconds)
		hours, sec =  secondsTotal // 3600, secondsTotal % 3600
		min, sec = sec // 60, sec % 60
	 	if (min == 0):
			time = str(int(sec))+"s"
		elif (hours == 0):
			time = str(int(min))+'m:'+str(int(sec))+"s"
		else:
			time = str(int(hours))+'h:'+str(int(min))+'m:'+str(int(sec))+"s"
		timeToRun.append(time)
	return timeToRun

def convertToSeconds(time):
	min, sec = time.split(':')
	return int(min) * 60 + int(sec)

def convertDistToMiles(data):
	miles = []
	for i in data:
		milesD = i.get('distance')*0.000621371192;
		mile = '%.3f'%(milesD)
		miles.append(mile)
	return miles
