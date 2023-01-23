import os
from time import time, ctime

class DataFileHelper:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file_handle = None
        date = ctime(time)
        self.file_header = "Créé le : " + str(date) + "\n"
    
    def open(self):
        if not os.path.isfile(self.file_name):
            self.file_handle = open(self.file_name, "w")
            self.file_handle.write(self.file_header)
        else:
            self.file_handle = open(self.file_name, "a")
    
    def write(self, data):
        self.file_handle.write(data)

data_file_helper = DataFileHelper("history.txt")
#On fera une boucle pour l'écriture à l'intérieur du fichier et eviter les doiublons pour les différentes valeurs
#l'enregistrement se fera sous format : DD/MM/YYYY TIME SPEED CARDINAL POINT
data_file_helper.open()
data_file_helper.write("Detection de bourrasque : " + str((ctime())) + "\n")
data_file_helper.close()