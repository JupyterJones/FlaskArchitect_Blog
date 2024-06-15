#!/home/jack/miniconda3/envs/cloned_base/bin/python
import os
import random
import pygame

def get_mp3_files(directory):
    """Return a list of MP3 files in the given directory."""
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.mp3')]

def play_playlist(playlist):
    """Play a list of MP3 files."""
    pygame.mixer.init()
    for track in playlist:
        print(f"Now playing: {track}")
        pygame.mixer.music.load(track)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Wait for the music to finish playing

def main(directory):
    # Replace with the path to your MP3 directory
    mp3_files = get_mp3_files(directory)

    if not mp3_files:
        print("No MP3 files found in the specified directory.")
        return

    print("Found the following MP3 files:")
    for mp3 in mp3_files:
        print(mp3)

    # Shuffle the playlist
    random.shuffle(mp3_files)

    print("\nPlaying shuffled playlist...")
    play_playlist(mp3_files)

if __name__ == '__main__':
    directory = '/home/jack/Desktop/newest_chatgpt/static/music/'  
    main(directory)
# Path: playmusic.py