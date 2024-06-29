# SoundBalancer-Your-Music-Volumes-at-One-Level

## Overview
This Python utility addresses the common issue of varying audio levels in music collections. It normalizes the volume of MP3 and MP4 files to a consistent level, making it ideal for listeners who wish to enjoy their music without the need to manually adjust the volume for each track.

## Features
- **Automatic Volume Normalization**: Set a target decibel level for all your audio files.
- **MP4 to MP3 Conversion**: Seamlessly converts MP4 files to MP3 format during the normalization process.
- **Batch Processing**: Processes an entire folder of audio files in one go.

## Prerequisites
Before running this script, ensure you have the following dependencies installed:
- `pydub`
- `moviepy`

You can install them using pip:
pip install pydub moviepy


Additionally, you'll need FFmpeg installed on your system. Follow this [simple tutorial](https://www.wikihow.com/Install-FFmpeg-on-Windows) to set it up.

## Usage
1. Clone the repository or download the script.
2. Place your MP3 and MP4 files in a designated folder.
3. Run the script and specify the path to your music folder.

The script will create a subfolder named `normalized_songs` within your music folder, where it will place all the normalized audio files.

## Code Snippet
Here's a glimpse of the core functionality:


from pydub import AudioSegment
import os
from moviepy.editor import VideoFileClip

# Set your target dBFS (Decibels relative to full scale)
TARGET_dBFS = -18

def match_target_amplitude(sound, target_dBFS):
    # Calculate the required gain adjustment
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS), change_in_dBFS

# ... rest of the code ...


## Contributions
Contributions are welcome! If you'd like to improve the script or add new features, please feel free to fork the repository and submit a pull request.

## License
This project is open-sourced under the MIT License. See the LICENSE file for more details.


This README provides a clear introduction and instructions for your project. I've included a brief code snippet to showcase the functionality. If you have any specific requirements or sections you'd like to add, please let me know!
Pedram Porbaha
p.porbaha@gmail.com
