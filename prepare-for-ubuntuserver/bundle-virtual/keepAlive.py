import client as cliente
from time import sleep
print('\nCLIENT [running]\n')
times = 0
while True:
    try:
        cliente.run()       
        print('-->End of the task next in 5 seconds')
        sleep(5)
    except Exception as e:
        print("", end=f"\rNot any Task Attempts: {times} times")
        #print(e)
        #print('\n ## ERROR--> RETRYING after 2 sec## \n')
        sleep(2)
    finally:
      times += 1