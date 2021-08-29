import requests
from threading import Thread
import os
from time import sleep

os.system("clear")
print("[==]============================[==]=====[ MOTIVATION ]======[==]")
print("                                [==]                             ")
print("          Created by Perl.      [==] Code only on Linux!         ")
print("                                [==] Have a nice Hack ;)         ")
print("[=========[ DESCRIPTION ]==========]                             ")
print("                                [==]====[==]=====[==]========[==]")
print("                                                                 ")
print("      Name: DDoS Link Destroyer          #@@@@#                  ")
print("      Version: 1.5.rc1                  @WWWWWWW@*               ")
print("                                       @WWWWWWWWW                ")
print("                                        WWWWWWWW@                ")
print("                                          @WWWW@*                ")
print("      What you need?                  #=##W@@@#@@@@@@=           ")
print("                                     #@@@@@@@@@@@@@@@@##         ")
print("      1)Target Link                  @##*****=*+++*==#@#@#       ")
print("                                   ##*+++++++++++++++@@@#        ")
print("                                  ##@@++++Eternal+++*@@@@#       ")
print("                                 @@@@@*++Destroyers+#=#@@        ")
print("                                 @@@@@@*+*******=**=#@@@@        ")
print("                                  @@@@@#*==##@#####==@@@@        ")
print("                                      @####@@@@@@@@@####         ")
print("                                                                 ")
print("[==]============================[==]=========================[==]")

global url
url = input("[?]Enter Url:>>> ")

islemler = """ 
[==]=============================================[==]
     And so choose the amount of timeout [max:5]
[==]=============================================[==]
"""

print(islemler)

global thrd
thrd = int(input("[?][Enter attack number]:> "))
bomb = requests.get(url)
global sonuc
sonuc = bomb.status_code


class thrds():
    @classmethod
    def errororno(self, ls):
        if ls == 200:
            return 'OK/WORKING'
        else:
            return 'ERROR/NO WORKING'

    @classmethod
    def islem(self):
        while True:
            yazi = f"[{thrd} Level][*][Attack to {url}\n site-status [=]:> {self.errororno(sonuc)} <:]\n"
            print(yazi)
            sleep(2)

    @classmethod
    def thr(self):
        for _ in range(thrd):
            thread = Thread(target=self.islem)
            thread.start()
ths = thrds().thr()
