import socket
import urllib
import hashlib
 
HOST = '35.204.90.89'    # The remote host
PORTS = [5555,5560]              # The same port as used by the server
 
for port in PORTS:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, port))
    data = s.recv(1024)
    print repr(data)
    link = "http://md5decrypt.net/Api/api.php?hash={}&hash_type=md5&email=nugoprasep@2anom.com&code=0e1486cda89a030b".format(data)
    print link
    f = urllib.urlopen(link)
    number = f.read()
    new_number = int(number) + 1
    s.sendall(hashlib.sha512(new_number).hexdigest())
    data = s.recv(1024)
    print 'Received', repr(data)
    s.close()