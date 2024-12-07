import os
from dotenv import load_dotenv

from bitwarden_sdk import BitwardenClient

load_dotenv()

BW_ACCESS_TOKEN = os.getenv("BW_ACCESS_TOKEN")
EXAMPLE_SECRET_UUID = os.getenv("EXAMPLE_SECRET_UUID")

client = BitwardenClient()

client.auth().login_access_token(BW_ACCESS_TOKEN)

EXAMPLE_SECRET = client.secrets().get(EXAMPLE_SECRET_UUID).data.value

print(EXAMPLE_SECRET)