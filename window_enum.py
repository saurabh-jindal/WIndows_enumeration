import subprocess
commands = [
"net view", 
"netstat -nao", 
"net accounts", 
"ipconfig /all",
"ipconfig /displaydns",
"netstat -ns",
"cmd.exe /c set", 
"route print", 
"arp -a",
"netstat -vb",
"net localgroup administrator", 
"net view /domain",
"net session",
"net user", 
"net group administrator", 
"net localgroup ",
"tasklist /svc",
"net share", 
"netsh firewall show config", 
"gpresult /SCOPE USER /Z",
"gpresult /SCOPE COMPUTER /Z",
"wmic netlogin get name,lastlogon,badpasswordcount",
"wmic share get name,path",
"wmic nteventlog get path,filename,writeable",
"wmic logicaldisk get description,filesystem,name,size",
"wmic volumn list brief",
"wmic service list brief",
"wmic group list ",
"wmic net client list brief",
"wmic useraccount list ",
"wmic netuse get name,username,connectiontype,localname"
]

text = open('stored.txt','w+')
print("Running commands:...")
for command in commands:
	print('Running command: ',command)
	out=subprocess.check_output(command, shell = True)
	text.write(str(out))
text.close()



