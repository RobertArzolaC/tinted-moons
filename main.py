import os

from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
from twilio.rest import Client

from constants import SITE_URL, MESSAGE, TAG_ID
from logger import ScraperLogger


logger = ScraperLogger("ScraperLogger", file_path="scraper.log")
load_dotenv()

twilio_account_sid = os.getenv('TWILIO_ACCOUNT_SID')
twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(twilio_account_sid, twilio_auth_token)

response = requests.get(SITE_URL)

soup = BeautifulSoup(response.content, "html.parser")
element = soup.find(id=TAG_ID)

if element.text != MESSAGE:
    logger.info("Hay cupos disponibles")
    client.messages.create(
        body=f"Hay cupos disponibles de Lunas Polarizadas: {SITE_URL}",
        from_="+16813813359",
        to="+51931314241"
    )
else:
    logger.info("No hay cupos disponibles")
