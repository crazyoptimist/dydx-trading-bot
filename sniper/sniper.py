import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_PRIVATE_KEY = os.getenv('ACCOUNT_PRIVATE_KEY')

print(ACCOUNT_PRIVATE_KEY)
