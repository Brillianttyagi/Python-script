# importing ZipFile 
from zipfile import ZipFile 
  
# specifying the zip file name 
file_name = "filename.zip"
  
# opening the zip file in read mode 
with ZipFile(file_name, 'r') as zip: 
    # printing all the contents of the zip file  
    zip.printdir() 
  
    # extracting all the files 
    zip.extractall() 
    print('Done!') 