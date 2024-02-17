import requests
import time
import threading
import os
from pystyle import Colorate, Colors
from datetime import datetime
from colorama import Fore
import uuid
import tls_client
import json
import random

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

def ttimee():
    return datetime.now().strftime('%H:%M')

def title():
    os.system("title Ticket Spammer")

def update_title(made, cap, failed, limit):
    os.system(f"title Ticket Spammer Made ~ {made} Captcha ~ {cap} Ratelimited ~ {limit} Failed ~ {failed}")


def nonce():
    return str((int(time.mktime(datetime.now().timetuple())) * 1000 - 1420070400000) * 4194304)

def ss():
    session = tls_client.Session(client_identifier="chrome_108",random_tls_extension_order=True)
    return session

def tokens():
    with open("tokens.txt", "r") as f:
        tokens = f.read().splitlines()
    return tokens

def cookies():
    try:
        r = requests.get("https://canary.discord.com")
        if r.status_code == 200:
            return "; ".join(f"{cookie.name}={cookie.value}" for cookie in r.cookies) + "; locale=en-US"
        else:
            return "__dcfduid=4e0a8d504a4411eeb88f7f88fbb5d20a; __sdcfduid=4e0a8d514a4411eeb88f7f88fbb5d20ac488cd4896dae6574aaa7fbfb35f5b22b405bbd931fdcb72c21f85b263f61400; __cfruid=f6965e2d30c244553ff3d4203a1bfdabfcf351bd-1699536665; _cfuvid=rNaPQ7x_qcBwEhO_jNgXapOMoUIV2N8FA_8lzPV89oM-1699536665234-0-604800000; locale=en-US"
    except:
        return "__dcfduid=4e0a8d504a4411eeb88f7f88fbb5d20a; __sdcfduid=4e0a8d514a4411eeb88f7f88fbb5d20ac488cd4896dae6574aaa7fbfb35f5b22b405bbd931fdcb72c21f85b263f61400; __cfruid=f6965e2d30c244553ff3d4203a1bfdabfcf351bd-1699536665; _cfuvid=rNaPQ7x_qcBwEhO_jNgXapOMoUIV2N8FA_8lzPV89oM-1699536665234-0-604800000; locale=en-US"

cookie = cookies()
def headers(token):
    headers = {
        "accept-language": "en-GB",
        "authorization": token,
        "cookie": cookie,
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9031 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "pl",
        "x-discord-timezone": "Europe/Warsaw",
        "x-failed-requests": "1",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDMxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMzEgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNjE5NzMsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQyODk5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
    }
    return headers

clear()
title()
print(Colorate.Vertical(Colors.blue_to_purple, ascii_art))

try:
    threads = int(input(Colorate.Horizontal(Colors.blue_to_purple, "> ~ $ Thread amount: ")))
except ValueError:
    print(Colorate.Horizontal(Colors.blue_to_purple, "Please input a valid integreer"))
    time.sleep(5)
    exit()
thred = str(input(Colorate.Horizontal(Colors.blue_to_purple, "> ~ $ Threading? [y/n] : ")))
guildid = int(input(Colorate.Horizontal(Colors.blue_to_purple, "> ~ $ Guild ID: ")))
channelid = int(input(Colorate.Horizontal(Colors.blue_to_purple, "> ~ $ Channel ID: ")))
messageid = int(input(Colorate.Horizontal(Colors.blue_to_purple, "> ~ $ Message ID: ")))

def get(channel_id):
    session = ss()
    found = False
    for token in tokens():
        if not found:
            r = session.get(
                f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=50",
                headers={
                    "accept-language": "en-GB",
                    "authorization": token,
                    "cookie": cookies(),
                    "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108"',
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9031 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36",
                    "x-debug-options": "bugReporterEnabled",
                    "x-discord-locale": "pl",
                    "x-discord-timezone": "Europe/Warsaw",
                    "x-failed-requests": "1",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDMxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0IiwiYXBwX2FyY2giOiJpYTMyIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMzEgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMjYgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMjYiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNjE5NzMsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjQyODk5LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
                },
            )
            if r.status_code == 200:
                found = True
                data = r.json()
                author_id = data[0]['author']['id']
                buttons_info = []
                components = data[0]['components']
                for component in components:
                    for sub_component in component['components']:
                        button_info = {
                            'custom_id': sub_component['custom_id'],
                            'label': sub_component['label']
                        }
                        buttons_info.append(button_info)

                return author_id, buttons_info

