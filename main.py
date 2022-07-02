import sys
import requests
from pystyle import Colors, Colorate
import random
import os
import json
import time

custompass = False
p1 = ''

def generate_email():
    domains = {
        'gmail': 'gmail.com',
        'hotmail': 'hotmail.com',
        'outlook': 'outlook.com',
        'yahoo': 'yahoo.com',
        'aol': 'aol.com',
        'icloud': 'icloud.com',
        'mail': 'mail.com',
        'comcast': 'comcast.net',
        'verizon': 'verizon.net',
        'att': 'att.net',
        'sbcglobal': 'sbcglobal.net',
        'bellsouth': 'bellsouth.net',
        'charter': 'charter.net',
        'metropcs': 'metropcs.com',
        'custserv': 'custserv.com',
        'cox': 'cox.net'
    }
    url = "https://api.namefake.com/"
    r = requests.get(url).text
    data = json.loads(r)
    name = data['name']
    name = name.split(' ')
    for i in range(len(name)):
        name[i] = name[i][0].lower() + name[i][1:]
    name = '.'.join(name)
    if '..' in name:
        name = name.replace('..', '.')
    domain = random.choice(list(domains.keys()))
    email = name + '@' + domains[domain]
    return email


def generate_password():
    if custompass == True:
        password = p1
    else:
        password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(random.randint(8, 16)))
    return password


def generate_name():
    url = 'https://raw.githubusercontent.com/itschasa/Discord-Scraped/main/names.txt'
    name = requests.get(url).text
    name = name.split('\n')
    name = random.choice(name)
    if ' ' in name:
        name = name.replace(' ', '_')
    return name

def generate_year():
    year = random.randint(1900, 2000)
    return year

def generate_month():
    month = random.randint(1, 12)
    return month

def generate_day():
    day = random.randint(1, 28)
    return day

e = ""
p = ""

def create():
    email = generate_email()
    password = generate_password()
    name = generate_name()
    year = generate_year()
    month = generate_month()
    day = generate_day()
    nick = generate_name()

    headers={"Accept-Encoding": "gzip",
             "Accept-Language": "en-US",
             "App-Platform": "Android",
             "Connection": "Keep-Alive",
             "Content-Type": "application/x-www-form-urlencoded",
             "Host": "spclient.wg.spotify.com",
             "User-Agent": "Spotify/8.6.72 Android/29 (SM-N976N)",
             "Spotify-App-Version": "8.6.72"
    }
    
    payload = {"creation_point": "client_mobile",
            "gender": "male" if random.randint(0, 1) else "female",
            "birth_year": year,
            "displayname": nick,
            "iagree": "true",
            "birth_month": month,
            "password_repeat": password,
            "password": password,
            "platform": "Android-ARM",
            "key": "142b583129b2df829de3656f9eb484e6",
            "email": email,
            "birth_day": day}
    
    r = requests.post('https://spclient.wg.spotify.com/signup/public/v1/account/', headers=headers, data=payload, timeout=1)
    if r.status_code == 200:
        print(Colorate.Horizontal(Colors.blue_to_purple, "[=] Created account: " + email + ":" + password))
        e = email
        p = password
        with open('accounts.txt', 'a') as f:
            f.write(email + ":" + password + "\n")
    else:
        print(Colorate.Horizontal(Colors.blue_to_purple, "[-] Failed to create account"))
        create()
    return r.text
    
def logo():
    os.system('title Spotify Account Creator - Made by: DRQSuperior - Version: 1.0')
    print(Colorate.Horizontal(Colors.blue_to_purple, """
 __                _    _   __        
/ _\ _ __    ___  | |_ (_) / _| _   _ 
\ \ | '_ \  / _ \ | __|| || |_ | | | |
_\ \| |_) || (_) || |_ | ||  _|| |_| |
\__/| .__/  \___/  \__||_||_|   \__, |
    |_|                         |___/ 
    """))

if __name__ == "__main__":
    logo()
    print(Colorate.Horizontal(Colors.blue_to_purple, "[+] Made by: DRQSuperior#0001"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "[+] Version: 1.0"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "[+] Discord: discord.gg/M8mTjxcYEx"))
    print("")
    print("")
    amount = int(input(Colorate.Horizontal(Colors.blue_to_purple, "[+] Amount of accounts to create 0(infinite): ")))
    if amount == 0:
        amount = (int(999999999999999999999))
    custompass = input(Colorate.Horizontal(Colors.blue_to_purple, "[+] Custom password (y/n): "))
    if custompass == "y":
        p1 = input(Colorate.Horizontal(Colors.blue_to_purple, "[?] Custom password: "))
        password = p1
        custompass = True
    else:
        custompass = False
        
    with open('accounts.txt', 'a') as f:
        pass

    for i in range(amount):
        create()
        print(Colorate.Horizontal(Colors.blue_to_purple, "[+] Created " + str(i + 1) + "/" + str(amount)))