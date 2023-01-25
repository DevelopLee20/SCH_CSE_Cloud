import time
import os

def file_edit_name(instance, filename):
    int_time = str(int(time.time()))
    ext = os.path.splitext(filename)[1]
    new_name = int_time + ext
    
    return new_name