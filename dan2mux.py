#!usr/bin/python
#//Hapus Recode?Lu Bukan Coder Bro!

import sys
import os

os.system ('clear')
os.system ('pkg install figlet -y')
os.system ('pkg install ruby -y')
os.system ('pkg install cowsay -y')
os.system ('pkg install toilet -y')
os.system ('gem install lolcat')
os.system ('clear')

yat = """//Code By CodayID//@hiidayt//TSC#ACTng#SD//"""

ct = """//+62 888-0928-0542//DanDanTermux//"""

os.system ('figlet DAN2muX')
print yat
print ct
print ("Example : roor@codayid")

ytnick = raw_input ("Nick Kamu :")

yat = open ("bash.bashrc","w")
yt1 =  """PS1='}{ploit@"""
yt2 = ytnick
yt3 = """]> '
clear 
cowsay -f eyes " """
yt4 = ytnick
yt5 = """ " | lolcat 
toilet -f standard " """
yt6 = ytnick
yt7 = """ " -F gay | lolcat"""
yat.write (yt1)
yat.write (yt2)
yat.write (yt3)
yat.write (yt4)
yat.write (yt5)
yat.write (yt6)
yat.write (yt7)
yat.close ()
 
print ("TUNGGU SEBENTAR, SEDANG MEMPROSES")

os.system ('rm $HOME/../usr/etc/bash.bashrc')
os.system ('cp -f bash.bashrc  $HOME/../usr/etc')

print ("SUKSES!!! SILAHKAN REFRASH TERMUX ANDA")
