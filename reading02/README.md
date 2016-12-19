Reading 02
==========

1. uname > uname.txt
2. The ip of eth0 on the local machine student02 is 129.74.152.75
I found this by using: /sbin/ifconfig
3. nslookup nd.edu
I found that the ip address associated witht the nd.edu domain name is 52.6.129.12
4. I was able to verify that the machine student02 is responsive by using the 
ping <ipaddress> command and verifying the output
5. In order to transfer a file between two machines, I would use the ftp command,
followed by the send command within the ftp text-based interface.
6. Use: tmux new -s session-name to create the new 
detachable session (tmux detach in order to detach), and when you want to re attach you
can use: tmux a -t session-name
7. wget -O <path> "http://downloadurl"
8. nmap <ipaddress>
My results for: nmap 129.74.152.75
Starting Nmap 5.51 ( http://nmap.org ) at 2016-01-24 17:08 EST
Nmap scan report for student02.cse.nd.edu (129.74.152.75)
Host is up (0.00047s latency).
Not shown: 995 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
111/tcp  open  rpcbind
5989/tcp open  wbem-https
8649/tcp open  unknown
9618/tcp open  condor

Nmap done: 1 IP address (1 host up) scanned in 0.07 seconds