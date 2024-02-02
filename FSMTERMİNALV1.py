import os
try:
    import requests
except:
    os.system ("pip install requests")
try:
   import colorama
except:
    os.system("pip install colorama")
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
from colorama import *
auth = '1840e53e-0a8b-4d4d-b4e6-4d34d1033d91'
import time as t
import modules
import requests
import colorama
import urllib.request  as urllib2 
import re
import sys,os
import random
import str
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('FSM CYBER TEAM'))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("LÜTFEN yardım KOMUTUNU TERMİNALE YAZ")

E = '\033[0m'
H = '\033[95m'
tip = input(E+'FSM»TERMİNAL»'+H)
if tip == 'yardım':
            print("""
            komutlar :  TÜM KOMUTLARI SANA SÖYLER
            iptracker :  ip adressin bilgilerink bulur
            help :  YARDIM İÇİN KOMUT
            exit : TOOLDAN ÇIKARSIN
            
            update:  Its update Ip-Tracker automatically 
            """)
elif tip == "komutlar":
            print("""
            This are the available commands
            help
            show
            exit
            iptracker
            update
            ddos
            """)
elif tip == 'exit':
            os.system("clear")
            os.system("exit")
elif tip == "iptracker":
            print("""________________________________Track Ip____________________________""")
            print("""
            """)

            ip = input("Enter IP Address : ")
            print (" Fetching data from " +ip)
            def get_location():
                ip_address = ip
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

                location_data = {
                "Ip Address" : ip_address, 
                "city" : response.get("city"),
                "region" : response.get("region"),
                "country" : response.get("country_name"),
                "Ip Address Type" : response.get("version"),
                "Region Code" : response.get("region_code"), 
                "Postal Code" : response.get("postal"), 
                "Latitude" : response.get(str("latitude")), 
                "Longitude" : response.get(str("longitude")), 
                "TimeZone" : response.get("timezone"), 
                "Country code" : response.get("country_calling_code"), 
                "Currency" : response.get("currency"), 
                "Currency Name" : response.get("currency_name") , 
                "Languages" : response.get("languages"), 
                "Country Area" : response.get("country_area"), 
                "Population" : response.get("country_population"),
                "ASN" : response.get("asn"), 
                "Organization" : response.get("org")

                }
                latitude = response.get("latitude")
                global lat
                lat = str(latitude)
                longitude = response.get("longitude")
                global long
                long = str(longitude)

                global url
                url = "https://google.com/maps/place/" + lat +  "," + long + "/@" + lat + "," + long + ",16z"

                return location_data
            map = input (Fore.CYAN + "\n\nDo you want to open location on google map? [yes/no]: " + Style.RESET_ALL)
else: 
 print("LÜTFEN DÜZGÜN KOMUT YAZ MK OĞLU")

 t.sleep(5) 
 os.system("clear")
 exit()
  
 print(f.renderText('FSM CYBER TEAM'))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("LÜTFEN yardım KOMUTUNU TERMİNALE YAZ")

E = '\033[0m'
H = '\033[95m'
tip = input(E+'FSM»TERMİNAL»'+H)
if tip == 'yardım':
            print("""
            komutlar :  TÜM KOMUTLARI SANA SÖYLER
            iptracker :  ip adressin bilgilerink bulur
            help :  YARDIM İÇİN KOMUT
            exit : TOOLDAN ÇIKARSIN
            
            update:  Its update Ip-Tracker automatically 
            """)
elif tip == "komutlar":
            print("""
            This are the available commands
            help
            show
            exit
            iptracker
            update
            ddos
            """)
elif tip == 'exit':
            os.system("clear")
            os.system("exit")
