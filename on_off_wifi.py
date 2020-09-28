import os 
import subprocess
def enable():
    result = subprocess.run(["netsh", "interface", "set", "interface", "deep", "ENABLED"])
    print("FAILED..." if result.returncode else "SUCCESS!")

def disable():
    result = subprocess.run(["netsh", "interface", "set", "interface", "deep", "DISABLED"])
    print("FAILED..." if result.returncode else "SUCCESS!")

e = input("enter  ")
os.system("netsh interface show interface")
if e=="on":
    enable()
elif e=="off":
    disable()