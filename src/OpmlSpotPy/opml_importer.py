import spotipy
import spotipy.util as util
import xml.etree.ElementTree as ET

class OPMLImporter:

    def __init__(self, client_id, client_secret, redirect_uri, username):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.username = username

    def search_and_add_podcast(self, podcast):
        print("===")
        print(f"Searching for {podcast.name}")
        # Search for the podcast by url
        search_query = podcast.url
        search_type = "show"
        sp = self.get_spotify_client()
        search_results = sp.search(search_query, type=search_type)
        # Get the first show from the search results
        try:
            show = search_results["shows"]["items"][0]
            self.add_show_to_library(show, sp)
        except IndexError:
            # If no shows were found for the url, search for the podcast by name
            print(f"No shows found for {podcast.url}, searching by name instead")
            search_query = podcast.name
            search_results = sp.search(search_query, type=search_type)
            try:
                show = search_results["shows"]["items"][0]
                # Prompt the user for input
                user_input = input(f"Do you want to add {show['name']} to your library? [y/n] ")
                if user_input.lower() == "y":
                    self.add_show_to_library(show, sp)
                else:
                    print(f"Skipping {show['name']}")
            except IndexError:
                print(f"No shows found for {podcast.name}")
            except spotipy.client.SpotifyException as e:
                print(f"Error adding {podcast.name} - {podcast.url} to the library: {e}")
        except spotipy.client.SpotifyException as e:
            print(f"Error adding {podcast.name} - {podcast.url} to the library: {e}")

    def get_spotify_client(self):
        # Authorize the app to access the user's Spotify account
        token = util.prompt_for_user_token(self.username,
        scope="user-library-modify",
        client_id=self.client_id,
        client_secret=self.client_secret,
        redirect_uri=self.redirect_uri)
        return spotipy.Spotify(auth=token)

    def add_show_to_library(self, show, sp):
        show_id = show["id"]
        # Add the show to the library
        sp.current_user_saved_shows_add([show_id])
        print(f"Added {show['name']} to your library")

    def import_podcasts(self, opml_file):
        # Parse the opml file to extract the podcast URLs
        
        try:
            root = ET.parse(opml_file).getroot()
        except ET.ParseError as e:
            print(f"Error parsing OPML file: {e}")
            return
        
        podcasts = {}
        for outline in root.iter("outline"):
            # Check if the outline element represents a podcast
            if outline.get("type") == "rss":
                name = outline.get("text")
                url = outline.get("xmlUrl")
                podcasts[name] = url

        # Add the podcasts to the library
        for name, url in podcasts.items():
            # Search for the podcast on Spotify
            podcast = Podcast(name=name, url=url)
            self.search_and_add_podcast(podcast)

        print(f"Successfully processed {len(podcasts)} podcasts")

class Podcast:
    def __init__(self, name, url):
        self.name = name
        self.url = url
