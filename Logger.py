import sys


class Logger:
    def __init__(self, filename="logfile.txt"):
        self.logfile = open(filename, "w")
        self.stdout = sys.stdout

    def write(self, message):
        self.stdout.write(message)
        self.logfile.write(message)

    def flush(self):
        self.stdout.flush()
        self.logfile.flush()
