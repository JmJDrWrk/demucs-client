import requests
import json
import pprintpp as Print
import wget
import runner as runner
import shutil
max_file_size = 10
server = 'https://demucsmaster.jmjdrwrk.repl.co'

def publish(body):
    response = requests.post(f'{server}/publish',data=body)
    print(response.status_code)

def run():
    res = requests.get('https://demucsmaster.jmjdrwrk.repl.co/stack')
    stack = json.loads(res.text)
    for task in stack:
        file_name = task['name']
        file_size = int(task['size'])/1000000
        file_mimetype = task['mimetype']
        if(file_size<=max_file_size):
            print(f'\nChecking {file_name}')
            print('\tFile Size [OK]')
            print('\tFile mimetype [OK]')

            print('===================DOWNLOADING beta========================')
            #res_file = wget.download(f'https://demucsmaster.jmjdrwrk.repl.co/src/{file_name}')
            r = requests.get(f'https://demucsmaster.jmjdrwrk.repl.co/src/{file_name}', allow_redirects=True)
            with open(f'input/{file_name}', 'wb') as opened:
                opened.write(r.content)
            
            #print('\n===================MOVING===========================')
            #shutil.move(f"{file_name}", f"input/{file_name}")


            print('\n @@ RUNNING DEMUCS AUTOMAGIC @@ ')
            output = runner.demucs_separate(file_name,'output','')
            
            print('\n@@ Publishing changes to server @@')
            publish({"success":True,"output":output,"originalfile":stack,"newfiles":"soon"})

# TEST #    

# stack = {
#     "file_name":"The name of the file",
#     "file_size":"The size of the file",
#     "file_mimetype":"The mimeype of the file"
# }
    
# print('\n @@ RUNNING DEMUCS AUTOMAGIC @@ ')
# output = runner.demucs_separate('file_name','output','')
# publish({"success":True,"output":output,"originalfile":stack,"newfiles":"soon"})