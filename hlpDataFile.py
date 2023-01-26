import os
from time import time, ctime
from datetime import datetime

class DataFileHelper:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_handle = None
        date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self.file_header = "Fichier d'historique des detections de bourrasques\nCree le : " + str(date) + "\n"

    def initHistory(self):
        if not os.path.isfile(self.file_name):
            self.file_handle = open(self.file_name, "w")
            self.file_handle.write(self.file_header) 
            self.file_handle.close()
        # else:
        #     self.file_handle = open(self.file_name, "a")

    def saveHistory(self, data):
        # open
        self.file_handle = open(self.file_name, "a")
        # write    
        self.file_handle.write(data)
        # close
        self.file_handle.close()

