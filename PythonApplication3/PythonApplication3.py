import sys
from datetime import datetime

class Logger:
    def __init__(self, out_stream=sys.stderr, time_formatter='%Y-%m-%d %H:%M:%S'):
        self.out_stream = out_stream
        self.time_formatter = time_formatter

    def log(self, message):
        timestamp = datetime.now().strftime(self.time_formatter)
        print(f"[{timestamp}] {message}", file=self.out_stream)

