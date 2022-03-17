# Tortuga [COMPLETE GUIDE]
## Pirates ONLY!

### Legal Notice
This is the complete guide to Turtuga. This is for practice and not to be deployed maliciously. Use at your own risk and I hold no resposibility for the use of this server.

### Server Setup
- download the .ova file for virutalbox
- server should be setup to NAT network [ kali box should be using the same NAT network ]
- verify with a netdiscovery     
```
sudo netdiscover -r [your ip address]
```

### Walkthrough GUIDE
- Scan the network with netdiscover -r is for range
```
sudo netdiscover -r 10.0.2.0
```
- Use nmap for additional information 
```
sudo nmap -sV -sN -T4 -A -O 10.0.2.10 -p-
```