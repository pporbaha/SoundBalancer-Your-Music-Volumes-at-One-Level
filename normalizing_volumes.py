from pydub import AudioSegment
import os
from moviepy.editor import VideoFileClip

# Copy the Path of the folder containing MP3 and MP4 files here
folder_path = r"C:\My Files\My Music\NES Soundtracks" 


# ===============================================================

target_dBFS = -18  # Set your target dBFS: I have found that -18 is an standard db

# Function to calculate the difference between the current song volume (db) with target standard db
def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS), change_in_dBFS

def check_if_mp4_and_convert_it_to_mp3(filename):
    name, ext = os.path.splitext(filename)
    path = os.path.join(folder_path, filename)
    if ext.lower() == '.mp4':
        video = VideoFileClip(path)
        audio = video.audio
        mp3_path = os.path.join(folder_path, f'{name}.mp3')
        audio.write_audiofile(mp3_path)
        path = mp3_path  # Update path to use the new MP3 file
        video.close()  # Close the video file to free resources
        return path
    
    elif ext.lower()=='.mp3':  # if .mp3 file
        return path
    
def process_and_normalize_the_file(filename):
    if filename.endswith('.mp3') or filename.endswith('.mp4'):
        path = check_if_mp4_and_convert_it_to_mp3(filename)

        # Normalize the MP3 file
        sound = AudioSegment.from_file(path)
        normalized_sound, change_in_dBFS = match_target_amplitude(sound, target_dBFS)

        new_path = os.path.join(folder_path, 'normalized_songs', filename)
        normalized_sound.export(new_path, format='mp3', bitrate="128k", parameters=["-ar", '44100'])
        print(f'{filename} has been normalized by {change_in_dBFS} dBFS!')


def main():
    os.makedirs(os.path.join(folder_path, 'normalized_songs'), exist_ok=True)  # make a new_folder of 'normalized_songs'

    for filename in os.listdir(folder_path):
        process_and_normalize_the_file(filename)

    print("Normalization complete. All MP4 files have been converted and all audio files have been normalized.Enjoy the musics!")

main()