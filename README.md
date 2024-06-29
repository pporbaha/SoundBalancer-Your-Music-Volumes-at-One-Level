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
2. Place your MP3 and MP4 files in a folder.
3. open the code "normalizing_volumes.py" by mouse right click and open with notepad
4. find this line in the code: folder_path = r"C:\My Files\My Music\NES Soundtracks"
5. paste your folder path between "" signs
6. save the file
7. Run the script and enjoy!

The script will create a subfolder named `normalized_songs` within your music folder, where it will place all the normalized audio files.

## Contributions
Contributions are welcome! If you'd like to improve the script or add new features, please feel free to fork the repository and submit a pull request.

## License
This project is open-sourced under the MIT License. See the LICENSE file for more details.


If you have any specific requirements or sections you'd like to add, please let me know!
Pedram Porbaha
p.porbaha@gmail.com
