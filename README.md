# OpmlSpotPy
OpmlSpotPy is a command-line tool that allows you to import podcasts from an OPML file into your Spotify library.

## Getting Started

### Prerequisites

- Python 3.9 (did not test on other versions)
- [pip](https://pip.pypa.io/en/stable/installing/)
- A Spotify account
- A Spotify app with the `user-library-modify` scope enabled
  - A Spotify API `client ID` and `client secret`
  - App callback configured to `http://localhost:8000/callback`
- OPML file with podcasts to import (tested on PocketCasts export)

### Installing

#### 1. Clone this repository

```bash
git clone https://github.com/Amoenus/OpmlSpotPy
```

#### 2. Install dependencies

```bash
pip install -r requirements.txt
```

#### 3. Create a copy of the .env-template file and rename it to .env

```bash
cp .env-template .env
```

#### 4. Fill in the values in the .env file with your own client ID, client secret, and redirect URI, which you can obtain by [creating a new Spotify app](https://developer.spotify.com/dashboard/applications)

> To find your Spotify username:
>
> - Open the Spotify app on your device.
> - Click on the settings icon in the top right corner.
> - Click on the Account tab.
>
> Your username will be displayed under the Username  heading.
> Alternatively, you can find your username by visiting your Spotify profile page on the web and looking for the `https://open.spotify.com/user/` portion of the URL. The string of characters that follows `/user/` is your Spotify username.

Create a file named `.env` in the root of the project and add the following environment variables:

```text
OPMLSPOT_CLIENT_ID=your-client-id
OPMLSPOT_CLIENT_SECRET=your-client-secret
OPMLSPOT_REDIRECT_URI=http://localhost:8000/callback
OPMLSPOT_USERNAME=your-spotify-username
```

Replace `your-client-id`, `your-client-secret`, and `your-spotify-username` with your own values.

#### 5. Run the app

```bash
python app.py
```

### Usage

- Put OPML file as podcasts.opml in the same directory as `app.py`
- Run the app
- Follow the prompts to authenticate the app with your Spotify account
- The app will import the podcasts from the file to your saved shows asking occationaly whether to import fuzzy matches
