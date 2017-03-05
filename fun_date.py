def checkmonth (month):
	if (month=='Jan' or month == 'jan'): return '01'
	elif (month=='Feb' or month == 'feb'): return '02'
	elif (month=='Mar' or month == 'mar'): return '03'
	elif (month=='Apr' or month == 'apr'): return '04'
	elif (month=='May' or month == 'may'): return '05'
	elif (month=='Jun' or month == 'jun'): return '06'
	elif (month=='Jul' or month == 'jul'): return '07'
	elif (month=='Aug' or month == 'aug'): return '08'
	elif (month=='Sep' or month == 'sep'): return '09'
	elif (month=='Oct' or month == 'oct'): return '10'
	elif (month=='Nov' or month == 'nov'): return '11'
	elif (month=='Dec' or month == 'dec'): return '12'
		
def checkformat (str):
	global ns

	if ((str.find('/')==2) or (str.find('-')==2) or (str.find('.')==2) ):
		i=0
		date = str[i:i+2]
		month = str[i+3:i+5]
		year = str[i+6:i+10]

	elif ((str.find('/')==4) or (str.find('-')==4) or (str.find('.')==4 )):
		i=0
		year = str[i:i+4]
		month = str[i+5:i+7]
		date = str[i+8:i+10]

	elif (str.find(' ')==2):
		i=0
		date = str[i:i+2]
		month = str[i+3:i+6]
		year = str[i+7:i+11]
		month = checkmonth(month)

	elif (str.find(' ')==3):
		i=0
		month = str[i:i+3]
		date = str[i+4:i+6]
		year = str[i+7:i+11]
		month = checkmonth(month)

	elif (str.find(' ')==4 and (str[2]=='t' or str[2]=='r' or str[2]=='s' 
		or str[2]=='n') and len(str)==13):
		i=0
		date = str[i:i+2]
		month = str[i+5:i+8]
		year = str[i+9:i+13]
		month = checkmonth(month)		

	elif (len(str)>13 and str.find(' ')==4 and (str[2]=='t' or str[2]=='r' 
		or str[2]=='s' or str[2]=='n')):
		i=0
		date = str[i:i+2]

		if (str[i+6:i+8]=='an') :
			month = '01' 
			year = str[i+13:i+17]

		elif (str[i+6:i+8]=='eb') :
			month = '02' 
			year = str[i+14:i+18]

		elif (str[i+6:i+8]=='ar') :
			month = '03' 
			year = str[i+11:i+15]
				
		elif (str[i+6:i+8]=='pr') :
			month = '04' 
			year = str[i+11:i+15]
				
		elif (str[i+6:i+8]=='ay') :
			month = '05' 
			year = str[i+9:i+13]
				
		elif (str[i+6:i+8]=='un') :
			month = '06' 
			year = str[i+10:i+14]
			
		elif (str[i+6:i+8]=='ul') :
			month = '07' 
			year = str[i+10:i+14]
			
		elif (str[i+6:i+8]=='ug') :
			month = '08' 
			year = str[i+12:i+16]

		elif (str[i+6:i+8]=='ep') :
			month = '09' 
			year = str[i+15:i+19]

		elif (str[i+6:i+8]=='ct') :
			month = '10' 
			year = str[i+13:i+17]

		elif (str[i+6:i+8]=='ov') :
			month = '11' 
			year = str[i+14:i+18]

		elif (str[i+6:i+8]=='ec') :
			month = '12' 
			year = str[i+14:i+18]

	elif (len(str)>=13 and str.find(' ')!=4):
		i=0
		if (str[i+1:i+3]=='an') :
			date = str[i+8:i+10]
			month = '01' 
			year = str[i+13:i+17]

		elif (str[i+1:i+3]=='eb') :
			date = str[i+9:i+11]
			month = '02' 
			year = str[i+14:i+18]

		elif (str[i+1:i+3]=='ar') :
			date = str[i+6:i+8]
			month = '03' 
			year = str[i+11:i+15]
				
		elif (str[i+1:i+3]=='pr') :
			date = str[i+6:i+8]
			month = '04' 
			year = str[i+11:i+15]
				
		elif (str[i+1:i+3]=='ay') :
			date = str[i+4:i+6]
			month = '05' 
			year = str[i+9:i+13]
				
		elif (str[i+1:i+3]=='un') :
			date = str[i+5:i+7]
			month = '06' 
			year = str[i+10:i+14]
			
		elif (str[i+1:i+3]=='ul') :
			date = str[i+5:i+7]
			month = '07' 
			year = str[i+10:i+14]
			
		elif (str[i+1:i+3]=='ug') :
			date = str[i+7:i+9]
			month = '08' 
			year = str[i+12:i+16]

		elif (str[i+1:i+3]=='ep') :
			date = str[i+10:i+12]
			month = '09' 
			year = str[i+15:i+19]

		elif (str[i+1:i+3]=='ct') :
			date = str[i+8:i+10]
			month = '10' 
			year = str[i+13:i+17]

		elif (str[i+1:i+3]=='ov') :
			date = str[i+9:i+11]
			month = '11' 
			year = str[i+14:i+18]

		elif (str[i+1:i+3]=='ec') :
			date = str[i+9:i+11]
			month = '12' 
			year = str[i+14:i+18]
		
	return year + '-' + month + '-' + date