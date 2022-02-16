from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACa82a0768cd2bacd5f0c39d4f4c64429d'
auth_token = 'feeb2ea3d3b96cfd80c8da0d7a429bf2'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="EricWu Go Go Go !.",
                     from_='+18596952721',
                     to='+886930310419'
                 )

print(message.sid)