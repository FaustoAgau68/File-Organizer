import shutil
import os
import zipfile

class FileOrganizer:
    def check_dst_folder(self, dst):
        if not os.path.exists(dst):
            print("Folder does not exist !! Created one.")
            new_dst_folder = os.makedirs(dst)
            return new_dst_folder
        return dst
    
    def totalfile(self, file):
        pass

    def compress_file(self, src, folder_src):
        with zipfile.ZipFile(src, 'r') as zip_file:
            zip_file.extractall(path=folder_src)
            print("RAR extraction Complete.")
        os.remove(src)
            
                

    def file_organizer(self, folder_src, folder_dst):
        files = os.listdir(folder_src)  # reading and storing file in list data type
        for file in files:
            src = os.path.join(folder_src, file)
            file_extentions = os.path.splitext(file)[1]

            if file_extentions.lower() == ".zip":
                self.compress_file(src, folder_src)

            if file_extentions == ".pdf":
                subdir = os.path.join(folder_dst, "PDF")
                os.makedirs(subdir, exist_ok=True)
                dst = os.path.join(subdir, file)
                shutil.move(src, dst)
            elif file_extentions.lower() in [".docx", ".pptx", ".xlsx", ".doc", ".csv",".txt"]:
                subdir = os.path.join(folder_dst, "Doc")
                os.makedirs(subdir, exist_ok=True)
                dst = os.path.join(subdir, file)
                shutil.move(src, dst)
            elif file_extentions.lower() in [".jpeg",".png", ".gif", ".svg", ".bmp", ".jpg", ".jfif"]:
                subdir = os.path.join(folder_dst, "Image")
                os.makedirs(subdir, exist_ok=True)
                dst = os.path.join(subdir, file)
                shutil.move(src, dst)
            else:
                subdir =os.path.join(folder_dst, "Apps & Others")
                os.makedirs(subdir, exist_ok=True)
                dst = os.path.join(subdir, file)
                shutil.move(src, dst)




    