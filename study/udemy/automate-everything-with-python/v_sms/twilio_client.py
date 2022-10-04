from twilio.rest import Client

from v_sms.constants import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN


twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