elif tip == "iptracker":
            print("""________________________________Track Ip____________________________""")
            print("""
            """)

            ip = input("Enter IP Address : ")
            print (" Fetching data from " +ip)
            def get_location():
                ip_address = ip
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

                location_data = {
                "Ip Address" : ip_address, 
                "city" : response.get("city"),
                "region" : response.get("region"),
                "country" : response.get("country_name"),
                "Ip Address Type" : response.get("version"),
                "Region Code" : response.get("region_code"), 
                "Postal Code" : response.get("postal"), 
                "Latitude" : response.get(str("latitude")), 
                "Longitude" : response.get(str("longitude")), 
                "TimeZone" : response.get("timezone"), 
                "Country code" : response.get("country_calling_code"), 
                "Currency" : response.get("currency"), 
                "Currency Name" : response.get("currency_name") , 
                "Languages" : response.get("languages"), 
                "Country Area" : response.get("country_area"), 
                "Population" : response.get("country_population"),
                "ASN" : response.get("asn"), 
                "Organization" : response.get("org")

                }
                latitude = response.get("latitude")
                global lat
                lat = str(latitude)
                longitude = response.get("longitude")
                global long
                long = str(longitude)

                global url
                url = "https://google.com/maps/place/" + lat +  "," + long + "/@" + lat + "," + long + ",16z"

                return location_data
            map = input (Fore.CYAN + "\n\nDo you want to open location on google map? [yes/no]: " + Style.RESET_ALL)
else: 
 print("LÜTFEN DÜZGÜN KOMUT YAZ MK OĞLU")

 t.sleep(5) 
 os.system("clear")
 exit()
   
 print(f.renderText('FSM CYBER TEAM'))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("LÜTFEN yardım KOMUTUNU TERMİNALE YAZ")

E = '\033[0m'
H = '\033[95m'
tip = input(E+'FSM»TERMİNAL»'+H)
if tip == 'yardım':
            print("""
            komutlar :  TÜM KOMUTLARI SANA SÖYLER
            iptracker :  ip adressin bilgilerink bulur
            help :  YARDIM İÇİN KOMUT
            exit : TOOLDAN ÇIKARSIN
            
            update:  Its update Ip-Tracker automatically 
            """)
elif tip == "komutlar":
            print("""
            This are the available commands
            help
            show
            exit
            iptracker
            update
            ddos
            """)
elif tip == 'exit':
            os.system("clear")
            os.system("exit")
elif tip == "iptracker":
            print("""________________________________Track Ip____________________________""")
            print("""
            """)

            ip = input("Enter IP Address : ")
            print (" Fetching data from " +ip)
            def get_location():
                ip_address = ip
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

                location_data = {
                "Ip Address" : ip_address, 
                "city" : response.get("city"),
                "region" : response.get("region"),
                "country" : response.get("country_name"),
                "Ip Address Type" : response.get("version"),
                "Region Code" : response.get("region_code"), 
                "Postal Code" : response.get("postal"), 
                "Latitude" : response.get(str("latitude")), 
                "Longitude" : response.get(str("longitude")), 
                "TimeZone" : response.get("timezone"), 
                "Country code" : response.get("country_calling_code"), 
                "Currency" : response.get("currency"), 
                "Currency Name" : response.get("currency_name") , 
                "Languages" : response.get("languages"), 
                "Country Area" : response.get("country_area"), 
                "Population" : response.get("country_population"),
                "ASN" : response.get("asn"), 
                "Organization" : response.get("org")

                }
                latitude = response.get("latitude")
                global lat
                lat = str(latitude)
                longitude = response.get("longitude")
                global long
                long = str(longitude)

                global url
                url = "https://google.com/maps/place/" + lat +  "," + long + "/@" + lat + "," + long + ",16z"

                return location_data
            map = input (Fore.CYAN + "\n\nDo you want to open location on google map? [yes/no]: " + Style.RESET_ALL)
else: 
 print("LÜTFEN DÜZGÜN KOMUT YAZ MK OĞLU")
 
 
 t.sleep(5) 
 os.system("clear")
 exit()
 
 print(f.renderText('FSM CYBER TEAM'))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("LÜTFEN yardım KOMUTUNU TERMİNALE YAZ")

