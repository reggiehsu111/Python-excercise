from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = "ACab406dc94aa9626ad66b16004f0a6497" # Your Account SID from www.twilio.com/console
auth_token  = "94485b490e46a4644569f6bbde1cb6b1"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

try:
    message = client.messages.create(body="哈囉  我用電腦傳給你訊息喔",
        to="+886958004230",    # Replace with your phone number
        from_="+18478654286") # Replace with your Twilio number
except TwilioRestException as e:
    print(e)