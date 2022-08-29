import client as cliente
from time import sleep
while True:
    try:
        cliente.run()       
        print('-->End of the task next in 5 seconds')
        sleep(5)
    except Exception as e:
        print(e)
        print('\n ## ERROR--> RETRYING after 2 sec## \n')
        sleep(2)