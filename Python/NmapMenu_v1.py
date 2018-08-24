import subprocess, socket
 
def cri(cmd):
    subprocess.call(cmd, shell=True)
 
print ("\x1b[1;32m       _   _                       __  __                   ")
print ("\x1b[1;32m      | \ | |                     |  \/  |                  ")
print ("\x1b[1;32m      |  \| |_ __ ___   __ _ _ __ | \  / | ___ _ __  _   _  ")
print ("\x1b[1;32m      | . ` | '_ ` _ \ / _` | '_ \| |\/| |/ _ \ '_ \| | | | ")
print ("\x1b[1;32m      | |\  | | | | | | (_| | |_) | |  | |  __/ | | | |_| | ")
print ("\x1b[1;32m      |_| \_|_| |_| |_|\__,_| .__/|_|  |_|\___|_| |_|\__,_| ")
print ("\x1b[1;32m                            | |                             ")
print ("\x1b[1;32m                            |_|    ")
print ("\x1b[1;32mSelect An Option:")
print ("\x1b[1;37m[\x1b[0;31m1\x1b[1;37m] -Intense Scan                \x1b[1;37m[\x1b[0;31m7\x1b[1;37m]  -Quick Scan, plus  ")
print ("\x1b[1;37m[\x1b[1;32m2\x1b[1;37m] -Instense Scan Plus UDP      \x1b[1;37m[\x1b[1;32m8\x1b[1;37m]  -Quick traceroute   ")
print ("\x1b[1;37m[\x1b[1;33m3\x1b[1;37m] -Intense Scan, all TCP Ports \x1b[1;37m[\x1b[1;33m9\x1b[1;37m]  -Regular scan   ")
print ("\x1b[1;37m[\x1b[1;34m4\x1b[1;37m] -Intense Scan, No Ping       \x1b[1;37m[\x1b[1;34m10\x1b[1;37m] -Slow comprehensive scan    ")
print ("\x1b[1;37m[\x1b[1;35m5\x1b[1;37m] -Ping Scan                   \x1b[1;37m[\x1b[1;35m11\x1b[1;37m] -IP GeoLocation    ")
print ("\x1b[1;37m[\x1b[1;36m6\x1b[1;37m] -Quick Scan                  \x1b[1;37m[\x1b[1;36m12\x1b[1;37m] -SubDomain Scanner    ")
 
choice = raw_input("\x1b[1;37m[\x1b[1;32mroot\x1b[1;37m@\x1b[1;32mNmap\x1b[1;37m ~]#\x1b[1;32m ")
 
if choice == '1':
 
 ip = raw_input("\x1b[1;37mEnter The Desired IP You Want To Scan:\x1b[1;32m ")
 direct = raw_input("\x1b[1;37mEnter The Desired OutPut File:\x1b[1;32m")

 cri("nmap -T4 -A -v "+ ip +" && nmap -T4 -A -v "+ ip +" > "+ direct +"")

if choice == '2':
 
 ip = raw_input("\x1b[1;37mEnter The Desired IP You Want To Scan:\x1b[1;32m ")
 direct = raw_input("\x1b[1;37mEnter The Desired OutPut File:\x1b[1;32m")

 cri("nmap -sS -sU -T4 -A -v "+ ip +" && nmap -T4 -A -v -Pn "+ ip +" > "+ direct +"")


if choice == '3':
 
 ip = raw_input("\x1b[1;37mEnter The Desired IP You Want To Scan:\x1b[1;32m ")
 direct = raw_input("\x1b[1;37mEnter The Desired OutPut File:\x1b[1;32m")

 cri("nmap -p 1-65535 -T4 -A -v "+ ip +" && nmap -T4 -A -v -Pn "+ ip +" > "+ direct +"")

if choice == '4':
 
 ip = raw_input("\x1b[1;37mEnter The Desired IP You Want To Scan:\x1b[1;32m ")
 direct = raw_input("\x1b[1;37mEnter The Desired OutPut File:\x1b[1;32m")

 cri("nmap -T4 -A -v -Pn "+ ip +" && nmap -T4 -A -v -Pn "+ ip +"  > "+ direct +"")

if choice == '5':
 
 ip = raw_input("\x1b[1;37mEnter The Desired IP You Want To Scan:\x1b[1;32m ")
 direct = raw_input("\x1b[1;37mEnter The Desired OutPut File:\x1b[1;32m")

 cri("nmap -sn "+ ip +" && nmap -T4 -A -v -Pn "+ ip +" > "+ direct +"")

