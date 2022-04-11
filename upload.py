import os, ctypes, json, requests, datetime
from colorama import Fore
from requests import get

def banner():
    print(f"""
                        {Fore.RED}Dev By Tahg{Fore.RESET}
░██████╗░██╗░░░██╗░█████╗░███████╗░█████╗░░░░░░░██╗███╗░░░███╗░██████╗░
██╔════╝░╚██╗░██╔╝██╔══██╗╚════██║██╔══██╗░░░░░░██║████╗░████║██╔════╝░
██║░░██╗░░╚████╔╝░███████║░░███╔═╝██║░░██║█████╗██║██╔████╔██║██║░░██╗░
██║░░╚██╗░░╚██╔╝░░██╔══██║██╔══╝░░██║░░██║╚════╝██║██║╚██╔╝██║██║░░╚██╗
╚██████╔╝░░░██║░░░██║░░██║███████╗╚█████╔╝░░░░░░██║██║░╚═╝░██║╚██████╔╝
░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚════╝░░░░░░░╚═╝╚═╝░░░░░╚═╝░╚═════╝░
    {Fore.RED}GitHub: {Fore.BLUE}https://github.com/T4hg/ {Fore.RESET}
    """)

def gyazo():
    prefix = f"{Fore.RED}Gyazo {Fore.BLUE}IMG {Fore.GREEN}· {Fore.WHITE}"
    system_prefix = f"{Fore.RED}$ {Fore.GREEN}"
    file = input(prefix + "Image (EXAMPLE: example.png): ")

    config = open("config.json", "r")
    config_load = json.load(config)

    url = "https://upload.gyazo.com/api/upload"
    r = requests.post(url, files=file, headers=config_load)
    resp = json.loads(r.text)
    print(f"""
    {Fore.RED}Image ID: {Fore.WHITE}{resp["image_id"]}
    {Fore.RED}Perma URL: {Fore.WHITE}{resp["permalink_url"]}
    {Fore.RED}Thumb URL: {Fore.WHITE}{resp["thumb_url"]}
    {Fore.RED}URL: {Fore.WHITE}{resp["url"]}
    """)

    date = datetime.datetime.now()
    file_txt = open("Uploads.txt", "a+")
    file_txt.write(f"{date}\nImage ID: {resp['image_id']}\nURL: {resp['url']}\n")
    file_txt.close()
    print(f"""
    {Fore.GREEN}If you like the app, don't forget to give it a {Fore.YELLOW}star {Fore.GREEN}on GitHub

    {Fore.WHITE}ENTER TO BACK""")
    input()
    gyazo()
if __name__ == '__main__':
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f'Gyazo Image Upload | Developed by Tahg - GitHub: https://github.com/T4hg/')
    banner()
    gyazo()
