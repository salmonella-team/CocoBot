import os
import glob

def fetch_file_size(file_name):
    file_name = [os.path.basename(p) for p in glob.glob('./tmp/' + file_name + "*", recursive=True) if os.path.isfile(p)]
    file_size = os.path.getsize('./tmp/' + file_name[0])
    return file_size