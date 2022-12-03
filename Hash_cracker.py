
"""
Python HASH CRACKER

Author: Mohammad Mahdi Rabiee
Created: Friday, December 2, 2022
"""

import base64
from colorama import Fore
import pyfiglet
import os

__author__ = 'Mohammad Mahdi Rabiee'


os.system("CLS")
SplashScreen = pyfiglet.figlet_format("HASH CRACKER")
print(Fore.BLUE + SplashScreen + Fore.WHITE)

Menu = ''' 
[1] : ENCODE (B64ENCODE)
[2] : DECODE (B64DECODE)
[3] : EXIT '''
print(Menu)

while True:
    InpHashing = int(input("\nCHOOSE OPTIONS: "))
    if (InpHashing == 1):
        ENCODEING = input(Fore.CYAN + "\nENCODEING: ENTER THE HASH: ")
        encoded = base64.b64encode(ENCODEING.encode())

        encoded_edited = f"\nENCODED: {encoded}"
        print(Fore.GREEN + f"ENCODED: {encoded_edited[11:]}" + Fore.WHITE)

    elif (InpHashing == 2):
        DECODEING = input(Fore.CYAN + "\nDECODEING: ENTER THE HASH: ")
        decoded = base64.b64decode(DECODEING.encode())

        decoded_edited = f"\nDECODED: {decoded}"
        print(Fore.GREEN + f"DECODED: {decoded_edited[11:]}" + Fore.WHITE)

    elif (InpHashing == 3):
        exit()

    else:
        print(Fore.RED + "ERROR." + Fore.WHITE)
