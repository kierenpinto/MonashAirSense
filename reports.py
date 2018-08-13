#Results Relay
import csv
import datetime
import time
import os
import errno
class Report:
    def __init__(self,path,date,time):
        self.Events = []
        self.filename = path + '/data/' + date + '/' + time + '.csv'

    def addEvent(self,eventInfo):
        self.Events.append(eventInfo)

    def save(self):
        if not os.path.exists(os.path.dirname(self.filename)):
            try:
                os.makedirs(os.path.dirname(self.filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        with open(self.filename, 'wb') as f:
            reswrite = csv.writer(f, delimiter = ',')
            for item in self.Events:
                if type(item)==dict:
                    info = []
                    for key in item:
                        info.append(key)
                        info.append(item[key])
                    reswrite.writerow(info)
                elif type(item)==str:
                    reswrite.writerow([item])
                else:
                    raise Exception('Wrong Type... needs to be dict or string')

