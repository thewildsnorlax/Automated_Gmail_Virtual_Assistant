def checkformat (string):
	hours = ''
	minutes = ''
	seconds = ''

	if(string[2:4]==' p'):
		if(string[0:2]!='12'):
			temp = int(string[0:2])+12
			hours = str(temp)
			minutes = '00'
			seconds = '00'
		else:
			hours = string[0:2]
			minutes = '00'
			seconds = '00'

	elif(string[2:4]==' a' ):
		if(string[0:2]!='12'):
			hours = string[0:2]
			minutes = '00'
			seconds = '00'
		else:
			hours = '00'
			minutes = '00'
			seconds = '00'

	elif (len(string)==2):
		hours = string[0:2]
		minutes = '00'
		seconds = '00'

	elif (string[2]==':' and len(string)>5):
		if(string[6]=='p' and string[0:2]!='12'):
			temp = int(string[0:2])+12
			hours = str(temp)
			minutes = string[3:5]
			seconds = '00'
		else:
			hours = string[0:2]
			minutes = string[3:5]
			seconds = '00'

	elif (len(string)==5):
		hours = string[0:2]
		minutes = string[3:5]
		seconds = '00'
	return hours+':'+minutes+':'+seconds