if choice == '6':
 
 ip = raw_input("\x1b[1;37mEnter The Desired IP You Want To Scan:\x1b[1;32m ")
 direct = raw_input("\x1b[1;37mEnter The Desired OutPut File:\x1b[1;32m")

 cri("nmap -T4 -F "+ ip +" && nmap -T4 -A -v -Pn "+ ip +" > "+ direct +"")

if choice == '7':
 
 ip = raw_input("\x1b[1;37mEnter The Desired IP You Want To Scan:\x1b[1;32m ")
 direct = raw_input("\x1b[1;37mEnter The Desired OutPut File:\x1b[1;32m")

 cri("nmap -sV -T4 -O -F --version-light "+ ip +" && nmap -T4 -A -v -Pn "+ ip +" > "+ direct +"")

if choice == '8':
 
 ip = raw_input("\x1b[1;37mEnter The Desired IP You Want To Scan:\x1b[1;32m ")
 direct = raw_input("\x1b[1;37mEnter The Desired OutPut File:\x1b[1;32m")

 cri("nmap -sn --traceroute "+ ip +" && nmap -T4 -A -v -Pn "+ ip +" > "+ direct +"")

if choice == '9':
 
 ip = raw_input("\x1b[1;37mEnter The Desired IP You Want To Scan:\x1b[1;32m ")
 direct = raw_input("\x1b[1;37mEnter The Desired OutPut File:\x1b[1;32m")

 cri("nmap "+ ip +" && > "+ direct +"")

if choice == '10':
 
 ip = raw_input("\x1b[1;37mEnter The Desired IP You Want To Scan:\x1b[1;32m ")
 direct = raw_input("\x1b[1;37mEnter The Desired OutPut File:\x1b[1;32m")

 cri("nmap -sS -sU -T4 -A -v -PE -PP -PS80,443 -PA3389 -PU40125 -PY -g 53"+ ip +" && nmap -T4 -A -v -Pn "+ ip +" > "+ direct +"")

if choice == '11':
 
 ip = raw_input("\x1b[1;37mEnter The Desired IP You Want To Scan:\x1b[1;32m ")
 direct = raw_input("\x1b[1;37mEnter The Desired OutPut File:\x1b[1;32m")

 cri("curl ipinfo.io/"+ ip +" && nmap -T4 -A -v -Pn "+ ip +" > "+ direct +"")

if choice == '12':

        subdomains = ["dc", "test", "api", "old", "ns2", "play", "server", "server1", "server2", "gateway", "app", "media", "help", "embed", "status", "ns1", "host", "dashboard", "blog", "autodiscovery", "beta", "dev", "wiki", "autoconfig", "secure", "irc", "irix", "fileserver", "backup", "agent", "c2c", "ts3", "login", "mssql", "mysql", "localhost", "nameserver", "netstats", "mobile", "mobil",  "ftp", "webadmin", "uploads", "transfer", "tmp", "support", "smtp0#", "smtp#", "smtp", "sms", "shopping", "sandbox", "proxy", "manager", "cpanel", "webmail", "forum", "driect- connect", "vb", "forums", "pop#", "pop", "home", "direct", "mail", "access", "admin", "oracle", "monitor", "administrator", "email", "downloads", "ssh", "webmin", "paralel", "parallels", "www0", "www", "www1", "www2", "www3", "www4", "www5", "autoconfig.admin", "autoconfig", "autodiscover.admin", "autodiscover", "sip", "msoid", "lyncdiscover"]
        url = raw_input('\x1b[1;36mEnter Hostname\x1b[0;31m:\x1b[1;37m')

        for cri in subdomains:
                try:
                        host = str(cri) + "." + str(url)
                        ip = socket.gethostbyname(str(host))
                        print '\x1b[1;37m[\x1b[0;31mREAPER\x1b[1;37m] ~> [\x1b[1;36mLOADING\x1b[1;37m] ~> [\x1b[0;31mNAMESERVER\x1b[1;37m] ~>\x1b[1;36m ' + host + ' \x1b[1;37m~> [\x1b[0;31mIP\x1b[1;37m] ~>\x1b[1;36m ' + ip
                except:
                        pass
