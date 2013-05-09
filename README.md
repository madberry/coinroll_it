coinroll_it
===========

Automated gambling script for <a href="http://coinroll.it" target="_blank">coinroll.it</a>

Change user and password. Set the variables and let em roll.

The variables to set should be pretty straight forward see below:

```python
# Variables used to run the script

user='' #userid from the site
password = '' #password from the site
less_than_min = 50000 #Bet less than minimum 64000, 60000, 55000 etc. 
less_than_max = 64000 #Bet less than maximum 64000, 60000, 55000 etc.
max_bet = 5000 # Maximum bet 5000=0.00005
min_bet = 2500 # Minimum bet can't be lower then 1000=0.00001
max_loss = 50 # stop after X losses
rate_limit = 0 #Rate limit in seconds Be a good guy and rate_limit your
			   # bets.  This will make the script fall a sleep for XX sec.
```

Enjoy.

Thanks to <a href="https://github.com/grimd34th" target="_blank">grimd34th</a> and any future contributors.

If this was in anyway useful to you then please consider donating:

btc: 1Q2QDC78uaGgkm4r3G5YzZSriPv7KMUuQU <br />
ltc: Lb5TUyhdUtqsExLmiyqCLAiBZUrs8mEYze

bitcointalk thread:
<a href="https://bitcointalk.org/index.php?topic=198727" target="">https://bitcointalk.org/index.php?topic=198727</a>
