import os
import shutil
class Folder_Organizer:
    def __init__(self):
        self.path = str(input("Write the absolete path of the folder you want to organize: ")) #"/home/pablitox/Downloads/Nordvpn"
        if self.path[-1] != '/':
            self.path = self.path + '/'
        self.dir_list = []

    def start(self):
        if os.path.exists(self.path):
            for file in os.listdir(self.path):
                file_path = self.path + file
                if os.path.isfile(file_path):
                    if file.rfind(".") != -1:
                        extention = file[file.rfind(".")+1:].upper()
                        if extention not in self.dir_list:
                            self.dir_list.append(extention)
                            os.mkdir(self.path + extention)
                            shutil.move(file_path, self.path + extention)
                        else:
                            shutil.move(file_path, self.path + extention)
        else:
            print("The path you entered does not exist or there are errors in the path")

if __name__ == "__main__":
    new = Folder_Organizer()
    new.start()