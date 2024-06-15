import time
def FilenameByTime(directory):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    filename = directory+"/"+timestr+"_.png"
    return filename    
