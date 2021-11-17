# Song Lyrics Fetcher

This microservice will fetch the music lyrics based on the user input of song name and artist name.
It will be using the Genius API to get information about the lyrics of the song. In other words, if the lyrics seems incorrect, then it is most likely from the Genius API. To use this service, you need to follow the steps below:

1. Make sure you have installed Python 3.x

2. In the terminal, type ```pip install -r requirments.txt```

3. Search Genius API and read the [documentation](https://docs.genius.com/#/getting-started-h1). At the same make sure you aknowledge the term and service of the Genius API.

4. Create an account for Genius in order to create a new API client.

5. Once you create the account, fill out the App Name and App Website URL. The others can be left as blank, but if you want to add redirect url or icon url, you may also do that as well.

6. Click Generate Access Token in the API Client that you created.

7. Copy the client token and paste it inside the get_song_lyrics.py file where the variable name is ```CLIENT_ACCESS_TOKEN```.

8. Once that is complete, it should be able to use the token you generated to get the song lyrics information.
