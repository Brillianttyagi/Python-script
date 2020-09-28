import psutil
used_percentage = int(psutil.virtual_memory().percent)
available = int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
print("used=",used_percentage,"%","available=",available,"%")