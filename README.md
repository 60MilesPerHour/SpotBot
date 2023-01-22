# SpotBot

SpotBot is a Python script that allows you to download music from Spotify. It takes the share links from Spotify (albums, songs, and playlists) and downloads the corresponding music into the user's specified directory. The bot will create folders for each item (albums, songs, and playlists) and sort the music accordingly.

## Requirements
- Python 3 and the latest version of pip (pip3)
- FFMPEG and SpotDL
- Spotify subscription
- A file named "SpotList.txt" in the desired folder where music will be downloaded to.

## Usage
1. Create a file named "SpotList.txt" in the desired folder where you want to download the music.
2. In the "SpotList.txt" file, enter the Spotify share links in the following format:

Album: Album Name - Artist Name
https://open.spotify.com/album/
Song: Song Name - Artist Name
https://open.spotify.com/song/
Playlist: Playlist Name - Various Artists
https://open.spotify.com/playlist/

3. Run the script using the command: `python3 SpotBot.py`
4. Select the desired bitrate from the listed options (larger the bitrate, larger the file)
5. The bot will start downloading the music and sorting it into the corresponding folders.

## Note
- The bot requires Spotify share links in the specific format shown above in order to work correctly.
- Make sure to have the latest version of FFMPEG and SpotDL installed, otherwise the bot will not work.
- Spotify subscription is required to use this bot.

## Troubleshooting
- If you encounter any errors or issues, please check that you have followed all the instructions correctly and that all dependencies are installed.
- If the problem persists, please open an issue on the GitHub page.

## Contact
If you have any questions or suggestions, please feel free to contact me.

## Disclaimer
This bot is intended for personal use only and should not be used for commercial purposes. Use at your own risk.
