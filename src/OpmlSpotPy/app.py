import os
from opml_importer import OPMLImporter
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Replace these values with your own Spotify API credentials
client_id = os.environ["OPMLSPOT_CLIENT_ID"]
client_secret = os.environ["OPMLSPOT_CLIENT_SECRET"]
redirect_uri = os.environ["OPMLSPOT_REDIRECT_URI"]
username = os.environ["OPMLSPOT_USERNAME"]


opml_importer = OPMLImporter(client_id, client_secret, redirect_uri, username)
opml_importer.import_podcasts("podcasts.opml")
