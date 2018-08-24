import subprocess

def cri(cmd):
    subprocess.call(cmd, shell=True)

print ("\x1b[1;35m __      __          __  __                    ")
print ("\x1b[1;35m \ \    / /         |  \/  |                   ")
print ("\x1b[1;35m  \ \  / / __  _ __ | \  / | ___ _ __  _   _   ")
print ("\x1b[1;35m   \ \/ / '_ \| '_ \| |\/| |/ _ \ '_ \| | | |  ")
print ("\x1b[1;35m    \  /| |_) | | | | |  | |  __/ | | | |_| |  ")
print ("\x1b[1;35m     \/ | .__/|_| |_|_|  |_|\___|_| |_|\__ _|  ")
print ("\x1b[1;35m        | |                                    ")
print ("\x1b[1;35m        |_|                                    ")
print ("\x1b[1;37m[\x1b[1;35mVpnMenu v1\x1b[1;37m] Developed By \x1b[1;35mFlexingOnLamers \x1b[1;37m|| \x1b[1;35mCri")
print ("\x1b[1;35mSelect An Option:")
print ("\x1b[1;37m[\x1b[0;31m1\x1b[1;37m] ~~> Downloads all Needed Dependencies    ")
print ("\x1b[1;37m[\x1b[1;32m2\x1b[1;37m] ~~> Downloads All Scripts                ")
print ("\x1b[1;37m[\x1b[1;33m3\x1b[1;37m] ~~> Sets Up OpenVPN                      ")
print ("\x1b[1;37m[\x1b[1;34m4\x1b[1;37m] ~~> Sets Up Softether                    ")
print ("\x1b[1;37m[\x1b[1;35m5\x1b[1;37m] ~~> Adds Users to SoftEther              ")
print ("\x1b[1;37m[\x1b[1;36m6\x1b[1;37m] ~~> Adds Users to OpenVPN                ")

option = input ("\x1b[1;37m[\x1b[1;35mroot\x1b[1;37m@\x1b[1;35mVpnMenu\x1b[1;37m ~]#\x1b[1;35m ")

if option == 1:
  OS = raw_input("\x1b[1;36mDebian \x1b[1;37mor \x1b[0;31mCentOS\x1b[1;37m:\x1b[1;35m")
if OS == "Debian":
 cri("apt-get update && upgrade -y")
 cri("apt-get install lsof git -y")
 cri("apt-get install gcc dstat iftop screen scapy iptraf-ng -y")
 cri("apt-get install curl -y")
 cri("apt-get install apache2 -y")
 cri("apt-get install php5 php-pear php5-mysql -y")
 cri("apt-get install tcpdump nmap -y")
 cri("apt-get install scapy -y")
 cri("python VpnMenu.py")
elif OS == "CentOS":
 cri("yum update -y")
 cri("yum install python-paramiko gcc screen nano wget httpd iptables perl -y")
 cri("yum install gcc cmake gmp gmp-devel libpcap-devel gengetopt byacc flex -y")
 cri("yum install json-c-doc.noarch json-c.i686 json-c.x86_64 json-c-devel.i686 json-c-devel.x86_64 -y")
 cri("yum install epel-release -y")
 cri("yum install gengetopt -y")
 cri("yum install lsof dstat iftop iptraf-ng git -y")
 cri("python VpnMenu.py")
if option == 2:
 cri("wget https://git.io/vpn -O openvpn-install.sh")
 cri("wget -q https://pastebin.com/raw/v3StmF23 -O softether.py")
 cri("wget -q https://pastebin.com/raw/BhuTQYnn -O softetheradd.py")
if option == 3:
	cri("bash openvpn-install.sh")
if option == 4:
	cri("python softether.py")
if option == 5:
	cri("python softetheradd.py")
if option == 6:
	cri("bash openvpn-install.sh")
