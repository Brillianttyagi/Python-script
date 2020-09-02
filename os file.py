import os 
for filename in os.listdir("."): #for current directory 
	if filename.startswith("("): 
		os.rename(filename, filename[5:]) 