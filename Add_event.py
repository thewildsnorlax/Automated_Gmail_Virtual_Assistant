from __future__ import print_function
import httplib2
import os
import get_infoFromMail
import smtplib
from auth import get_credentials


from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools

import datetime
check_start_date = get_infoFromMail.start_date[:-2] + '+05:30'
check_end_date = get_infoFromMail.end_date[:-2] + '+05:30'

TO = 'btp.sem4@gmail.com'
SUBJECT = 'Conflicting Events'

gmail_sender = 'btp.sem4@gmail.com'
gmail_passwd = 'mohitashish'

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


def main():
    credentials = get_credentials()
    print (credentials)
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming events')
    
    eventsResult = service.events().list(
        calendarId='primary', timeMin=check_start_date,timeMax=check_end_date, 
        maxResults=10, singleEvents=True, orderBy='startTime').execute()
    events = eventsResult.get('items', [])
    start = ''

    if not events:
        print('No upcoming events found.')

    elif events:
        for event in events:
            start += event['summary'] + ', '
        start = start[:-1]

        TEXT = 'Some of your events are clashing on' + get_infoFromMail.start_date[0:10] + 'The event summary is as follows:' + start


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
            print ('Email Sent')

        except:
            print ('Error Sending Email')

        server.quit()


    GMT_OFF = '+05:30'      
    EVENT = {
    'summary': get_infoFromMail.event_details,
    'location':get_infoFromMail.location,
    'start':  {'dateTime': get_infoFromMail.start_date % GMT_OFF},
    'end':    {'dateTime': get_infoFromMail.end_date % GMT_OFF},

    'reminders': {
        'useDefault': False,
        'overrides': [
            {'method': 'email', 'minutes': 10},
            
    ],
  },

    }

    e = service.events().insert(calendarId='primary', body=EVENT).execute()

    print ("Event Added")
