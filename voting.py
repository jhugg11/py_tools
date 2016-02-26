import hashlib
import urllib
import urllib2
import sys
from datetime import datetime
from dateutil import parser

'''
Example response with 'username' input:
{"vote":"non-academic"}

Example response with no 'username' input:
[{"first_name":"Jennifer","last_name":"Sample","middle_name":null,"campus_desc":"History","title_desc":"Vstng Asst Prof 10m","role_desc":"Faculty","vote":"academic","email":"sample@sample.edu"}]

'''
#date must be in yyyyMMddHHmmss format
date = datetime.now().strftime('%Y%m%d%H%M%S')

#simple hash that expires after a few seconds on the Grails webservice end
def create_hash(date, shared_secret):
		date_secret_unicode = unicode(date+shared_secret, "UTF-8")
		m = hashlib.md5()
		m.update(date_secret_unicode)
		m.digest()
		hash_str = m.hexdigest()
		return hash_str

shared_secret = os.environ['SECRET']
hash_str = create_hash(date, shared_secret)

#user interface for testing purposes
q1 = raw_input("username (leave blank for all)?  ")
if q1 is not '':
		username = '&username='+q1
else:
		username = ''

#you can base your call on this basic template
url = os.environ['PSNU_URL'] + '?timeStamp='+date+'&hash='+hash_str+username
print url
#output response and url for testing purposes
response = urllib2.urlopen(url)
html = response.read()
print url
print html
