import os
import shutil
from pathlib import Path
import bydate as ti
import random
import time

def sort_exten(path):
  print("File work in progress.....")
  wait_time = random.randint(1,30)
  time.sleep(wait_time)
  all_extension = {
    'image' : [".jpeg", ".jpg",".JPG",".jpg#",".odg",".JPG#",".odg#",".ODG#",".TIF", ".gif", ".bmp", ".png", ".bpg", ".svg","heif", ".psd"],
    'videos' : [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
    'audio' :  [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    'docs' : [".pdf",".docs",".docx",".doc",".pdf",".PDF",".pptx"],
    'program' : [".exe",".py",".zip",".deb",".html",".htm",".epub",".gz",".iso",".odp"],
    'excel' : [".xls",".xlsx"]
    }
  All_files =os.listdir(path)

  FILE_FORMATS = {file_format: directory
          for directory, file_formats in all_extension.items()
          for file_format in file_formats}

  for file in All_files:
    name, extension = os.path.splitext(path+'//'+file)
    if extension == '':
      continue
    folder_name = ''
    for key,values in all_extension.items():
      if extension in values:
        folder_name = key
        break
    if os.path.isdir(path + '//' + folder_name):
      pass
    else:
      os.makedirs(path + '//' + folder_name)
    source = path+'//'+file  
    dest = path+'//'+folder_name
    shutil.move(source, dest)
  print("File organizing completed.")
  
  
  
  
  
  
