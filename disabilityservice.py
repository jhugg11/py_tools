import hashlib
import urllib
import urllib2
import sys
import os
from datetime import datetime
from dateutil import parser

def date = datetime.now().strftime('%Y%m%d%H%M%S')

def devprod = raw_input("[1]dev [2]prod [3]local: ")

def create_hash(date, shared_secret):
		date_secret_unicode = unicode(date+shared_secret, "UTF-8")
		m = hashlib.md5()
		m.update(date_secret_unicode)
		m.digest()
		hash_str = m.hexdigest()
		return hash_str

def username = raw_input('username? ')

def search_params = '?timeStamp='+date+'&hash='+hash_str+'&username='+username

if (username):
		shared_secret = os.environ['SECRET']
		hash_str = create_hash(date, shared_secret)
		if (devprod == '1'):
				url = os.environ['DEV_URL'] + search_params
		elif (devprod == '2'):
				url = os.environ['PROD_URL'] + search_params
		elif (devprod == '3'):
				url = url = os.environ['LOCAL_URL'] + search_params
else:
		print "no username entered."

print url
response = urllib2.urlopen(url)
html = response.read()
print html
