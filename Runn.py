#!/usr/bin/env python
#coding: utf-8

 
import codecs
import binascii
from time import sleep
import sys
import os


Clears = "clear"
Run = "python Installer.py"
Jeda = "sleep 3"
Pause = "sleep 10"


def Gator_Bks():
	os.system(Clears)
	print("""\033[91m	╔╦═╦╗╔═╗╔╗─╔═╗╔═╗╔═╦═╗╔═╗ ╔══╗╔═╗
	║║║║║║╦╝║║─║╔╝║║║║║║║║║╦╝ ╚╗╔╝║║║
\033[97m	║║║║║║╩╗║╚╗║╚╗║║║║║║║║║╩╗ ─║║─║║║
	╚═╩═╝╚═╝╚═╝╚═╝╚═╝╚╩═╩╝╚═╝ ─╚╝─╚═╝
\033[93m		  ▇ ◢▇▇▇◣◢▇▇▇◣ ▇
\033[93m		  ▇▇▇▇▇▇▇▇▇▇▇▇▇▇
\033[93m		  ▇\033[91m╳\033[93m◥▇▇▇▇▇▇▇▇◤\033[91m╳\033[93m▇
\033[93m		  ▇\033[91m╳╳\033[93m◥▇▇▇▇▇▇◤\033[91m╳╳\033[93m▇
\033[93m		  ▇\033[91m╳╳╳\033[93m◥▇▇▇▇◤\033[91m╳╳╳\033[93m▇
\033[93m		  ▇\033[91m╳╳╳╳\033[93m▇▇▇▇\033[91m╳╳╳╳\033[93m▇
\033[93m		  ◥▇▇▇▇▇▇▇▇▇▇▇▇◤
\033[93m 		   ◥▇▇▇▇\033[91m◢◣\033[93m▇▇▇▇◤
\033[93m  		    ◥▇▇▇▇▇▇▇▇◤
\033[93m    		     ◥▇▇▇▇▇▇◤
\033[96m╔══╗╔══╗╔══╗╔═╗╔═╗ ╔══╗╔╦╗╔══╗ ╔══╗╔═╗╔═╗╔╗─╔══╗
║╔═╣║╔╗║╚╗╔╝║║║║╬║ ║╔╗║║╔╝║══╣ ╚╗╔╝║║║║║║║║─║══╣
\033[94m║╚╗║║╠╣║─║║─║║║║╗╣ ║╔╗║║╚╗╠══║ ─║║─║║║║║║║╚╗╠══║
╚══╝╚╝╚╝─╚╝─╚═╝╚╩╝ ╚══╝╚╩╝╚══╝ ─╚╝─╚═╝╚═╝╚═╝╚══╝
\033[92m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●\033[0m
\033[0m • Gunakan Tools Ini Dengan Bijak!!!
\033[0m • Dilarang Memperjual Belikan Tools Ini Tanpa
\033[0m   Seizin Saya!!!
\033[0m • Dilarang Keras Untuk Recode Tools Ini Tanpa
\033[0m   Seizin Saya!!
\033[0m • For Credit/Bug Chat WA : 081310662343
\033[92m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
\033[0m
""")


def NFZ():
	Gator_Bks()
	User = input("\033[91m[\033[93m+\033[91m]\033[93m Username\033[92m :\033[0m ")
	Pass = input("\033[91m[\033[93m+\033[91m]\033[93m Password\033[32m :\033[0m ")
	
	
	if User == "GBKS" and Pass == "SuperTools":
		login()
	elif User != "GBKS" and Pass == "SuperTools":
		Gator_Bks()
		print("\033[92m[\033[93m+\033[92m]\033[91m Username Salah!!!")
		print("\033[37m")
		print("\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Username Dengan Benar!!!")
		print("\033[37m")
		os.system(Jeda)
		NFZ()
	elif User == "GBKS" and Pass != "SuperTools":
		Gator_Bks()
		print("\033[92m[\033[93m+\033[92m]\033[91m Password Salah!!!")
		print("\033[37m")
		print("\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Password Dengan Benar!!!")
		print("\033[37m")
		sleep(3)
		NFZ()
	else:
		os.system(Clears)
		Gator_Bks()
		print("\033[92m[\033[93m+\033[92m]\033[91m Username & Password Salah!!!")
		print("\033[37m")
		print("\033[92m[\033[93m+\033[92m]\033[91m Harap Masukkan Username & Password Dengan Benar!!!")
		print("\033[37m")
		os.system(Jeda)
		NFZ()
	
	
def login():
	os.system(Clears)
	Gator_Bks()
	print("\033[96m[\033[93m+\033[96m]\033[93m Login Berhasil")
	print("\n")
	os.system(Jeda)
	os.system(Clears)
	print("\n")
	print("\033[92m[\033[93m+\033[92m]\033[93m Author By ǴaͲor βks")
	print("\033[92m[\033[93m+\033[92m]\033[96m Terima Kasih Telah Menggunakan Tools Ini ●‿○")
	print("\n")
	print("\n")
	os.system(Jeda)
	os.system(Clears)
	print("\n")
	print("\033[96m[\033[93m+\033[96m]\033[93m Sedang Mempersiapkan Tools Harap Tunggu Sebentar...")
	os.system(Pause)
	os.system(Clears)
	print("\n")
	Bang_Jago = input("\033[92m[\033[93m+\033[92m]\033[93m Tekan Enter Untuk Melanjutkan Program")
	os.system(Run)


NFZ()
