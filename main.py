from pytube import Playlist
import os
from pytube import YouTube

# URL of the playlist


def check_playlist(url):
    str = url.split('?')
    str1 = str[0].split('/')
    # print(str1[3])
    if str1[3] == "watch":
        return 1
    elif str1[3] == "shorts":
        return 2
    else:
        return 3

def download_video(url):

    if check_playlist(url) == 3:
        # Create a Playlist object
        playlist = Playlist(url)

        # Get the playlist name
        playlist_name = playlist.title

        # Create the folder for the playlist if it doesn't exist
        if not os.path.exists(playlist_name):
            os.makedirs(playlist_name)

        # Download each video in the playlist and save it in the playlist folder
        for video in playlist.videos:
            video.streams.get_highest_resolution().download(output_path=playlist_name)
    
    elif check_playlist(url) == 2:

        yt = YouTube(url)

        # Get the highest resolution stream
        stream = yt.streams.filter(file_extension='mp4').first()

        # Download the video
        stream.download()

    else:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download()



playlist_url = input("Paste the Link here .... ")
download_video(playlist_url)