E = '\033[0m'
H = '\033[95m'
tip = input(E+'FSM»TERMİNAL»'+H)
if tip == 'yardım':
            print("""
            komutlar :  TÜM KOMUTLARI SANA SÖYLER
            iptracker :  ip adressin bilgilerink bulur
            help :  YARDIM İÇİN KOMUT
            exit : TOOLDAN ÇIKARSIN
            
            update:  Its update Ip-Tracker automatically 
            """)
elif tip == "komutlar":
            print("""
            This are the available commands
            help
            show
            exit
            iptracker
            update
            ddos
            """)
elif tip == 'exit':
            os.system("clear")
            os.system("exit")
elif tip == "iptracker":
            print("""________________________________Track Ip____________________________""")
            print("""
            """)

            ip = input("Enter IP Address : ")
            print (" Fetching data from " +ip)
            def get_location():
                ip_address = ip
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

                location_data = {
                "Ip Address" : ip_address, 
                "city" : response.get("city"),
                "region" : response.get("region"),
                "country" : response.get("country_name"),
                "Ip Address Type" : response.get("version"),
                "Region Code" : response.get("region_code"), 
                "Postal Code" : response.get("postal"), 
                "Latitude" : response.get(str("latitude")), 
                "Longitude" : response.get(str("longitude")), 
                "TimeZone" : response.get("timezone"), 
                "Country code" : response.get("country_calling_code"), 
                "Currency" : response.get("currency"), 
                "Currency Name" : response.get("currency_name") , 
                "Languages" : response.get("languages"), 
                "Country Area" : response.get("country_area"), 
                "Population" : response.get("country_population"),
                "ASN" : response.get("asn"), 
                "Organization" : response.get("org")

                }
                latitude = response.get("latitude")
                global lat
                lat = str(latitude)
                longitude = response.get("longitude")
                global long
                long = str(longitude)

                global url
                url = "https://google.com/maps/place/" + lat +  "," + long + "/@" + lat + "," + long + ",16z"

                return location_data
            map = input (Fore.CYAN + "\n\nDo you want to open location on google map? [yes/no]: " + Style.RESET_ALL)
else: 
 print("LÜTFEN DÜZGÜN KOMUT YAZ MK OĞLU")

 
 t.sleep(5) 
 os.system("clear")
 exit() 
 
 print(f.renderText('FSM CYBER TEAM'))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("LÜTFEN yardım KOMUTUNU TERMİNALE YAZ")

E = '\033[0m'
H = '\033[95m'
tip = input(E+'FSM»TERMİNAL»'+H)
if tip == 'yardım':
            print("""
            komutlar :  TÜM KOMUTLARI SANA SÖYLER
            iptracker :  ip adressin bilgilerink bulur
            help :  YARDIM İÇİN KOMUT
            exit : TOOLDAN ÇIKARSIN
            
            update:  Its update Ip-Tracker automatically 
            """)
elif tip == "komutlar":
            print("""
            This are the available commands
            help
            show
            exit
            iptracker
            update
            ddos
            """)
elif tip == 'exit':
            os.system("clear")
            os.system("exit")
