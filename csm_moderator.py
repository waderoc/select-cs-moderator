import pandas as pd
import random
import time
from colorama import Fore, Style

csm = pd.read_csv (r'./csm.csv')   
csm_list = pd.DataFrame(csm, columns= ['First Name', 'Last Name', 'Area'])
print ("\n\n\nSelecting a random CSM (Primary and Secondary) to moderate the next meeting in...\n\n\n")
time.sleep(2)
print ("               5\n\n\n")
time.sleep(1)
print ("               4\n\n\n")
time.sleep(1)
print ("               3\n\n\n")
time.sleep(1)
print ("               2\n\n\n")
time.sleep(1)
print ("               1\n\n\n")
time.sleep(1)
print (Fore.MAGENTA)
print (csm_list.sample(2))
print (Style.RESET_ALL)
