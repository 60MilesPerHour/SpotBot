#!/usr/bin/env python3.8
import re
import os

spotify_list = open('/home/USER/Music/SpotList.txt', 'r')
bitrate = str(input('Enter the bitrate you want to download the music at (128k, 256k, 320k): '))
os.chdir('/home/USER/Music')
music = []
for line in spotify_list:
    if line.startswith('Album: ') or line.startswith('album: '):
        music.append(line[7:-1].rstrip())
        continue
    elif line.startswith('Playlist: ') or line.startswith('playlist: '):
        music.append(line[10:-1].rstrip())
        continue
    elif line.startswith('Song: ') or line.startswith('song: '):
        music.append(line[6:-1].rstrip())
        continue
    else:
        continue
spotify_links = []
with open("/home/USER/Music/SpotList.txt", 'r') as file:
        for line in file:
            albums = re.findall('https://open.spotify.com/album/.*', line)
            playlists = re.findall('https://open.spotify.com/playlist/.*', line)
            songs = re.findall('https://open.spotify.com/track/.*', line)
            for url in albums:
                spotify_links.append(url)
                continue
            for url in playlists:
                spotify_links.append(url)
                continue
            for url in songs:
                spotify_links.append(url)
                continue
            continue
for i in range(len(music)):
    os.mkdir(music[i])
for i in range(len(music)):
    os.chdir(music[i])
    print('Downloading ' + music[i] + '...' + '\n')
    os.system('spotdl ' + spotify_links[i] + ' --bitrate ' + bitrate)
    os.chdir('..')
    os.system('clear')
spotify_list.close()
