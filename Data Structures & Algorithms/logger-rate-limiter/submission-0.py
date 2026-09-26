"""
hash map to store: message -> timestamp

if entry is new = add to map and record timestamp
otherwise if record ts + 10 > timestamp then false
in true case we update record 
"""


class Logger:

    def __init__(self):
        self.logs = {} 

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logs:
            self.logs[message] = timestamp
            return True

        if self.logs[message] + 10 > timestamp:
            return False
        else:
            self.logs[message] = timestamp 
            return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
