import socket

def scan(target,ports):
    for port in range(1,ports):
        scan_port(target,ports)

def scan_port(ip,port):
    try:
        sock=socket.socket()
        sock.connect((ip,port))
        print("[+] port opened " + str(port))
        sock.close()
    except:
        pass

targets=input("[*] Enter Target to scan(split them by ,): ")
ports=int(input("[*] Enter How many ports you want to scan: "))
if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '),ports)
else:
    scan(targets,ports)


