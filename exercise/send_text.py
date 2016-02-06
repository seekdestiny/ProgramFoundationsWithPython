from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACf0c91327910c7c3b8a0e59e32d290c4e"
auth_token  = "fe321e58aeee946e6392836aa7c66617"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="My name is Jeff Qian.",
    to="+17342393751",    # Replace with your phone number
    from_="+17345489390") # Replace with your Twilio number
print message.sid
