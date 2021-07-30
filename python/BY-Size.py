import os
import shutil
from pathlib import Path
import bydate as ti
import random
import time
    


    

def sizecheck(folderpath):

    print("File Organizing in progress by size of files, Please wait...")
    wait_time = random.randint(1,30)
    time.sleep(wait_time)
    list_dir=os.walk(folderpath)
    for dir,filename, file in list_dir:
        for f in file:
            sizeoffile=os.stat(dir+"/"+f).st_size
            try:
                if sizeoffile < 1024:
                    if os.path.exists(folderpath+"/Byte_Files/"):
                        shutil.move(folderpath+"/"+f, folderpath+"/Byte_Files/"+f)
                    else:
                        os.mkdir(folderpath+"/Byte_Files/")
                        shutil.move(folderpath+"/"+f, folderpath+"/Byte_Files/"+f)
                elif sizeoffile >= 1024 and sizeoffile < 1000*1024:
                    if os.path.exists(folderpath+"/KiloBytes_Files/"):
                        shutil.move(folderpath+"/"+f, folderpath+"/KiloBytes_Files/"+f)
                    else:
                        os.mkdir(folderpath+"/KiloBytes_Files/")
                        shutil.move(folderpath+"/"+f, folderpath+"/KiloBytes_Files/"+f)
                elif sizeoffile >= 1000*1024 and sizeoffile <= 1000*1024*1024:
                    if os.path.exists(folderpath+"/MegaBytes_Files/"):
                        shutil.move(folderpath+"/"+f, folderpath+"/MegaBytes_Files/"+f)
                    else:
                        os.mkdir(folderpath+"/MegaBytes_Files/")
                        shutil.move(folderpath+"/"+f, folderpath+"/MegaBytes_Files/"+f)
                else:
                    if os.path.exists(folderpath+"/GigaBytes_Files/"):
                        shutil.move(folderpath+"/"+f, folderpath+"/GigaBytes_Files/"+f)
                    else:
                        os.mkdir(folderpath+"/GigaBytes_Files/")
                        shutil.move(folderpath+"/"+f, folderpath+"/GigaBytes_Files/"+f)
            except FileExistsError:
                continue
    print("File organizing completed by Size.")
