import client as cliente
from time import sleep
while True:
    try:
        cliente.run()       
        print('-->End of the task next in 5 seconds')
        sleep(5)
    except Exception as e:
        print('...')
        #print(e)
        #print('\n ## ERROR--> RETRYING after 2 sec## \n')
        sleep(2)


#IMPLEMENT A TIMEOUT
import time
timeout = time.time() + 60*5   # 5 minutes from now
while True:
    test = 0
    if test == 5 or time.time() > timeout:
        break
    test = test - 1
    
#IMPLEMENT A ZIP FUNCTION

#IMPLEMENT A OS.POPEN ERROR CONTROLLER ON RUNNER.py

#IMPLEMENT A 