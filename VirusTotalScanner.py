"""
A simple script to scan a file for virus online, Using VirusTotal API.

Author: Shivam Saini (https://github.com/shivamsn97)

Usage:
python VirusTotalScanner.py /path/to/yourfile

Installation:
pip install colorama
pip install vt-py

Login to https://www.virustotal.com/gui/, create an account, get your API key, and Paste that key down, in the API_KEY variable.

For a more detailed solution, and adding this script to your context menu, check out the main repo at https://github.com/shivamsn97/ScanIt

"""

API_KEY = "PLACE_YOUR_API_KEY_HERE"   


import vt
import argparse
import os
import hashlib, time
import colorama
import time

colorama.init(convert=True)

def check_file_exists(given_path):
    if not os.path.isfile(given_path):
        raise argparse.ArgumentTypeError(f"{given_path} is not a valid file. Make sure you are trying to scan only file, not directory.")
    return given_path

def print_result(stats, file_path):
    print(colorama.Fore.MAGENTA)
    print("Scan Results for file named {}".format(file_path.split(os.sep)[-1]))
    print("-------------------------------------------------------"+colorama.Fore.RESET)
    for i in stats:
        print((colorama.Fore.RED if i in ["suspicious", "malicious"] else colorama.Fore.GREEN if i in ["harmless", "undetected"] else colorama.Fore.CYAN) + i + colorama.Fore.RESET + ": {}".format(stats[i]))
    print(colorama.Fore.MAGENTA + "-------------------------------------------------------")
    print("Verdict: \n" + colorama.Fore.RESET)
    num_safe = stats["harmless"] + stats["undetected"]
    num_unsafe = stats["suspicious"] + stats["malicious"]
    if num_unsafe == 0 and num_safe >= 20:
        print(colorama.Fore.GREEN + "TOTALLY SAFE" + colorama.Fore.RESET)
    elif num_unsafe == 0 and num_safe >=5:
        print(colorama.Fore.GREEN + "SAFE" + colorama.Fore.RESET)
    elif num_unsafe == 0 and num_safe:
        print(colorama.Fore.LIGHTGREEN_EX + "UNKNOWN" + colorama.Fore.RESET)
    elif num_unsafe == 0:
        print(colorama.Fore.YELLOW + "UNKNOWN" + colorama.Fore.RESET)
    elif num_safe > num_unsafe:
        print(colorama.Fore.LIGHTGREEN_EX + "UNKNOWN" + colorama.Fore.RESET)
    elif num_safe == 0:
        print(colorama.Fore.RED + "VERY UNSAFE" + colorama.Fore.RESET)
    else:
        print(colorama.Fore.RED + "UNSAFE" + colorama.Fore.RESET)
    print(colorama.Fore.MAGENTA + "-------------------------------------------------------" + colorama.Fore.RESET)
    
parser = argparse.ArgumentParser()
parser.add_argument("filepath", help="Path of the file you want to scan.", type=check_file_exists)
args = parser.parse_args()
file_path = args.filepath

with open(file_path,"rb") as f:
    bytes = f.read() # read entire file as bytes
    file_hash = hashlib.sha256(bytes).hexdigest()

with vt.Client(API_KEY) as client:
    try:
        print("Checking if file already available in VirusTotal DB.", end="")
        stats = client.get_object("/files/{}".format(file_hash)).last_analysis_stats
        print("\rFile is already available in VirusTotal DB")
    except vt.error.APIError as ex:
        if not ex.code == "NotFoundError":
            raise
        with open(file_path, "rb") as f:
            choice = input("\rFile not available in VirusTotal DB. Do you want to upload? (Internet charges may apply) (Y/N)\n :: ")
            if choice.lower() in ["y", "yes"]:
                print(colorama.Fore.GREEN + "Now Uploading. ")
                analysis = client.scan_file(f)
                while True:
                    analysis = client.get_object("/analyses/{}".format(analysis.id))
                    print("\r" + colorama.Fore.MAGENTA +  "Current Status: " + colorama.Fore.RESET + analysis.status, end="")
                    if analysis.status == "completed":
                        break
                    time.sleep(10)
                stats = analysis.stats
            else:
                print("Operation cancelled. ")
                time.sleep(2)
                exit()

    print_result(stats, file_path)
    input("Press enter to exit...")