elif tip == "iptracker":
            print("""________________________________Track Ip____________________________""")
            print("""
            """)

            ip = input("Enter IP Address : ")
            print (" Fetching data from " +ip)
            def get_location():
                ip_address = ip
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

                location_data = {
                "Ip Address" : ip_address, 
                "city" : response.get("city"),
                "region" : response.get("region"),
                "country" : response.get("country_name"),
                "Ip Address Type" : response.get("version"),
                "Region Code" : response.get("region_code"), 
                "Postal Code" : response.get("postal"), 
                "Latitude" : response.get(str("latitude")), 
                "Longitude" : response.get(str("longitude")), 
                "TimeZone" : response.get("timezone"), 
                "Country code" : response.get("country_calling_code"), 
                "Currency" : response.get("currency"), 
                "Currency Name" : response.get("currency_name") , 
                "Languages" : response.get("languages"), 
                "Country Area" : response.get("country_area"), 
                "Population" : response.get("country_population"),
                "ASN" : response.get("asn"), 
                "Organization" : response.get("org")

                }
                latitude = response.get("latitude")
                global lat
                lat = str(latitude)
                longitude = response.get("longitude")
                global long
                long = str(longitude)

                global url
                url = "https://google.com/maps/place/" + lat +  "," + long + "/@" + lat + "," + long + ",16z"

                return location_data
            map = input (Fore.CYAN + "\n\nDo you want to open location on google map? [yes/no]: " + Style.RESET_ALL)
else: 
 print("LÜTFEN DÜZGÜN KOMUT YAZ MK OĞLU")

 t.sleep(5) 
 os.system("clear")
 exit()
 
 print(f.renderText('FSM CYBER TEAM'))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("LÜTFEN yardım KOMUTUNU TERMİNALE YAZ")

E = '\033[0m'
H = '\033[95m'
tip = input(E+'FSM»TERMİNAL»'+H)
if tip == 'yardım':
            print("""
            komutlar :  TÜM KOMUTLARI SANA SÖYLER
            iptracker :  ip adressin bilgilerink bulur
            help :  YARDIM İÇİN KOMUT
            exit : TOOLDAN ÇIKARSIN
            
            update:  Its update Ip-Tracker automatically 
            """)
elif tip == "komutlar":
            print("""
            This are the available commands
            help
            show
            exit
            iptracker
            update
            ddos
            """)
elif tip == 'exit':
            os.system("clear")
            os.system("exit")
elif tip == "iptracker":
            print("""________________________________Track Ip____________________________""")
            print("""
            """)

            ip = input("Enter IP Address : ")
            print (" Fetching data from " +ip)
            def get_location():
                ip_address = ip
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

                location_data = {
                "Ip Address" : ip_address, 
                "city" : response.get("city"),
                "region" : response.get("region"),
                "country" : response.get("country_name"),
                "Ip Address Type" : response.get("version"),
                "Region Code" : response.get("region_code"), 
                "Postal Code" : response.get("postal"), 
                "Latitude" : response.get(str("latitude")), 
                "Longitude" : response.get(str("longitude")), 
                "TimeZone" : response.get("timezone"), 
                "Country code" : response.get("country_calling_code"), 
                "Currency" : response.get("currency"), 
                "Currency Name" : response.get("currency_name") , 
                "Languages" : response.get("languages"), 
                "Country Area" : response.get("country_area"), 
                "Population" : response.get("country_population"),
                "ASN" : response.get("asn"), 
                "Organization" : response.get("org")

                }
                latitude = response.get("latitude")
                global lat
                lat = str(latitude)
                longitude = response.get("longitude")
                global long
                long = str(longitude)

                global url
                url = "https://google.com/maps/place/" + lat +  "," + long + "/@" + lat + "," + long + ",16z"

                return location_data
            map = input (Fore.CYAN + "\n\nDo you want to open location on google map? [yes/no]: " + Style.RESET_ALL)
else: 
 print("LÜTFEN DÜZGÜN KOMUT YAZ MK OĞLU")
 
 t.sleep(5) 
 os.system("clear")
 exit() 
 
print(f.renderText('FSM CYBER TEAM'))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("LÜTFEN yardım KOMUTUNU TERMİNALE YAZ")

E = '\033[0m'
H = '\033[95m'
tip = input(E+'FSM»TERMİNAL»'+H)
if tip == 'yardım':
            print("""
            komutlar :  TÜM KOMUTLARI SANA SÖYLER
            iptracker :  ip adressin bilgilerink bulur
            help :  YARDIM İÇİN KOMUT
            exit : TOOLDAN ÇIKARSIN
            
            update:  Its update Ip-Tracker automatically 
            """)
