import threading
import asyncio
import time
import threading

from runInBackground import runInBackground


def backgroundf():
    while True:
        print('I am running in Background')
        time.sleep(3)

def runOnMain():
    for i in range(10):
        print(i)






def background(f):
    '''
    a threading decorator
    use @background above the function you want to run in the background
    '''
    def backgrnd_func(*a, **kw):
        threading.Thread(target=f, args=a, kwargs=kw).start()
    return backgrnd_func

@background
def call_function():
    backgroundf()

# start the background function
# note that with the @background decorator
# background function executes simultaneously

# runOnMain()
# call_function("Background Function One", 6)




async def runBothFunction():
    runOnMain()
    await runInBackground(backgroundf)
    runOnMain()


await runBothFunction()