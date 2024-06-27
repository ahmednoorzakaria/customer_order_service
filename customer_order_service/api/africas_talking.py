import africastalking
import os
from dotenv import load_dotenv
load_dotenv()

username = "sandbox"  
api_key = os.getenv('api_key')



africastalking.initialize(username, api_key)

sms = africastalking.SMS