elif tip == "komutlar":
            print("""
            This are the available commands
            help
            show
            exit
            iptracker
            update
            ddos
            """)
elif tip == 'exit':
            os.system("clear")
            os.system("exit")
elif tip == "iptracker":
            print("""________________________________Track Ip____________________________""")
            print("""
            """)

            ip = input("Enter IP Address : ")
            print (" Fetching data from " +ip)
            def get_location():
                ip_address = ip
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

                location_data = {
                "Ip Address" : ip_address, 
                "city" : response.get("city"),
                "region" : response.get("region"),
                "country" : response.get("country_name"),
                "Ip Address Type" : response.get("version"),
                "Region Code" : response.get("region_code"), 
                "Postal Code" : response.get("postal"), 
                "Latitude" : response.get(str("latitude")), 
                "Longitude" : response.get(str("longitude")), 
                "TimeZone" : response.get("timezone"), 
                "Country code" : response.get("country_calling_code"), 
                "Currency" : response.get("currency"), 
                "Currency Name" : response.get("currency_name") , 
                "Languages" : response.get("languages"), 
                "Country Area" : response.get("country_area"), 
                "Population" : response.get("country_population"),
                "ASN" : response.get("asn"), 
                "Organization" : response.get("org")

                }
                latitude = response.get("latitude")
                global lat
                lat = str(latitude)
                longitude = response.get("longitude")
                global long
                long = str(longitude)

                global url
                url = "https://google.com/maps/place/" + lat +  "," + long + "/@" + lat + "," + long + ",16z"

                return location_data
            map = input (Fore.CYAN + "\n\nDo you want to open location on google map? [yes/no]: " + Style.RESET_ALL)
else: 
 print("LÜTFEN DÜZGÜN KOMUT YAZ MK OĞLU")

 t.sleep(5) 
 os.system("clear")
 exit()
 print(f.renderText('FSM CYBER TEAM'))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("LÜTFEN yardım KOMUTUNU TERMİNALE YAZ")

E = '\033[0m'
H = '\033[95m'
tip = input(E+'FSM»TERMİNAL»'+H)
if tip == 'yardım':
            print("""
            komutlar :  TÜM KOMUTLARI SANA SÖYLER
            iptracker :  ip adressin bilgilerink bulur
            help :  YARDIM İÇİN KOMUT
            exit : TOOLDAN ÇIKARSIN
            
            update:  Its update Ip-Tracker automatically 
            """)
elif tip == "komutlar":
            print("""
            This are the available commands
            help
            show
            exit
            iptracker
            update
            ddos
            """)
elif tip == 'exit':
            os.system("clear")
            os.system("exit")
elif tip == "iptracker":
            print("""________________________________Track Ip____________________________""")
            print("""
            """)

            ip = input("Enter IP Address : ")
            print (" Fetching data from " +ip)
            def get_location():
                ip_address = ip
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

                location_data = {
                "Ip Address" : ip_address, 
                "city" : response.get("city"),
                "region" : response.get("region"),
                "country" : response.get("country_name"),
                "Ip Address Type" : response.get("version"),
                "Region Code" : response.get("region_code"), 
                "Postal Code" : response.get("postal"), 
                "Latitude" : response.get(str("latitude")), 
                "Longitude" : response.get(str("longitude")), 
                "TimeZone" : response.get("timezone"), 
                "Country code" : response.get("country_calling_code"), 
                "Currency" : response.get("currency"), 
                "Currency Name" : response.get("currency_name") , 
                "Languages" : response.get("languages"), 
                "Country Area" : response.get("country_area"), 
                "Population" : response.get("country_population"),
                "ASN" : response.get("asn"), 
                "Organization" : response.get("org")

                }
                latitude = response.get("latitude")
                global lat
                lat = str(latitude)
                longitude = response.get("longitude")
                global long
                long = str(longitude)

                global url
                url = "https://google.com/maps/place/" + lat +  "," + long + "/@" + lat + "," + long + ",16z"

                return location_data
            map = input (Fore.CYAN + "\n\nDo you want to open location on google map? [yes/no]: " + Style.RESET_ALL)
