#coding=utf-8

import os, sys, platform

try:

    import requests

except:

    os.system('pip2 install requests')

import requests

if not os.path.isfile('HaMza.so):

    os.system('curl -L https://raw.githubusercontent.com/HaMza-Khalil/HaMzaBrand/main/hamza.so > hamza.so')

    os.system('clear')

if not os.path.isfile('KhaLil.so'):

    os.system('curl -L https://raw.githubusercontent.com/HaMza-KhaLil/HaMzaBrand/main/hamza.so > hamza.so')

    os.system('clear')

bit=platform.architecture()[0]

go = requests.get('https://raw.githubusercontent.com/HaMza-Khalil/ArainBadshah/main/update.txt').text

if 'HaMzaBrand in go:

    if bit == '64bit':

        from Jutt import reg

        reg()

    elif bit == '32bit':

        from brand import reg

        reg()

else:

    os.system('rm -rf hamza.so khalil.so')

    os.system('curl -L https://raw.githubusercontent.com/HaMza-KhaLil/HaMzaBrand/main/hamza.so > hamza.so')

    os.system('curl -L https://raw.githubusercontent.com/HaMza-KhaLil/HaMzaBrand/main/hamza.so > hamza.so')

    if bit == '64bit':

        from HaMza import reg

        reg()

    elif bit == '32bit':

        from KhaLil import reg

        reg()

