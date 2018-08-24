import os
import socket
import threading
import random
import sys
 
def cri(cmd):
    subprocess.call(cmd, shell=True)
 
print ("\x1b[0;31m8888888b ")
print ("\x1b[0;31m888   Y88b ")
print ("\x1b[0;31m888    888 ")
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
print (" ")
print ("\x1b[0;31mSelect An Option:")
print ("\x1b[1;37m[\x1b[1;32m1\x1b[1;37m] -Windows SubDomain Scanner ")
print ("\x1b[1;37m[\x1b[1;33m2\x1b[1;37m] -Linux SubDomain Scanner")
 
choice = raw_input("\x1b[1;37m[root@Reaper ~]# ")
 
if choice == '1':
 
        os.system('cls')
 
        subdomains = ["dc", "test", "api", "embed", "old", "play", "ns2", "server1", "server2", "gateway", "app", "status", "media", "ts3", "ns1", "host", "dashboard", "blog", "autodiscovery", "beta", "dev", "wiki", "autoconfig", "irc", "irix", "fileserver", "backup", "agent", "c2c", "login", "mssql", "mysql", "localhost", "nameserver", "netstats", "mobile", "mobil",  "ftp", "webadmin", "uploads", "transfer", "tmp", "support", "smtp0#", "smtp#", "smtp", "sms", "shopping", "sandbox", "proxy", "manager", "cpanel", "webmail", "forum", "driect- connect", "vb", "forums", "pop#", "pop", "home", "direct", "mail", "access", "admin", "oracle", "monitor", "administrator", "email", "downloads", "ssh", "webmin", "paralel", "parallels", "www0", "www", "www1", "www2", "www3", "www4", "www5", "autoconfig.admin", "autoconfig", "autodiscover.admin", "autodiscover", "sip", "msoid", "lyncdiscover"]
        os.system ('color D')
        url = raw_input('Enter Hostname:')
        os.system ('color C')
 
        for cri in subdomains:
                try:
                        host = str(cri) + "." + str(url)
                        ip = socket.gethostbyname(str(host))
                        print '[REAPER] ~> [LOADING] ~> [NAMESERVER] ' + host + ' ~> [IP] ~> ' + ip
                except:
                        pass
 
if choice == '2':
 
        subdomains = ["dc", "test", "api", "old", "ns2", "play", "server", "server1", "server2", "gateway", "app", "media", "help", "embed", "status", "ns1", "host", "dashboard", "blog", "autodiscovery", "beta", "dev", "wiki", "autoconfig", "secure", "irc", "irix", "fileserver", "backup", "agent", "c2c", "ts3", "login", "mssql", "mysql", "localhost", "nameserver", "netstats", "mobile", "mobil",  "ftp", "webadmin", "uploads", "transfer", "tmp", "support", "smtp0#", "smtp#", "smtp", "sms", "shopping", "sandbox", "proxy", "manager", "cpanel", "webmail", "forum", "driect- connect", "vb", "forums", "pop#", "pop", "home", "direct", "mail", "access", "admin", "oracle", "monitor", "administrator", "email", "downloads", "ssh", "webmin", "paralel", "parallels", "www0", "www", "www1", "www2", "www3", "www4", "www5", "autoconfig.admin", "autoconfig", "autodiscover.admin", "autodiscover", "sip", "msoid", "lyncdiscover"]
        url = raw_input('\x1b[1;36mEnter Hostname\x1b[0;31m:\x1b[1;37m')
 
        for cri in subdomains:
                try:
                        host = str(cri) + "." + str(url)
                        ip = socket.gethostbyname(str(host))
                        print '\x1b[1;37m[\x1b[0;31mREAPER\x1b[1;37m] ~> [\x1b[1;36mLOADING\x1b[1;37m] ~> [\x1b[0;31mNAMESERVER\x1b[1;37m] ~>\x1b[1;36m ' + host + ' \x1b[1;37m~> [\x1b[0;31mIP\x1b[1;37m] ~>\x1b[1;36m ' + ip
                except:
                        pass