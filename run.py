#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  run.py
#  
#  Copyright 2013 [mad]Berry <madberry@hush.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 

### Please send donations to:
#btc: 1Q2QDC78uaGgkm4r3G5YzZSriPv7KMUuQU
#ltc: Lb5TUyhdUtqsExLmiyqCLAiBZUrs8mEYze
# Thanks.  

import simplejson
import json
import urllib2
import urllib
import os

# Variables used to run the script

part1 = '348293' #change this to something else
part2 = '223393' #change this to something else
part3 = '291029' #change this to something else
password = 'dasuiausua7soq' #change this to something else needs to be 14 chars
less_than = 55000 #Bet less than "offset" 
'''
60000 = 91.6%    odds wins     1.081x
55000 = 83.9%    odds wins     1.179x
32768 = 50.0%    odds wins     1.98x
16384 = 25.0%    odds wins     3.96x
 7000 = 10.7%    odds wins     9.268x
 2400 = 3.66%    odds wins    27.03x
 1000 = 1.53%    odds wins    64.88x
    1 = 0.00153% odds wins 64880x
'''
#max_bet = 4000 # Maximum bet 4000=0.00004 || Not used yet
min_bet = 1000 # Minimum bet can't be lower then 1000=0.00001
max_loss = 1 # stop after X losses
max_wins = 3
rate_limit = 0 #Rate limit in seconds, currently 1 bet per 10 sec.

#-------Any changes below this line might break the script------

__prog__ = "coinroll.it automated gambling script"
__scriptname__ = "run.py"
__author__ = "[mad]Berry"
__date__ = "$May 07, 2013 17:10:45 PM$"
__version__ = "1.0"

part1 = part1.encode('hex')
part2 = part2.encode('hex')
part3 = part3.encode('hex')
part1 = part1[:-(len(part1)-4)]
part2 = part2[:-(len(part2)-4)]
part3 = part3[:-(len(part3)-4)]
user = part1 + '-' + part2 + '-' + part3 

class Error(Exception):
    pass

def pause(n, post=False):
	import time
	import sys
	if post:
		print "Start : %s" % time.ctime()
	while n != 0:
		time.sleep(1)
		sys.stdout.write("Sleeping for: %d   \r" % (n) )
		sys.stdout.flush()
		n = n -1
	print "                     "

def call(api_url, **kwargs):
	try:
		baseurl = 'https://coinroll.it/'
		api_url = baseurl + api_url
		data = urllib.urlencode(kwargs) #({'user': user, 'password': password})
		header = {
					"Content-type": "application/x-www-form-urlencoded",
					"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.46 Safari/535.11"
				}
		req = urllib2.Request(api_url, data, header)
		response = urllib2.urlopen(req)
		result = response.read()
		result = simplejson.loads(result)
		if 'error' in result:
		# An error occurred; raise an exception
			raise Error({'message': result['error']})
			exit(1)
		return result
	except Exception, e:
		print e.args[0]['message']
		exit(1)
		
def firstrun():
	print 'here'
	if os.path.isfile('cred.txt'): 
		print 'Success we already have credentials'
		file = open('cred.txt','r')
		address = file.read()
		file.close()
		print address
		pass
	else:
		result = call('deposit/', user=user, password=password)
		file = open('cred.txt','w')
		file.write(result['address'])
		print 'Send a deposit to:', result['address'], 'to create the new account'
		file.close() 

def main():
	#firstrun()
	#check balance
	#result = call('getbets', user=user, password=password, offset=60000)
	'''
	{'count': 4, 'bets': [{'nonce': 3, 'timestamp': 1367964483126, 'display': 1081, 'win': True, 'lessthan': 60000, 'lucky': 16884, 'amount': 1000, 'num': 4, 'multiplier': 1.081, 'date': 'May 7 2013 - 22:08', 'diff': 81, 'id': 'fe04d2818b69'}, {'nonce': 2, 'timestamp': 1367964395023, 'display': 1081, 'win': True, 'lessthan': 60000, 'lucky': 8810, 'amount': 1000, 'num': 3, 'multiplier': 1.081, 'date': 'May 7 2013 - 22:06', 'diff': 81, 'id': '22e02832ae67'}, {'nonce': 1, 'timestamp': 1367963757823, 'display': 1081, 'win': True, 'lessthan': 60000, 'lucky': 8429, 'amount': 1000, 'num': 2, 'multiplier': 1.081, 'date': 'May 7 2013 - 21:55', 'diff': 81, 'id': '39390fa2aaa9'}, {'nonce': 0, 'timestamp': 1367960796804, 'display': -1000, 'win': False, 'lessthan': 60000, 'lucky': 60196, 'amount': 1000, 'num': 1, 'multiplier': 1.081, 'date': 'May 7 2013 - 21:06', 'diff': -1000, 'id': '515e8d110c88'}], 'result': 1}
	'''
	#result = call('querybet', id='515e8d110c88')
	'''
	{'nonce': 0, 'win': False, 'secret': 'in 6 hours', 'lucky': 60196,
	 'secretHash': '5bc0a2b7d9851e08496e95195f14f36c51e31a6da89c1fec07c99a2e6c496fbe', 
	 'txid': '443f638e5a77dde8472f2e6d25a62da4701ecedcc6bae98f476f613935c6b23b', 
	 'released': False, 'lessthan': 60000, 'user': '3332-3332-3830', 
	 'timestamp': 'May 7 2013 - 21:06', 'delta': 0, 'amount': 1000, 
	 'id': '515e8d110c88', 'multiplier': 1.081, 'result': 1}
	'''
	resultloss = call('getbalance', user=user, password=password)
	initial_loss = resultloss['bets'] - resultloss['wins']
	initial_wins = resultloss['wins']
	while True:
			resultloss = call('getbalance', user=user, password=password)
			'''
			{'bets': 4, 'wins': 3, 'profit': -757, 'balance': 1999243, 'result': 1}
			'''
			print resultloss
			wins = initial_wins+max_wins
			if ( resultloss['wins'] == wins):
				print 'won', max_wins, 'exiting'
				exit(0)
			else:
				pass
			losses = resultloss['bets'] - resultloss['wins']
			if (losses >= max_loss):
				max_lost = initial_loss+max_loss
			else:
				max_lost = max_loss
			if (losses == max_lost):
				print 'Lost to much exiting'
				break;
			else:
				print 'Lost only', losses, 'which is less than', losses,'-',max_lost, '\nplacing another bet I will stop after', max_lost, 'total lost'
				result = call('bet',user=user, password=password, lessthan=less_than,amount=min_bet)
				'''
				{'bets': 4, 'nonce': 3, 'profit': -757, 'wins': 3, 
				'lessthan': 60000, 'lucky': 16884, 'display': 1081, 'amount': 1000,
				'result': 1, 'multiplier': 1.081, 'date': 'May 7 2013 - 22:08',
				'diff': 81, 'balance': 1999243, 'win': True, 'id': 'fe04d2818b69'}
				'''
			pause(rate_limit) 
	#print result
	#515e8d110c88
	return 0

if __name__ == '__main__':
	import logging
	import optparse
	parser = optparse.OptionParser(version= __prog__ + " " + __version__ + "\nDeveloped by: " + __author__)
	parser.add_option("-n", "--new", action="store_true", dest="new",
			help=("Add a new account, your address will be added to cred.txt"))
	(options, args) = parser.parse_args()
	if options.new == True:
		firstrun()
	else:
		main()

