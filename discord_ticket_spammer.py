import requests
import time
import threading
import os
from pystyle import Colorate, Colors
from datetime import datetime
from colorama import Fore

ascii_art = """
▄▄▄█████▓ ██▓ ▄████▄   ██ ▄█▀▓█████▄▄▄█████▓     ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
▓  ██▒ ▓▒▓██▒▒██▀ ▀█   ██▄█▒ ▓█   ▀▓  ██▒ ▓▒   ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▒██▒▒▓█    ▄ ▓███▄░ ▒███  ▒ ▓██░ ▒░   ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ░██░▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄░ ▓██▓ ░      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
  ▒██▒ ░ ░██░▒ ▓███▀ ░▒██▒ █▄░▒████▒ ▒██▒ ░    ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
  ▒ ░░   ░▓  ░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░ ▒ ░░      ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
    ░     ▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░   ░       ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
  ░       ▒ ░░        ░ ░░ ░    ░    ░         ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
          ░  ░ ░      ░  ░      ░  ░                 ░                 ░  ░       ░          ░      ░  ░   ░     
             ░                                                                                                   
"""


def clear():
    os.system("cls") if os.name == "nt" else os.system("clear")


def title(args=None):
    os.system("title Ticket Spammer") if args==None else os.system(f"title Ticket Spammer [~] {args}")


url = "https://discord.com/api/v9/interactions"

headers = {
    'authorization' : "YOUR-DISCORD-TOKEN"
}


clear()
title()
print(Colorate.Vertical(Colors.blue_to_purple, ascii_art))


count = int(input("> ~ $ Amount: "))
thred = str(input("> ~ $ Threading? [y/n] : "))
guildid = int(input("> ~ $ Guild ID: "))
channelid = int(input("> ~ $ Channel ID: "))
messageid = int(input("> ~ $ Message ID: "))
applicationid = int(input("> ~ $ Application ID: "))
buttonid = str(input("> ~ $ Button ID: "))

session_id = str(input("> ~ $ Session ID: "))


data = {
    "type":3,
    "guild_id":guildid,
    "channel_id":channelid,
    "message_flags":0,
    "message_id":messageid,
    "application_id":"508391840525975553",
    "session_id":session_id,
    "data":{
        "component_type":2,
        "custom_id":buttonid
        }
    }


global penis
penis = 0


def send():
    global penis
    for i in range(count):
        penis += 1
        title(f"Count: {penis}")
        time.sleep(1)
        r = requests.post(url, headers=headers, json=data)
        if r.status_code == 204:
            print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} {Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Succesfully made ticket")
        else:
            print(f"{Fore.LIGHTBLACK_EX}[{datetime.now().strftime('%H:%M')}]{Fore.RESET} {Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.RESET} Failed to make ticket")

if thred.lower() == "y":
    threads = []
    for i in range(count):
        t = threading.Thread(target=send)
        t.daemon = True
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

else:
    for i in range(count):
        send()