import threading


def runInBackground(backgroundf):
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

    call_function()