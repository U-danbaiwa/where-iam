import os
import sys
import requests
import time
os.system("clear")
os.system("figlet U-danbaiwa")

red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
cya='\033[035m'
def ebsb():
  print(yellow+"{1} Where Iam")
  print("")
  print(cyan+"{2} What Is My Ip Address ")
  print("")
  print(cya+"{3} About Author ")
  print("")
  print("")
  print(red+bold+"{00} Exit")
ebsb()
def inpyt():
  print("\n")
  wv=input("Choose Options: ")
  if wv=="1":
    os.system("clear")
    os.system("figlet Where-Iam")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    a=(green+bold+"Loading…")
    print(a)
    print(yellow+bold+"█▒▒▒▒▒▒▒▒▒0%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet Where-Iam")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(green+bold+"Loading…")
    print(cyan+bold+"███▒▒▒▒▒▒▒10%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet Where-Iam")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(green+bold+"Loading…")
    print(red+bold+"█████▒▒▒▒▒40%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet Where-Iam")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(green+bold+"Loading…")
    print(yellow+bold+"███████▒▒▒70%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet Where-Iam")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(yellow+bold+"Loading…")
    print(green+bold+"██████████100%")
    
    res=requests.get("http://ip-api.com/json/")
    bs=input("Enter ")
inpyt()

    