
print('Hello World')
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


print('\n Type install  to install modules, Test to test and enter to skip')
a = input('[  ]\n')
if(a=='install'): 
  #print('Ensure you have pip install demucs as -u demucs')
  #pip_install('pip install -U git+https://github.com/facebookresearch/demucs#egg=demucs')
  print('1. INSTALLING PySoundFile and PySound')
  
  pip_install('PySoundFile')
  pip_install('PySound')
  
  print('\n2. INSTALLING pprintpp, requests, wget')    
  pip_install('pprintpp')
  pip_install('requests')
  pip_install('wget')
  
elif(a=='test'):
  import client as cliente
  from time import sleep
  import requests
  import json
  import pprintpp as Print
  import wget
  import runner as runner
  import shutil
  import sys
else:
  print('install skipped')



