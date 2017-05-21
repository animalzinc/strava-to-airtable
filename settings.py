import os
from dotenv import load_dotenv

from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

AIRTABLE_API_KEY = os.environ.get('AIRTABLE_API_KEY')
AIRTABLE_BASE = 'app5Bgi9eRp49oGyZ'

STRAVA_ACCESS_TOKEN = os.environ.get('STRAVA_ACCESS_TOKEN')
