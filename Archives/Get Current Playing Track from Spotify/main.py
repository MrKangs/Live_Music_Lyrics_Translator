from pprint import pprint
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import os.path


# TODO: Add a pop up for the user to enter the url link on a box if their are linking up their account for the first time, else ignore it --> this should run in the back
# When I use the terminal to run it, it never ask it. Need to try someone to run it


def create_spotify_api():
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="fd435a4fa71949f2a235179ff3ef3010", client_secret= "4bb5c3ce498847bfbdfde31c3e615080", redirect_uri="https://open.spotify.com", scope="user-read-playback-state, user-modify-playback-state"))
    return spotify

def open_web_spotify_player():
    webbrowser.open("https://open.spotify.com")

def get_authorization_for_users(spotify_api):
    # Filter out if the User provided authorization or not
    # Will be good block to add the pop-up part here so that the user needs what to do
    # Maybe providing a sign that the user needs to run it on the terminal 
    url = spotify_api.auth_manager.get_authorize_url()
    webbrowser.open(url)
    print("Enter the URL you got.")
    user_input = input("It should start as https://open.spotify.com/?code=:")
    # This will get it from the pop-up with URL entery text box
    code = spotify_api.auth_manager.parse_response_code(user_input)
    spotify_api.auth_manager.get_access_token(code)


def get_current_track(spotify_api):
    
    responses_json = spotify_api.current_user_playing_track()

    if responses_json is None:
        print("Please play a song on Spotify")
        return False

    track_name = responses_json['item']['name']
    artists = responses_json['item']['artists']
    artist_names = ', '.join([artist['name'] for artist in artists])


    current_track_info = {
        "name": track_name,
        "artists": artist_names
    }

    return current_track_info


def main():
    
    spotify = create_spotify_api()

    if os.path.exists(spotify.auth_manager.cache_handler.cache_path) is False:
        get_authorization_for_users(spotify)
    else:
        open_web_spotify_player()

    while True:
        current_track_info = get_current_track(spotify)

        # if current_track_info is false, then give a pop up --> make sure when the user close it the pop-up, it will continue the loop

        pprint(current_track_info)

        time.sleep(1)


if __name__ == '__main__':
    main()