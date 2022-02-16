#用 twilio 傳 簡訊
from twilio.rest import Client
account_sid = 'A'
auth_token = 'f'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="EricWu Go Go Go !.",
                     from_='+18596952721',
                     to='+8'
                 )

print(message.sid)