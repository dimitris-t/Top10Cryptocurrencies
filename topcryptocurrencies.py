#!/usr/bin/python
# Requires Python 3
import argparse
import json
import re

# Customize this:
number_of_top_cryptocurrencies_to_consider = 10
# Customize this. Format is:
# cryptocurrenencies_to_ignore = ('Tether','Bitcoin')
cryptocurrenencies_to_ignore = ('Tether')

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
description='Parse top weekly cryptocurrencies from coinmarketcap.com/historical. Grab the files with:\n'
'wget -w 70 -r -l 1 --include-directories=historical https://coinmarketcap.com/historical/\n'
'In the generated historical folder run:\n'
'topcryptoccurencies.py */index.html\n\n'
'This script requires Python 3.')
parser.add_argument('file', metavar='FILE', nargs='*', help='HTML file(s) to read.')
args = parser.parse_args()

# Initialize the dictionary
top10cryptocurrencies = {}
# Initialise the list
top10cryptocurrencies_list = []

for file in args.file:
	filehandle = open(file,'r')
	for line in filehandle:
		# Look for the line that contains the JSON structure
		if re.match(r'.*__NEXT_DATA__.*',line):
			# Only keep the JSON string
			line = re.sub(r'.*<script id=\"__NEXT_DATA__\" type=\"application/json\">([^<]*)</script>.*',r'\1',line)
			# If you want to view the whole JSON structure
			# print (line)
			# Parse the JSON string
			day = json.loads(line)
			for cryptocurrency in day['props']['initialState']['cryptocurrency']['listingHistorical']['data']:
				# Only consider the top X cryptocurrencies and ignore certain ones e.g. stablecoins
				if cryptocurrency['rank'] <= number_of_top_cryptocurrencies_to_consider and not cryptocurrency['name'] in cryptocurrenencies_to_ignore:
					# Full name of cryptocurrency i.e. Bitcoin: cryptocurrency['name']
					# Cryptocurrency symbol i.e. BTC: cryptocurrency['symbol']
					# Rank on that day: cryptocurrency['rank']
					# Cryptocurrency price in USD: cryptocurrency['quote']['USD']['price']
					# Cryptocurrency price in BTC: cryptocurrency['quote']['BTC']['price']
					# Date in YYYYMMDD format: day['query']['date']
					if cryptocurrency['name'] in top10cryptocurrencies:
						top10cryptocurrencies[cryptocurrency['name']]['count'] += 1
						top10cryptocurrencies[cryptocurrency['name']]['last_date'] = day['query']['date']
					else:
						# If the dictionary entry for this cryptocurrency did not exist we need to initialize it
						top10cryptocurrencies[cryptocurrency['name']] = {'count' : 1, 'last_date' : day['query']['date']}
	filehandle.close()

# Turn the top10cryptocurrencies dictionary into the top10cryptocurrencies_list list so we can sort it
for item in top10cryptocurrencies.keys():
	top10cryptocurrencies_list.append((item,top10cryptocurrencies[item]['count'],top10cryptocurrencies[item]['last_date']))

# Sort the list by the 2nd column i.e. by count
top10cryptocurrencies_list.sort(key=lambda x:x[1],reverse=True)

# Print in CSV format
print ("Coin,Top "+str(number_of_top_cryptocurrencies_to_consider)+" Week Count,Last Top "+str(number_of_top_cryptocurrencies_to_consider)+" Date")
for item in top10cryptocurrencies_list:
	print (item[0]+','+str(item[1])+','+item[2])