import string 
import random
import time
import getpass
from turtle import color
import colorama
run = False
walletNum = ""
win = random.randint(2,10)
code = 0
print(colorama.Fore.YELLOW + """
░█████╗░░█████╗░░██████╗██╗░░██╗███╗░░░███╗██╗███╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██║░░██║████╗░████║██║████╗░██║██╔════╝██╔══██╗
██║░░╚═╝███████║╚█████╗░███████║██╔████╔██║██║██╔██╗██║█████╗░░██████╔╝
██║░░██╗██╔══██║░╚═══██╗██╔══██║██║╚██╔╝██║██║██║╚████║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║██████╔╝██║░░██║██║░╚═╝░██║██║██║░╚███║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝
""" + colorama.Fore.RESET)
key = getpass.getpass("Paste license key:")
if key == "rspmfedcstfmvnjifzevumklctzlxlho":
    print(colorama.Fore.MAGENTA + """
██╗░░██╗███████╗██╗░░░██╗  ██╗░░░██╗░█████╗░██╗░░░░░██╗██████╗░
██║░██╔╝██╔════╝╚██╗░██╔╝  ██║░░░██║██╔══██╗██║░░░░░██║██╔══██╗
█████═╝░█████╗░░░╚████╔╝░  ╚██╗░██╔╝███████║██║░░░░░██║██║░░██║
██╔═██╗░██╔══╝░░░░╚██╔╝░░  ░╚████╔╝░██╔══██║██║░░░░░██║██║░░██║
██║░╚██╗███████╗░░░██║░░░  ░░╚██╔╝░░██║░░██║███████╗██║██████╔╝
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝╚═════╝░
    """ + colorama.Fore.RESET)
    run = True
else:
    print(colorama.Fore.RED + """
██╗░░██╗███████╗██╗░░░██╗  ██╗███╗░░██╗██╗░░░██╗░█████╗░██╗░░░░░██╗██████╗░
██║░██╔╝██╔════╝╚██╗░██╔╝  ██║████╗░██║██║░░░██║██╔══██╗██║░░░░░██║██╔══██╗
█████═╝░█████╗░░░╚████╔╝░  ██║██╔██╗██║╚██╗░██╔╝███████║██║░░░░░██║██║░░██║
██╔═██╗░██╔══╝░░░░╚██╔╝░░  ██║██║╚████║░╚████╔╝░██╔══██║██║░░░░░██║██║░░██║
██║░╚██╗███████╗░░░██║░░░  ██║██║░╚███║░░╚██╔╝░░██║░░██║███████╗██║██████╔╝
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝╚═════╝░
    """ + colorama.Fore.RESET)
    input()
    run = False
while run:    
    while win  != code:
        for x in range(50):
            litera = random.choice(string.ascii_letters)
            walletNum += str(litera)
            time.sleep(0.005)
        code += 1
        print(f"{colorama.Fore.RED}[INVALID]{colorama.Fore.RESET}{walletNum}{colorama.Fore.RED}[0.00000000BTC]{colorama.Fore.RESET}")
        walletNum = ""
    for x in range(50):
            litera = random.choice(string.ascii_letters)
            walletNum += str(litera)
            time.sleep(0.005)
    code += 1
    satoshi = round(random.uniform(0.00000000, 0.4), 8)
    print(f"{colorama.Fore.GREEN}[VALID]{colorama.Fore.RESET}{walletNum}{colorama.Fore.GREEN}[{satoshi}BTC]{colorama.Fore.RESET}")
    input("Wallet saved to wallets.txt press any key to exit.")
    f = open("wallets.txt", "a")
    f.write(f"{walletNum}\n")
    f.close()
    run = False