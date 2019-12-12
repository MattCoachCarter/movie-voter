# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC9a21cff385b1ad97a50b588b1bb204e8'
auth_token = '3c8c7852a4778439a38e8442ae0b5769'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+12702880653',
                     to='+16362489705'
                 )

print(message.sid)
# http://www.omdbapi.com/?t=tremors&apikey=f5ea7ac