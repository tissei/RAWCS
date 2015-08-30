import time

class Timer(object):
    def __init__(self, iterations=1, verbose=False):
        """
        Timer class constructor

        :param iterations: Amount of iterations executed
        :type: int
        :param verbose: Determines if the time lapse will be automatically printed
        :type: boolean
        """
        self.verbose = verbose
        self.iterations = iterations

    def __enter__(self):
        """
        Executed on the opening of a with tag

        :return: Timer object instance
        :rtype : Timer
        """
        self.start = time.time()
        return self

    def __exit__(self, *args):
        """
        Executed on the end of a with tag

        :param args: None
        """
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print 'elapsed time: %f ms' % (self.msecs / self.iterations)