def click(token, guild_id, channel_id, message_id, custom_id, author_id):
    session = ss()
    r = session.post(
        "https://discord.com/api/v9/interactions",
        headers=headers(token),
        json={
            'application_id': author_id,
            'channel_id': channel_id,
            'data': {
                'component_type': 2,
                'custom_id': custom_id,
            },
            'guild_id': guild_id,
            'message_flags': 0,
            'message_id': message_id,
            'nonce': nonce(),
            'session_id': uuid.uuid4().hex,
            'type': 3,
        }
    )
    status = r.status_code
    text = r.text
    if status == 204:
        print(f"{Fore.LIGHTBLACK_EX}[{ttimee()}]{Fore.RESET} {Fore.GREEN}[{Fore.RESET}+{Fore.GREEN}]{Fore.RESET} Made ticket")
        return 'made'
    elif status == 400:
        print(f"{Fore.LIGHTBLACK_EX}[{ttimee()}]{Fore.RESET} {Fore.YELLOW}[{Fore.RESET}~{Fore.YELLOW}]{Fore.RESET} Captcha")
        return 'captcha'
    elif status == 429:
        text = json.loads(text)
        slip = float(text.get('retry_after'))
        print(f"{Fore.LIGHTBLACK_EX}[{ttimee()}]{Fore.RESET} {Fore.YELLOW}[{Fore.RESET}~{Fore.YELLOW}]{Fore.RESET} Ratelimit {Fore.LIGHTBLACK_EX}({slip}s)")
        time.sleep(slip)
        return 'limited'
    elif status == 401:
        print(f"{Fore.LIGHTBLACK_EX}[{ttimee()}]{Fore.RESET} {Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.RESET} Invalid token {Fore.LIGHTBLACK_EX}({text})")
        return 'invalid_token'
    else:
        print(f"{Fore.LIGHTBLACK_EX}[{ttimee()}]{Fore.RESET} {Fore.RED}[{Fore.RESET}-{Fore.RED}]{Fore.RESET} Failed to make ticket {Fore.LIGHTBLACK_EX}({text})")
        return 'failed'

def run(tkns, guildid, channelid, messageid, custom_id, author_id):
    failed = 0
    made = 0
    cap = 0
    limited = 0
    token = random.choice(tkns)
    try:
        while True:
            result = click(token, guildid, channelid, messageid, custom_id, author_id)
            if result == 'made':
                made += 1
            elif result == 'captcha':
                cap += 1
            elif result == 'limited':
                limited += 1
            elif result == 'invalid_token':
                failed += 1
            else:
                failed += 1
            update_title(made, cap, failed, limited)
    except KeyboardInterrupt:
        return

print(Colorate.Horizontal(Colors.blue_to_purple, "Getting buttons..."))
author_id, buttons_info = get(channelid)
print(Colorate.Horizontal(Colors.blue_to_purple, "Buttons:\n"))
for i, button_info in enumerate(buttons_info, start=1):
    print(Colorate.Horizontal(Colors.blue_to_purple, f"{i} - {button_info['label']}"))
print("\n")
choice = int(input(Colorate.Horizontal(Colors.blue_to_purple, "> ~ $ Button: ")))
if 1 <= choice <= len(buttons_info):
    selected_button_info = buttons_info[choice - 1]
    custom_id = selected_button_info['custom_id']

tkns = tokens()
print(Colorate.Horizontal(Colors.blue_to_purple, "Controll + c to stop"))
if thred.lower() == "y":
    thread_list = []
    for i in range(threads):
        t = threading.Thread(target=run, args=(tkns, guildid, channelid, messageid, custom_id, author_id))
        t.daemon = True
        t.start()
        thread_list.append(t)
    for thread in thread_list:
        thread.join()

else:
    for i in range(threads):
        click()
