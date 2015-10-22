import threading
import thread


def cdquit(*fn_name):
    thread.interrupt_main()  # raises KeyboardInterrupt


def exit_after(s):
    '''
    use as decorator to exit process if 
    function takes longer than s seconds
    '''

    def outer(fn):
        def inner(*args, **kwargs):
            timer = threading.Timer(s, cdquit, fn.__name__)
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
            return result

        return inner

    return outer