else: 
 print("LÜTFEN DÜZGÜN KOMUT YAZ MK OĞLU")
 
 
 t.sleep(5) 
 os.system("clear")
 exit()
 
 print(f.renderText('FSM CYBER TEAM'))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("LÜTFEN yardım KOMUTUNU TERMİNALE YAZ")

E = '\033[0m'
H = '\033[95m'
tip = input(E+'FSM»TERMİNAL»'+H)
if tip == 'yardım':
            print("""
            komutlar :  TÜM KOMUTLARI SANA SÖYLER
            iptracker :  ip adressin bilgilerink bulur
            help :  YARDIM İÇİN KOMUT
            exit : TOOLDAN ÇIKARSIN
            
            update:  Its update Ip-Tracker automatically 
            """)
elif tip == "komutlar":
            print("""
            This are the available commands
            help
            show
            exit
            iptracker
            update
            ddos
            """)
elif tip == 'exit':
            os.system("clear")
            os.system("exit")
elif tip == "iptracker":
            print("""________________________________Track Ip____________________________""")
            print("""
            """)

            ip = input("Enter IP Address : ")
            print (" Fetching data from " +ip)
            def get_location():
                ip_address = ip
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

                location_data = {
                "Ip Address" : ip_address, 
                "city" : response.get("city"),
                "region" : response.get("region"),
                "country" : response.get("country_name"),
                "Ip Address Type" : response.get("version"),
                "Region Code" : response.get("region_code"), 
                "Postal Code" : response.get("postal"), 
                "Latitude" : response.get(str("latitude")), 
                "Longitude" : response.get(str("longitude")), 
                "TimeZone" : response.get("timezone"), 
                "Country code" : response.get("country_calling_code"), 
                "Currency" : response.get("currency"), 
                "Currency Name" : response.get("currency_name") , 
                "Languages" : response.get("languages"), 
                "Country Area" : response.get("country_area"), 
                "Population" : response.get("country_population"),
                "ASN" : response.get("asn"), 
                "Organization" : response.get("org")

                }
                latitude = response.get("latitude")
                global lat
                lat = str(latitude)
                longitude = response.get("longitude")
                global long
                long = str(longitude)

                global url
                url = "https://google.com/maps/place/" + lat +  "," + long + "/@" + lat + "," + long + ",16z"

                return location_data
            map = input (Fore.CYAN + "\n\nDo you want to open location on google map? [yes/no]: " + Style.RESET_ALL)
else: 
 print("LÜTFEN DÜZGÜN KOMUT YAZ MK OĞLU")

 
 t.sleep(5) 
 os.system("clear")
 exit() 

print(f.renderText('FSM CYBER TEAM'))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("LÜTFEN yardım KOMUTUNU TERMİNALE YAZ")

E = '\033[0m'
H = '\033[95m'
tip = input(E+'FSM»TERMİNAL»'+H)
if tip == 'yardım':
            print("""
            komutlar :  TÜM KOMUTLARI SANA SÖYLER
            iptracker :  ip adressin bilgilerink bulur
            help :  YARDIM İÇİN KOMUT
            exit : TOOLDAN ÇIKARSIN
            
            update:  Its update Ip-Tracker automatically 
            """)
elif tip == "komutlar":
            print("""
            This are the available commands
            help
            show
            exit
            iptracker
            update
            ddos
            """)
elif tip == 'exit':
     os.system("clear")
     os.system("exit")
