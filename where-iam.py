import os
import sys
import requests
import time
os.system("clear")
print("-"*50)
os.system("figlet U-danbaiwa")

red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
cya='\033[035m'
print("-"*50)
def ebsb():
  print("="*50)
  print(cyan+"="*50)
  print("")
  print(yellow+bold+"\t{1} Where Iam")
  print(green+"="*50)
  print("")
  print(bold+bold+"\t{2} What Is My Ip Address ")
  print(yellow+"="*50)
  print("")
  print(cya+bold+"\t{3} About Author ")
  print(red+"="*50)
  print("")
  print(cyan+bold+"\t{00} Exit")
  print(yellow+"="*50)
ebsb()
def inpyt():
  print("\n")
  wv=input("Choose Options: ")
  if wv=="1":
    os.system("clear")
    os.system("figlet Where-Iam...")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    a=(green+bold+"Loading…")
    print(a)
    print(yellow+bold+"█▒▒▒▒▒▒▒▒▒0%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet Where-Iam...")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(green+bold+"Loading…")
    print(cyan+bold+"███▒▒▒▒▒▒▒10%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet Where-Iam...")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(green+bold+"Loading…")
    print(cy+bold+"█████▒▒▒▒▒40%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet Where-Iam...")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(green+bold+"Loading…")
    print(yellow+bold+"███████▒▒▒70%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet Where-Iam...")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(yellow+bold+"Loading…")
    print(green+bold+"██████████100%")
    
    res=requests.get("http://ip-api.com/json/").json()
    print("\n")
    bs=input(yellow+bold+"Your Device Name: ")
    try:
      print(green+bold+"checking...")
      time.sleep(5)
      print("")
      print(cya+bold+"{ - } You Are in |<====>|",cyan+res["country"])
      time.sleep(5)
      print("-"*60)
      print("")
      print(yellow+bold+"{ - } Your Town |<====>|",green+("FireWell Protected"))
      time.sleep(5)
      print("-"*60)
      print("")
      
      print(green+bold+"{ - } Your Country Code |<====>|",cya+res["countryCode"])
      print("-"*60)
      print("")
      time.sleep(5)
      print(cyan+bold+"{ - } Country City |<====>|",yellow+res["regionName"])
      print("-"*60)
      print("")
      time.sleep(5)
      print(yellow+bold+"{ - } Latitude |<====>|",cya,res["lat"])
      print("-"*60)
      print("")
      time.sleep(5)
      print(cya+bold+"{ - } longitude |<====>|",green,res["lon"])
      print("-"*60)
      print("")
      time.sleep(5)
      print(cyan+bold+"{ - } Your Sim Card Name |<====>|",cya+res["as"])
      print("-"*60)
      print("")
      time.sleep(5)
      print(green+bold+"{ - } Your Phone Status|<====>|",yellow+res["status"])
      print("-"*60)
      print("")
      time.sleep(5)
      print(yellow+bold+"{ - } Your Isp |<====>|",cyan,res["isp"])
      #print(cyan+"Your Organization |<====>|",gresn,res["org"])
      print("-"*60)
      print("")
      time.sleep(5)
      print(green+bold+"{ - } Your Time Zone |<====>|",yellow,res["timezone"])
      print("")
      os.system("figlet Thank You.")
      os.system("figlet Follow Me.")
    except Exception:
      print("Something Wrong")
  elif wv=="2":
    os.system("clear")
    os.system("figlet Where-Iam...")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    a=(green+bold+"Loading…")
    print(a)
    print(yellow+bold+"█▒▒▒▒▒▒▒▒▒0%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet Where-Iam...")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(green+bold+"Loading…")
    print(cyan+bold+"███▒▒▒▒▒▒▒10%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet Where-Iam...")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(green+bold+"Loading…")
    print(cy+bold+"█████▒▒▒▒▒40%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet Where-Iam...")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(green+bold+"Loading…")
    print(yellow+bold+"███████▒▒▒70%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet Where-Iam...")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(yellow+bold+"Loading…")
    print(green+bold+"██████████100%")
    print("\n\n")
    input("Enter Your Device Name: ")
    print("please wait...")
    time.sleep(10)
    print("\n")
    re=requests.get("http://ip-api.com/json/").json()
    print(red+bold+"*"*60)
    print(yellow+bold+"\tYOUR IP ADDRESS IS",cyan+"<=>====<=>",green,bold,re["query"])
    print(cyan+bold+"*"*60)
    print("\n")
    os.system("toilet Thank You")
    os.system("toilet Follow Me")
    os.system("toilet For More")
    os.system("toilet TOOLS")
  elif wv=="3":
    os.system("clear")
    os.system("figlet U-danbaiwa")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    a=(green+bold+"Loading…")
    print(a)
    print(yellow+bold+"█▒▒▒▒▒▒▒▒▒0%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet U-danbaiwa")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(green+bold+"Loading…")
    print(cyan+bold+"███▒▒▒▒▒▒▒10%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet U-danbaiwa")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(green+bold+"Loading…")
    print(cy+bold+"█████▒▒▒▒▒40%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet U-danbaiwa")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(green+bold+"Loading…")
    print(yellow+bold+"███████▒▒▒70%")
    time.sleep(5)
    os.system("clear")
    os.system("figlet U-danbaiwa")
    print(green+bold+"\t\t\tv 2.1.1")
    print("")
    print(yellow+bold+"Loading…")
    print(green+bold+"██████████100%")
    print("\n")
    print(yellow+bold+"\tName:<==========>",cyan+bold+"U-danbaiwa")
    print("\n")
    print(yellow+bold+"\tgithub:<=========>",cyan+bold+"www.github.com/U-danbaiwa")
    print("\n")
    print(yellow+bold+"\tFacebook:<=========>",cyan+bold+"Blank")
    print("\n")
    print(yellow+bold+"\tEmail/Gmail:<=========>",cyan+bold+"myownhacking1@gmail.com")
    print("\n")
    print(yellow+bold+"\tWhatsapp:<==========>",cyan+bold+"+2349031265908")
    print("\n")
    print(yellow+bold+"\tTwitter:<==========>"+cyan+bold+"Blank")
    print("\n")
    print(yellow+bold+"\tYoutube:<=========>",cyan+bold+"Blank")
    os.system("toilet Thank You")
    os.system("toilet Follow Me")
  elif wv=="00":
    os.system("clear")
    os.system("figlet U-danbaiwa")
    print("loading...")
    time.sleep(5)
    os.system("toilet See You")
    exit()
  else:
    os.system("toilet invalid")
    print(yellow+bold+"\t\tWrong Input")
  
inpyt()

    