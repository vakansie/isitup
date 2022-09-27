import requests
from twilio.rest import Client

url = ''
twilio_phone = ''
my_phone = ''
twilio_SID = ''
twilio_auth_token = ''

SMS_client = Client(twilio_SID, twilio_auth_token)

http_status_dict = {
    200: 'HTTP 200: All is well.',
    301: 'HTTP 301: Permanent Redirect',
    302: 'HTTP 302: Temporary Redirect',
    404: 'HTTP 404: it is down...',
    500: 'HTTP 500: Internal Server Error',
    503: 'HTTP 503: Service Unavailable'}


def send_SMS(client, message):
    client.messages.create(to=my_phone, 
                       from_= twilio_phone, 
                       body=f'isitup.py says: "{message}"')

def check_status(url):
        site_response = requests.get(url)
        return site_response.status_code

if __name__== '__main__':
    try:
        response = check_status(url)
        if response != 200:
            send_SMS(SMS_client, http_status_dict[response])
    except Exception as whateveritisnow:
        send_SMS(SMS_client, whateveritisnow)
