import subprocess
import os
from termcolor import colored

FNULL = open(os.devnull, 'w')

os.chdir(os.getcwd())
files = subprocess.check_output(["ls"], universal_newlines=True).splitlines()
for i in files:
    if i.find(".sfv") != -1:
        try:
            if subprocess.call(["cksfv", "-g", i], stdout=FNULL, stderr=subprocess.STDOUT) == 0:
                print(colored("Everything good!", "green"))
            else:
                subprocess.check_output(["cksfv", "-g", i])
        except subprocess.CalledProcessError:
            print("Sorry that you encountered errors in your files :|")
