import os
import sys

#pip install demucs

#No audio backend avaliable
    #pip install ffmeg
    #pip install PySoundFile

# When trying to load using ffmpeg, got the following error: Ffmpeg is not installed.
    #https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z
    #Move ffmeg and rename as ffmpeg
    #Open Admin Console and C:\WINDOWS\system32>setx /m PATH "C:\ffmpeg\bin;%PATH%"

def demucs_separate(input,output):
    command_output = os.popen(f'python.exe -m demucs.separate -d cpu -o "U:\Demucs\output" U:\Demucs\input\{input}').read()
    print(command_output)