elif tip == "iptracker":
            print("""________________________________Track Ip____________________________""")
            print("""
            """)

            ip = input("Enter IP Address : ")
            print (" Fetching data from " +ip)
            def get_location():
                ip_address = ip
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

                location_data = {
                "Ip Address" : ip_address, 
                "city" : response.get("city"),
                "region" : response.get("region"),
                "country" : response.get("country_name"),
                "Ip Address Type" : response.get("version"),
                "Region Code" : response.get("region_code"), 
                "Postal Code" : response.get("postal"), 
                "Latitude" : response.get(str("latitude")), 
                "Longitude" : response.get(str("longitude")), 
                "TimeZone" : response.get("timezone"), 
                "Country code" : response.get("country_calling_code"), 
                "Currency" : response.get("currency"), 
                "Currency Name" : response.get("currency_name") , 
                "Languages" : response.get("languages"), 
                "Country Area" : response.get("country_area"), 
                "Population" : response.get("country_population"),
                "ASN" : response.get("asn"), 
                "Organization" : response.get("org")

                }
                latitude = response.get("latitude")
                global lat
                lat = str(latitude)
                longitude = response.get("longitude")
                global long
                long = str(longitude)

                global url
                url = "https://google.com/maps/place/" + lat +  "," + long + "/@" + lat + "," + long + ",16z"

                return location_data
            map = input (Fore.CYAN + "\n\nDo you want to open location on google map? [yes/no]: " + Style.RESET_ALL)
else: 
 print("LÜTFEN DÜZGÜN KOMUT YAZ MK OĞLU")

 t.sleep(5) 
 os.system("clear")
 exit()
 
 print(f.renderText('FSM CYBER TEAM'))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("LÜTFEN yardım KOMUTUNU TERMİNALE YAZ")

E = '\033[0m'
H = '\033[95m'
tip = input(E+'FSM»TERMİNAL»'+H)
if tip == 'yardım':
            print("""
            komutlar :  TÜM KOMUTLARI SANA SÖYLER
            iptracker :  ip adressin bilgilerink bulur
            help :  YARDIM İÇİN KOMUT
            exit : TOOLDAN ÇIKARSIN
            
            update:  Its update Ip-Tracker automatically 
            """)
elif tip == "komutlar":
            print("""
            This are the available commands
            help
            show
            exit
            iptracker
            update
            ddos
            """)
elif tip == 'exit':
            os.system("clear")
            os.system("exit")
elif tip == "iptracker":
            print("""________________________________Track Ip____________________________""")
            print("""
            """)

            ip = input("Enter IP Address : ")
            print (" Fetching data from " +ip)
            def get_location():
                ip_address = ip
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

                location_data = {
                "Ip Address" : ip_address, 
                "city" : response.get("city"),
                "region" : response.get("region"),
                "country" : response.get("country_name"),
                "Ip Address Type" : response.get("version"),
                "Region Code" : response.get("region_code"), 
                "Postal Code" : response.get("postal"), 
                "Latitude" : response.get(str("latitude")), 
                "Longitude" : response.get(str("longitude")), 
                "TimeZone" : response.get("timezone"), 
                "Country code" : response.get("country_calling_code"), 
                "Currency" : response.get("currency"), 
                "Currency Name" : response.get("currency_name") , 
                "Languages" : response.get("languages"), 
                "Country Area" : response.get("country_area"), 
                "Population" : response.get("country_population"),
                "ASN" : response.get("asn"), 
                "Organization" : response.get("org")

                }
                latitude = response.get("latitude")
                global lat
                lat = str(latitude)
                longitude = response.get("longitude")
                global long
                long = str(longitude)

                global url
                url = "https://google.com/maps/place/" + lat +  "," + long + "/@" + lat + "," + long + ",16z"

                return location_data
            map = input (Fore.CYAN + "\n\nDo you want to open location on google map? [yes/no]: " + Style.RESET_ALL)
else: 
 print("LÜTFEN DÜZGÜN KOMUT YAZ MK OĞLU")
 
 t.sleep(5) 
 os.system("clear")
 exit()
