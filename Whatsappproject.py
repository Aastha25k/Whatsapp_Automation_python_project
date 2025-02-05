#step 1 install required libraries
from twilio.rest import Client                 #client will be used to send messages 
from datetime import datetime,timedelta        #datetime will manage date and time  , timedelta will calculate the difference
import time                                    #to add timedelay 

#step 2 twilio  credentials
account_sid = ''
auth_token=''

client = Client(account_sid,auth_token)

#step 3 define send message function

def send_whatsapp_message(receipient_number,message_body):
    try:
        message = client.messages.create(
            from_='whatsapp: ',
            body = message_body,
            to =f'whatsapp:{recipient_number}'
        )
        print(f"Message sent successfully! Message SID{message.sid}")
    except Exception as e:
        print("An error occured")

#step 4 user input

name= input('Enter the recipient name= ')        
recipient_number =input('Enter the recipient whatsapp number with country code(e.g. +124)')
message_body = input('Enter the message you want to send to {name}: ')

#step 5 parse date/time and calculate delay
date_str =input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Ener the time to send the message (HH:MM in 24 hr format): ')

#datetime
schedule_datetime =datetime.strptime(f'{date_str} {time_str}',"%Y-%m-%d %H:%M")  #strptime= string parse time ...converts string to date time object
current_datetime = datetime.now()

#calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <=0:
    print('The specified time is in the past. Please enter a future date/time: ')
else:
    print(f'Message to be sent to {name} at {schedule_datetime}.')    

    #wait until the scheduled time
    time.sleep(delay_seconds)    #1000

    #send the message
    send_whatsapp_message(recipient_number,message_body)



