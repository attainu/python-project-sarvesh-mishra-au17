import os 
import shutil
import random
import time
import datetime
from datetime import datetime


def bydate(path):
    print("File Organizing in progress by size of files, Please wait...")
    wait_time = random.randint(1,30)
    time.sleep(wait_time)
    lis = os.listdir(path)
    lis.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
    files = [f for f in os.listdir(
        path) if os.path.isfile(os.path.join(path, f))]
    os.chdir(path)

    for x in files:
    

        modified_time = time.ctime(
            os.path.getmtime(os.path.join(path, x)))

        modified_datetime = datetime.strptime(
         modified_time, '%a %b %d %H:%M:%S %Y')

        modified_date = str(modified_datetime.day) + '-' + str(
         modified_datetime.month) + '-' + str(modified_datetime.year)

        if(os.path.isdir(modified_date)):
            shutil.move(os.path.join(path, x), modified_date)
        else:
            os.makedirs(modified_date)
            shutil.move(os.path.join(path, x), modified_date)
    print("File organizing completed by Size.")
    
    
    
    
    
    
    
    
    
    
