import shutil 
  
# Path 
path = "C:/"
  
stat = shutil.disk_usage(path) 
  

total = int(stat[0]/1073741824)
used = int(stat[1]/1073741824)
free = int(stat[2]/1073741824)
print(total,"GB")
print(used,"GB")
print(free,"GB")