# Fingerprintjs2-camper

This is a slight modification to the fingerprintjs2 module by LukasDrgon, so that it can be covertly deployed quickly.

### Usage

Suppose you use /var/www/html for the web root.
```
git clone https://github.com/pauljoohyunkim/fingerprintjs2-camper.git
mv fingerprintjs2-camper /var/www/html/
cd /var/www/html
nc -nlvp 5555       # For listening on port 5555, currently only supports localhost fingerprinting.
```

### Note
I am using `fetch` to send POST request, but it seems that my adblock blocks it from sending it to my Netcat listener.
