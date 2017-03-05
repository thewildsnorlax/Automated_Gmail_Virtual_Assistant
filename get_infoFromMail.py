from __future__ import print_function
from auth import *                                #auth.py
from get_messageID import ListMessagesMatchingQuery             #get_messageID.py
from get_mimeMessage import GetMimeMessage
from process_mail import process_text
import httplib2
import os
import smtplib
from auth import get_credentials
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
import datetime
import base64
import email
from apiclient import errors
import fun_date
import fun_time
from datetime import datetime
from httplib2 import Http
from apiclient.discovery import build



credentials = get_credentials()
service = build('gmail', 'v1', http=credentials.authorize(Http()))
service2 = discovery.build('calendar', 'v3', http=credentials.authorize(Http()))

listmessage = ListMessagesMatchingQuery(service, 'me', 'in:inbox AND newer_than:2d AND older_than:1d')
l = len(listmessage)

current_date = datetime.now().strftime('%Y-%m-%d')
current_time = datetime.now().strftime('%H:%M:%S')

TO = 'btp.sem4@gmail.com'
SUBJECT = 'Conflicting Events'

gmail_sender = 'btp.sem4@gmail.com'
gmail_passwd = 'mohitashish'

  
for i in range(l):
    a = listmessage[i]['id']
    message = GetMimeMessage(service, 'me', a)
    start_date1 = process_text(message, 'Starting Date')
    end_date1 = process_text(message, 'Starting Date')
    location = process_text(message, 'Location')
    start_time = process_text(message, 'Start Time')
    end_time = process_text(message, 'End Time')
    event_details = process_text(message, 'Event Details')
    start_date = fun_date.checkformat(start_date1)+'T'+fun_time.checkformat(start_time)+'%s'
    end_date  = fun_date.checkformat(end_date1)+'T'+fun_time.checkformat(end_time)+'%s'

    check_start_date = start_date[:-2] + '+05:30'
    check_end_date = end_date[:-2] + '+05:30'

    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    
    eventsResult = service2.events().list(
        calendarId='primary', timeMin=check_start_date,timeMax=check_end_date, 
        maxResults=10, singleEvents=True, orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    start = ''

    if events:
        for event in events:
            start += event['summary'] + ', '
        start = start[:-1]

        TEXT = 'Some of your events are clashing on' + start_date[0:10] + 'The event summary is as follows:' + start


        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo
        server.login(gmail_sender, gmail_passwd)

        BODY = '\r\n'.join(
            [   
            'To: %s' % TO,
            'From: %s' % gmail_sender,
            'Subject: %s' % SUBJECT,
            '',
            TEXT    
            ])

        try:
            server.sendmail(gmail_sender, [TO], BODY)

        except:
            print ("Error sending email")

        server.quit()


    GMT_OFF = '+05:30'      
    EVENT = {
    'summary': event_details,
    'location':location,
    'start':  {'dateTime': start_date % GMT_OFF},
    'end':    {'dateTime': end_date % GMT_OFF},

    'reminders': {
        'useDefault': False,
        'overrides': [
            {'method': 'email', 'minutes': 10},
            
    ],
  },

    }

    e = service2.events().insert(calendarId='primary', body=EVENT).execute()
