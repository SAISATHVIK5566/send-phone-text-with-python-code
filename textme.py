from twilio.rest import Client 
 
account_sid = 'ACf87b63eae9212e980249b343f3016290' 
auth_token = 'cd685e7ef69671bf05fd4d14c3d5bc70' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+12029524531',  
                              body='Iam texting this thing out',      
                              to='+919347735636' 
                          )
 
print(message.sid)