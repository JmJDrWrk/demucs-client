import os
print('....Upgrading python pip')
print(os.popen('python.exe -m pip install --upgrade pip').read())

print('\n ***Run it again if wget fails the first time***\n')

def pip_install(lib):
    try:
        print(os.popen(f'pip install {lib}').read())
    except Exception as e:
        print(f'Error installing {lib}')

pip_install('wget')
import wget
print('Ensure you have pip install demucs as -u demucs')
pip_install('pip install -U git+https://github.com/facebookresearch/demucs#egg=demucs')
print('1. INSTALLING PySoundFile and PySound')

pip_install('PySoundFile')
pip_install('PySound')

print('\n2. INSTALLING pprintpp, requests, wget')    
pip_install('pprintpp')
pip_install('requests')
pip_install('wget')


print('2. DOWNLOADING the ffmpeg file')

#wget.download('https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-full.7z')

print('3. You must follow this steps with the downloaded folder:')
instros = '''
1. Unzip file and change the name of the FILE INSIDE to ffmpeg
2. Copy the ffmpeg folder only to the C:\Windows 
3. Open a terminal/cmd in admin mode and type: C:\WINDOWS\system32>setx /m PATH "C:\ffmpeg\bin;%PATH%"
4. Check with ffmpeg -version that something diferent from unreconized command happens
5. IMPORTANT!! Restart Computer !!
'''
print(instros)
    
