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
    
#.windows-build-tools\python27\python.exe No module named demucs
    #Clone demucs repo git clone https://github.com/facebookresearch/demucs
def demucs_separate(input,output,compute_with):
    command_output = os.popen(rf'python.exe -m demucs.separate {compute_with} -o "C:\Users\jroman\Documents\GitHub\demucs-client\output" "C:\Users\jroman\Documents\GitHub\demucs-client\input\{input}"').read()
    print(command_output)
    return command_output

def test_demucs_separate(a,b,c):
    return 'Supossing all worked fine'